<template>
  <div v-if="headings.length" class="flex flex-col gap-1">
    <!-- Header -->
    <p class="text-[10px] font-mono uppercase tracking-widest mb-2"
       style="color: var(--dim)">
      Table of Contents
    </p>

    <!-- TOC items -->
    <button
      v-for="h in headings"
      :key="h.id"
      @click="scrollTo(h.id)"
      :class="[
        'toc-item text-left w-full rounded-r-md transition-all duration-200 border-l-2 text-[12px] leading-snug',
        h.level === 3 ? 'pl-5 py-1' : 'pl-3 py-1.5',
        activeId === h.id
          ? 'border-amber-400/80 bg-amber-400/[0.06] font-medium'
          : 'border-transparent hover:border-white/15 hover:bg-white/[0.04]',
      ]"
      :style="activeId === h.id ? 'color: var(--text)' : 'color: var(--muted)'"
    >
      <span v-if="h.level === 3" class="mr-1 opacity-50">–</span>
      <span v-else class="mr-1 opacity-40">•</span>
      {{ h.text }}
    </button>
  </div>
</template>

<script setup>
import { ref, computed, watch, onUnmounted, nextTick } from "vue";
import { useResearchStore } from "../stores/research";
import { slugify } from "../utils/slug";

const store    = useResearchStore();
const activeId = ref("");

// ── Parse ## / ### headings from raw markdown ──────────────────────────────
const headings = computed(() => {
  if (!store.report) return [];
  return store.report
    .split("\n")
    .reduce((acc, line) => {
      const m2 = line.match(/^## (.+)/);
      const m3 = line.match(/^### (.+)/);
      if (m2) acc.push({ level: 2, text: m2[1].trim(), id: slugify(m2[1].trim()) });
      else if (m3) acc.push({ level: 3, text: m3[1].trim(), id: slugify(m3[1].trim()) });
      return acc;
    }, []);
});

// ── IntersectionObserver: track which heading is on screen ─────────────────
let observer = null;

function setupObserver() {
  if (observer) observer.disconnect();

  observer = new IntersectionObserver(
    (entries) => {
      // Pick the first heading that just entered the viewport
      const visible = entries
        .filter((e) => e.isIntersecting)
        .sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);
      if (visible.length) activeId.value = visible[0].target.id;
    },
    {
      // Fire when heading crosses the 20% mark from the top
      rootMargin: "-64px 0px -75% 0px",
      threshold: 0,
    }
  );

  const els = document.querySelectorAll(".prose-research h2, .prose-research h3");
  els.forEach((el) => observer.observe(el));
}

watch(
  () => store.report,
  async (val) => {
    if (val) {
      await nextTick();
      // Small delay to ensure markdown v-html has painted
      setTimeout(setupObserver, 150);
    }
  },
  { immediate: true }
);

onUnmounted(() => {
  if (observer) observer.disconnect();
});

// ── Smooth scroll ──────────────────────────────────────────────────────────
function scrollTo(id) {
  const el = document.getElementById(id);
  if (!el) return;
  const top = el.getBoundingClientRect().top + window.scrollY - 88; // navbar + margin
  window.scrollTo({ top, behavior: "smooth" });
  activeId.value = id;
}
</script>
