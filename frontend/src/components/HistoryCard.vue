<template>
  <!-- Entire card is clickable to load the report; delete button stops propagation -->
  <div
    @click="load"
    class="history-card glass rounded-2xl border border-white/8 p-4
           flex items-center gap-4 cursor-pointer select-none
           transition-all duration-200 hover:-translate-y-0.5"
  >
    <!-- Icon -->
    <div class="glass-amber w-11 h-11 rounded-xl flex items-center justify-center
                text-xl shrink-0">
      {{ emoji }}
    </div>

    <!-- Text -->
    <div class="flex-1 min-w-0">
      <p class="text-sm font-semibold truncate" style="color: var(--text)">
        {{ entry.topic }}
      </p>
      <p class="text-[11px] font-mono mt-0.5" style="color: var(--dim)">
        {{ entry.citations?.length ?? 0 }} sources
        · {{ entry.elapsedSeconds }}s
        · {{ formattedDate }}
      </p>
    </div>

    <!-- Delete -->
    <button
      @click.stop="del"
      class="delete-btn w-7 h-7 rounded-lg flex items-center justify-center
             text-sm shrink-0 transition-all duration-200"
      style="color: var(--dim)"
      title="Remove from history"
    >
      ✕
    </button>
  </div>
</template>

<script setup>
import { computed } from "vue";
import { useRouter } from "vue-router";
import { useResearchStore } from "../stores/research";

const props  = defineProps({ entry: { type: Object, required: true } });
const store  = useResearchStore();
const router = useRouter();

// Pick a topic-themed emoji (simple keyword match, fallback 🔬)
const emoji = computed(() => {
  const t = (props.entry.topic || "").toLowerCase();
  if (t.includes("quantum"))      return "⚛️";
  if (t.includes("crispr") || t.includes("gene") || t.includes("dna")) return "🧬";
  if (t.includes("ai") || t.includes("agent") || t.includes("llm"))    return "🤖";
  if (t.includes("climate") || t.includes("carbon"))                   return "🌍";
  if (t.includes("neuro") || t.includes("brain"))                      return "🧠";
  if (t.includes("space") || t.includes("astro"))                      return "🚀";
  if (t.includes("drug") || t.includes("pharma") || t.includes("medicine")) return "💊";
  return "🔬";
});

const formattedDate = computed(() => {
  if (!props.entry.generatedAt) return "—";
  return new Date(props.entry.generatedAt).toLocaleDateString("en-GB", {
    day: "numeric", month: "short", year: "numeric",
  });
});

function load() {
  store.loadFromHistory(props.entry);
  router.push("/research");
}

function del() {
  store.deleteHistory(props.entry.id);
}
</script>

<style scoped>
.history-card {
  border-color: rgba(255, 255, 255, 0.08);
}
.history-card:hover {
  border-color: rgba(242, 166, 90, 0.25);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
}
.delete-btn:hover {
  background: rgba(239, 68, 68, 0.15);
  color: rgb(252, 165, 165) !important;
}
</style>
