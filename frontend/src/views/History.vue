<template>
  <main class="min-h-[calc(100vh-4rem)]">
    <div class="max-w-screen-md mx-auto px-4 sm:px-6 py-10">

      <!-- ── Page header ── -->
      <div class="animate-fade-up flex items-start justify-between gap-4 mb-8">
        <div>
          <h1 class="text-2xl font-semibold" style="font-family:'Fraunces',serif; color: var(--text)">
            📚 Research History
          </h1>
          <p class="text-sm font-mono mt-1" style="color: var(--dim)">
            {{ store.history.length }} saved
            {{ store.history.length === 1 ? "report" : "reports" }}
          </p>
        </div>

        <button
          v-if="store.history.length"
          @click="confirmClear"
          class="text-xs font-mono px-3 py-1.5 rounded-lg border transition-all duration-200 shrink-0 mt-1"
          style="color: var(--dim); border-color: rgba(255,255,255,0.10)"
          @mouseover="e => e.currentTarget.style.borderColor='rgba(239,68,68,0.4)'"
          @mouseleave="e => e.currentTarget.style.borderColor='rgba(255,255,255,0.10)'"
        >
          Clear All
        </button>
      </div>

      <!-- ── History list ── -->
      <div v-if="store.history.length" class="flex flex-col gap-3 animate-scale-in delay-100">
        <HistoryCard
          v-for="entry in store.history"
          :key="entry.id"
          :entry="entry"
        />
      </div>

      <!-- ── Empty state ── -->
      <div
        v-else
        class="animate-fade-up flex flex-col items-center justify-center text-center
               min-h-[60vh] gap-6"
      >
        <div class="glass-amber w-20 h-20 rounded-3xl flex items-center justify-center text-4xl">
          📭
        </div>
        <div>
          <h2 class="text-xl font-semibold mb-2"
              style="font-family:'Fraunces',serif; color: var(--text)">
            No history yet
          </h2>
          <p class="text-sm max-w-xs leading-relaxed" style="color: var(--muted)">
            Reports you generate will appear here so you can revisit them any time.
          </p>
        </div>
        <RouterLink
          to="/"
          class="btn-amber px-5 py-2.5 text-sm flex items-center gap-2 no-underline"
        >
          <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24"
               stroke="currentColor" stroke-width="2.5">
            <path stroke-linecap="round" stroke-linejoin="round"
                  d="M13.5 4.5 21 12m0 0-7.5 7.5M21 12H3"/>
          </svg>
          Start Researching
        </RouterLink>
      </div>

      <!-- ── Confirm clear overlay ── -->
      <Transition name="fade">
        <div
          v-if="showConfirm"
          class="fixed inset-0 z-50 flex items-center justify-center px-4"
          style="background: rgba(0,0,0,0.6); backdrop-filter: blur(4px)"
          @click.self="showConfirm = false"
        >
          <div class="glass rounded-2xl border border-white/10 p-6 max-w-sm w-full
                      animate-scale-in text-center">
            <p class="text-base font-semibold mb-2" style="color: var(--text)">
              Clear all history?
            </p>
            <p class="text-sm mb-6" style="color: var(--muted)">
              This will permanently delete all {{ store.history.length }} saved reports.
            </p>
            <div class="flex gap-3 justify-center">
              <button
                @click="showConfirm = false"
                class="px-4 py-2 text-sm rounded-xl border transition-all duration-200"
                style="border-color: rgba(255,255,255,0.12); color: var(--muted)"
              >
                Cancel
              </button>
              <button
                @click="doClear"
                class="px-4 py-2 text-sm rounded-xl font-semibold
                       bg-red-500/20 border border-red-400/40 text-red-300
                       hover:bg-red-500/30 transition-all duration-200"
              >
                Yes, clear all
              </button>
            </div>
          </div>
        </div>
      </Transition>

    </div>
  </main>
</template>

<script setup>
import { ref } from "vue";
import { useResearchStore } from "../stores/research";
import HistoryCard from "../components/HistoryCard.vue";

const store       = useResearchStore();
const showConfirm = ref(false);

const confirmClear = () => (showConfirm.value = true);
const doClear      = () => { store.clearHistory(); showConfirm.value = false; };
</script>

<style scoped>
.fade-enter-active, .fade-leave-active { transition: opacity 0.2s ease; }
.fade-enter-from, .fade-leave-to       { opacity: 0; }
</style>
