<template>
  <div v-if="store.citations.length">
    <p class="text-[10px] font-mono uppercase tracking-widest text-gray-600 mb-4">
      {{ store.citations.length }} Sources
    </p>

    <div class="flex flex-col gap-2">
      <a
        v-for="(citation, i) in store.citations"
        :key="citation.url"
        :href="citation.url"
        target="_blank"
        rel="noopener noreferrer"
        class="group flex items-start gap-3 p-3 rounded-xl glass border border-white/5
               hover:border-amber-400/30 hover:bg-amber-400/[0.04]
               transition-all duration-200 no-underline"
      >
        <!-- Number -->
        <span class="w-5 h-5 rounded-md bg-amber-400/10 text-amber-400 text-[10px] font-mono font-bold
                     flex items-center justify-center shrink-0 mt-0.5">
          {{ i + 1 }}
        </span>

        <div class="flex-1 min-w-0">
          <!-- Domain row -->
          <div class="flex items-center gap-1.5 mb-1">
            <img
              :src="`https://www.google.com/s2/favicons?sz=16&domain=${getDomain(citation.url)}`"
              class="w-3.5 h-3.5 rounded shrink-0"
              loading="lazy"
              alt=""
            />
            <span class="text-[10px] font-mono text-gray-600 truncate">{{ getDomain(citation.url) }}</span>
            <span class="ml-auto text-gray-700 group-hover:text-amber-400 transition-colors text-xs shrink-0">→</span>
          </div>
          <!-- Title -->
          <p class="text-xs font-medium text-gray-400 group-hover:text-gray-200 leading-snug line-clamp-2 transition-colors duration-200">
            {{ citation.title || citation.url }}
          </p>
        </div>
      </a>
    </div>
  </div>
</template>

<script setup>
import { useResearchStore } from "../stores/research";

const store = useResearchStore();

const getDomain = (url) => {
  try { return new URL(url).hostname.replace("www.", ""); }
  catch { return url; }
};
</script>
