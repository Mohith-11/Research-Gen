<template>
  <nav class="fixed top-0 left-0 right-0 z-50">
    <!-- Frosted glass bar -->
    <div class="glass border-b border-white/5 border-t-0 border-l-0 border-r-0 rounded-none">
      <div class="max-w-screen-xl mx-auto px-6 h-16 flex items-center justify-between">

        <!-- Logo -->
        <RouterLink to="/" class="flex items-center gap-2.5 no-underline group">
          <div class="w-8 h-8 rounded-xl glass-amber flex items-center justify-center text-amber-400 font-mono font-bold text-sm group-hover:scale-110 transition-transform duration-200">
            R
          </div>
          <span class="text-white font-semibold text-lg tracking-tight">
            Research<span class="text-amber-400">Gen</span>
          </span>
          <span class="hidden sm:inline-block text-xs font-mono text-gray-600 border border-white/10 rounded-full px-2 py-0.5">
            AI
          </span>
        </RouterLink>

        <!-- Right: status + actions -->
        <div class="flex items-center gap-3">

          <!-- Live indicator when loading -->
          <div v-if="store.loading" class="flex items-center gap-2 text-sm text-amber-400">
            <span class="relative flex h-2 w-2">
              <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-amber-400 opacity-75"></span>
              <span class="relative inline-flex rounded-full h-2 w-2 bg-amber-400"></span>
            </span>
            <span class="font-mono text-xs hidden sm:block">Agents running…</span>
          </div>

          <!-- New Research (results page only) -->
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

const route = useRoute();
const router = useRouter();
const store = useResearchStore();

const newResearch = () => {
  store.reset();
  router.push("/");
};
</script>