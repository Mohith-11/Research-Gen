<template>
  <nav class="fixed top-0 left-0 right-0 z-50 print:hidden">
    <div class="glass border-b border-white/5 border-t-0 border-l-0 border-r-0 rounded-none">
      <div class="max-w-screen-xl mx-auto px-6 h-16 flex items-center justify-between">

        <!-- Logo -->
        <RouterLink to="/" class="flex items-center gap-2.5 no-underline group">
          <div class="w-8 h-8 rounded-xl glass-amber flex items-center justify-center
                      text-amber-400 font-mono font-bold text-sm
                      group-hover:scale-110 transition-transform duration-200">
            R
          </div>
          <span class="font-semibold text-lg tracking-tight" style="color: var(--text)">
            Research<span style="color: var(--amber)">Gen</span>
          </span>
          <span class="hidden sm:inline-block text-xs font-mono border rounded-full px-2 py-0.5"
                style="color: var(--dim); border-color: rgba(255,255,255,0.10)">
            AI
          </span>
        </RouterLink>

        <!-- Right area -->
        <div class="flex items-center gap-2">

          <!-- Live indicator while loading -->
          <div v-if="store.loading" class="flex items-center gap-2 text-sm" style="color: var(--amber)">
            <span class="relative flex h-2 w-2">
              <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-amber-400 opacity-75"></span>
              <span class="relative inline-flex rounded-full h-2 w-2 bg-amber-400"></span>
            </span>
            <span class="font-mono text-xs hidden sm:block">Agents running…</span>
          </div>

          <!-- Theme toggle (always visible) -->
          <ThemeToggle />

          <!-- History link (always visible) -->
          <RouterLink
            to="/history"
            class="hidden sm:flex items-center gap-1.5 text-xs font-mono px-3 py-1.5
                   rounded-lg border no-underline transition-all duration-200"
            style="color: var(--muted); border-color: rgba(255,255,255,0.10)"
            active-class="!border-amber-400/30 !text-amber-400"
          >
            History
            <span
              v-if="store.history.length"
              class="inline-flex items-center justify-center w-4 h-4 rounded-full
                     text-[9px] font-bold"
              style="background: rgba(242,166,90,0.20); color: var(--amber)"
            >
              {{ store.history.length > 9 ? "9+" : store.history.length }}
            </span>
          </RouterLink>

          <!-- New Research button (results page only, not loading) -->
          <button
            v-if="route.path === '/research' && !store.loading"
            @click="newResearch"
            class="btn-amber px-4 py-2 text-sm flex items-center gap-2"
          >
            <span>+</span>
            <span>New Research</span>
          </button>

        </div>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { useRoute, useRouter } from "vue-router";
import { useResearchStore } from "../stores/research";
import ThemeToggle from "./ThemeToggle.vue";

const route  = useRoute();
const router = useRouter();
const store  = useResearchStore();

const newResearch = () => {
  store.reset();
  router.push("/");
};
</script>