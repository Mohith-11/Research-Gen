<template>
  <div v-if="store.research_plan" class="glass rounded-2xl border border-white/8 overflow-hidden">

    <!-- ── Header (always visible, clickable) ── -->
    <button
      @click="open = !open"
      class="w-full flex items-center justify-between gap-3 px-4 py-3
             hover:bg-white/[0.04] transition-colors duration-200"
    >
      <div class="flex items-center gap-2 min-w-0">
        <span class="text-base shrink-0">📋</span>
        <span class="text-[10px] font-mono uppercase tracking-widest"
              style="color: var(--dim)">
          Research Plan
        </span>
      </div>

      <!-- Chevron -->
      <svg
        :class="['w-3.5 h-3.5 shrink-0 transition-transform duration-300', open ? 'rotate-180' : '']"
        style="color: var(--dim)"
        fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"
      >
        <path stroke-linecap="round" stroke-linejoin="round" d="m6 9 6 6 6-6"/>
      </svg>
    </button>

    <!-- ── Collapsible body ── -->
    <div
      class="plan-body overflow-hidden transition-all duration-300 ease-in-out"
      :style="{ maxHeight: open ? '240px' : '0px' }"
    >
      <div class="border-t border-white/5 px-4 py-3 overflow-y-auto max-h-60
                  text-[13px] leading-relaxed whitespace-pre-wrap"
           style="color: var(--muted)">
        {{ store.research_plan }}
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref } from "vue";
import { useResearchStore } from "../stores/research";

const store = useResearchStore();
const open  = ref(false);
</script>
