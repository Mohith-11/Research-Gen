<template>
  <button
    @click="app.toggleTheme()"
    class="theme-toggle-btn glass flex items-center justify-center w-9 h-9 rounded-xl transition-all duration-300 hover:border-white/20 shrink-0"
    :title="app.theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode'"
  >
    <!-- Sun (shown in dark mode → click to go light) -->
    <svg
      v-if="app.theme === 'dark'"
      class="w-4 h-4 text-amber-400 transition-transform duration-300"
      fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"
    >
      <circle cx="12" cy="12" r="4"/>
      <path stroke-linecap="round" stroke-linejoin="round"
        d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41
           M2 12h2M20 12h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41"/>
    </svg>

    <!-- Moon (shown in light mode → click to go dark) -->
    <svg
      v-else
      class="w-4 h-4 transition-transform duration-300"
      style="color: var(--violet)"
      fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"
    >
      <path stroke-linecap="round" stroke-linejoin="round"
        d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>
    </svg>
  </button>
</template>

<script setup>
import { useAppStore } from "../stores/app";
const app = useAppStore();
</script>

<style scoped>
.theme-toggle-btn {
  border: 1px solid rgba(255, 255, 255, 0.10);
}
.theme-toggle-btn:hover {
  border-color: rgba(255, 255, 255, 0.22);
}
</style>
