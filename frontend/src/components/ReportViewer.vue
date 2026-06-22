<template>
  <div class="animate-fade-up">

    <!-- ── Metadata bar ── -->
    <div class="glass rounded-2xl border border-white/8 p-5 mb-5
                flex flex-col sm:flex-row sm:items-center justify-between gap-4 report-meta-bar">

      <!-- Left: meta chips -->
      <div class="flex flex-wrap gap-4">
        <div v-for="meta in metaItems" :key="meta.label" class="flex flex-col gap-0.5">
          <span class="text-[10px] font-mono uppercase tracking-widest" style="color: var(--dim)">
            {{ meta.label }}
          </span>
          <span class="text-sm font-semibold" style="color: var(--text)">
            {{ meta.value }}
          </span>
        </div>
      </div>

      <!-- Right: action buttons -->
      <div class="report-actions flex gap-2 shrink-0">

        <!-- Copy -->
        <button
          @click="copyReport"
          :class="[
            'flex items-center gap-2 px-4 py-2 rounded-xl text-sm font-semibold border transition-all duration-300',
            copied
              ? 'bg-teal-500/15 border-teal-400/50 text-teal-300'
              : 'glass border-white/10 text-gray-400 hover:text-white hover:border-white/20',
          ]"
        >
          <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
            <path v-if="copied" stroke-linecap="round" stroke-linejoin="round" d="m4.5 12.75 6 6 9-13.5"/>
            <path v-else stroke-linecap="round" stroke-linejoin="round"
              d="M15.666 3.888A2.25 2.25 0 0 0 13.5 2.25h-3c-1.03 0-1.9.693-2.166
                 1.638m7.332 0c.055.194.084.4.084.612v0a.75.75 0 0 1-.75.75H9a.75.75
                 0 0 1-.75-.75v0c0-.212.03-.418.084-.612m7.332 0c.646.049 1.288.11
                 1.927.184 1.1.128 1.907 1.077 1.907 2.185V19.5a2.25 2.25 0 0
                 1-2.25 2.25H6.75A2.25 2.25 0 0 1 4.5 19.5V6.257c0-1.108.806-2.057
                 1.907-2.185a48.208 48.208 0 0 1 1.927-.184"/>
          </svg>
          {{ copied ? "Copied!" : "Copy" }}
        </button>

        <!-- Download Markdown -->
        <button @click="downloadMarkdown" class="btn-amber flex items-center gap-2 px-4 py-2 text-sm">
          <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round"
              d="M3 16.5v2.25A2.25 2.25 0 0 0 5.25 21h13.5A2.25 2.25 0 0
                 0 21 18.75V16.5M16.5 12 12 16.5m0 0L7.5 12m4.5 4.5V3"/>
          </svg>
          Markdown
        </button>

        <!-- Export PDF -->
        <button
          @click="exportPDF"
          class="flex items-center gap-2 px-4 py-2 rounded-xl text-sm font-semibold
                 border glass border-white/10 text-gray-400 hover:text-white
                 hover:border-white/20 transition-all duration-300"
        >
          <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round"
              d="M19.5 14.25v-2.625a3.375 3.375 0 0 0-3.375-3.375h-1.5A1.125 1.125
                 0 0 1 13.5 7.125v-1.5a3.375 3.375 0 0 0-3.375-3.375H8.25m0
                 12.75h7.5m-7.5 3H12M10.5 2.25H5.625c-.621 0-1.125.504-1.125
                 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0
                 1.125-.504 1.125-1.125V11.25a9 9 0 0 0-9-9Z"/>
          </svg>
          PDF
        </button>

      </div>
    </div>

    <!-- ── Report prose ── -->
    <div class="glass rounded-2xl border border-white/8 p-8 md:p-12 shadow-2xl report-prose-card">
      <div
        class="prose prose-invert prose-lg prose-research max-w-none"
        v-html="renderedReport"
      ></div>
    </div>

  </div>
</template>

<script setup>
import MarkdownIt from "markdown-it";
import { computed, ref } from "vue";
import { useResearchStore } from "../stores/research";
import { slugify } from "../utils/slug";

const store  = useResearchStore();
const copied = ref(false);

// ── Markdown-it with heading IDs (needed for TOC anchor scroll) ──────────
const md = new MarkdownIt({ html: true, linkify: true, typographer: true });

md.renderer.rules.heading_open = (tokens, idx, options, _env, self) => {
  const token      = tokens[idx];
  const inlineToken = tokens[idx + 1];
  const text = inlineToken?.children?.map((t) => t.content).join("") ?? "";
  token.attrSet("id", slugify(text));
  return self.renderToken(tokens, idx, options);
};

const renderedReport = computed(() => md.render(store.report || ""));

// ── Word count & read time ────────────────────────────────────────────────
const wordCount = computed(() => {
  if (!store.report) return 0;
  return store.report
    .replace(/```[\s\S]*?```/g, "")   // strip code blocks
    .replace(/[#*`>\[\]()_\-~]/g, "") // strip markdown symbols
    .split(/\s+/)
    .filter(Boolean).length;
});

const readTime = computed(() => {
  const mins = Math.ceil(wordCount.value / 200);
  return `~${mins} min`;
});

// ── Meta chips ────────────────────────────────────────────────────────────
const metaItems = computed(() => [
  { label: "Topic",     value: store.topic || "—" },
  {
    label: "Sources",
    value: store.citations.length > 0 ? `${store.citations.length} sources` : "—",
  },
  { label: "Time",      value: store.elapsedSeconds ? `${store.elapsedSeconds}s` : "—" },
  {
    label: "Date",
    value: store.generatedAt
      ? new Date(store.generatedAt).toLocaleDateString("en-GB", {
          day: "numeric", month: "short", year: "numeric",
        })
      : "—",
  },
  {
    label: "Words",
    value: wordCount.value > 0 ? wordCount.value.toLocaleString() : "—",
  },
  { label: "Read time", value: wordCount.value > 0 ? readTime.value : "—" },
]);

// ── Actions ───────────────────────────────────────────────────────────────
const copyReport = async () => {
  try {
    await navigator.clipboard.writeText(store.report);
    copied.value = true;
    setTimeout(() => (copied.value = false), 2500);
  } catch {
    console.error("Clipboard error");
  }
};

const downloadMarkdown = () => {
  const slug = (store.topic || "report").replace(/\s+/g, "-").toLowerCase();
  const blob = new Blob([store.report], { type: "text/markdown;charset=utf-8" });
  const url  = URL.createObjectURL(blob);
  const a    = document.createElement("a");
  a.href = url; a.download = `${slug}.md`; a.click();
  URL.revokeObjectURL(url);
};

const exportPDF = () => window.print();
</script>