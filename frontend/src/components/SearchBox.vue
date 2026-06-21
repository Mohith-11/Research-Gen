<template>
  <div class="w-full">
    <!-- Input row -->
    <div class="glass rounded-2xl p-2 flex items-center gap-2 border border-white/10 focus-within:border-amber-400/40 transition-colors duration-300">
      <div class="flex items-center gap-3 flex-1 px-4">
        <svg class="w-4 h-4 text-gray-500 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
          <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-4.35-4.35m0 0A7.5 7.5 0 1 0 6.5 6.5a7.5 7.5 0 0 0 10.65 10.65z" />
        </svg>
        <input
          v-model="topic"
          @keyup.enter="go"
          type="text"
          placeholder="e.g. Quantum Computing in Drug Discovery"
          class="flex-1 bg-transparent outline-none text-white font-mono text-sm placeholder-gray-600 py-3"
        />
      </div>

      <button
        @click="go"
        :disabled="!topic.trim()"
        class="btn-amber px-6 py-3 text-sm shrink-0 flex items-center gap-2 disabled:opacity-40 disabled:cursor-not-allowed disabled:transform-none disabled:shadow-none"
      >
        <span>Generate</span>
        <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
          <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5 21 12m0 0-7.5 7.5M21 12H3" />
        </svg>
      </button>
    </div>

    <!-- Example topics -->
    <div class="mt-3 flex flex-wrap items-center gap-2">
      <span class="text-xs text-gray-600 font-mono">Try:</span>
      <button
        v-for="ex in examples"
        :key="ex"
        @click="topic = ex"
        class="text-xs text-gray-500 hover:text-amber-400 transition-colors font-mono border border-white/5 hover:border-amber-400/30 rounded-full px-3 py-1 bg-white/[0.02] hover:bg-amber-400/5"
      >
        {{ ex }}
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import { useResearchStore } from "../stores/research";

const topic = ref("");
const store = useResearchStore();
const router = useRouter();

const examples = [
  "Agentic AI",
  "CRISPR Gene Editing",
  "Quantum Supremacy",
];

const go = async () => {
  if (!topic.value.trim()) return;
  router.push("/research");
  store.generateResearch(topic.value.trim());
};
</script>