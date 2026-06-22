<template>
  <main class="min-h-[calc(100vh-4rem)]">

    <!-- ─── Loading ─── -->
    <ProgressTimeline v-if="store.loading" />

    <!-- ─── Results ─── -->
    <div v-else-if="store.report" class="animate-fade-up">
      <div class="max-w-screen-xl mx-auto px-4 sm:px-6 py-8">

        <!-- Two-column: sticky sidebar left, report right -->
        <div class="flex flex-col lg:flex-row gap-6 items-start">

          <!-- ─── Sidebar ─── -->
          <aside class="w-full lg:w-72 xl:w-80 shrink-0
                        lg:sticky lg:top-20 lg:max-h-[calc(100vh-6rem)] lg:overflow-y-auto
                        flex flex-col gap-4">

            <!-- Research Plan (collapsible) -->
            <ResearchPlan />

            <!-- Citations -->
            <div class="glass rounded-2xl border border-white/8 p-5">
              <CitationList />
            </div>

            <!-- Table of Contents -->
            <div v-if="store.report" class="glass rounded-2xl border border-white/8 p-5">
              <TableOfContents />
            </div>

          </aside>

          <!-- ─── Main Report ─── -->
          <section class="flex-1 min-w-0">
            <ReportViewer />
          </section>

        </div>
      </div>
    </div>

    <!-- ─── Empty guard ─── -->
    <div
      v-else
      class="flex flex-col items-center justify-center min-h-[80vh]
             text-center px-6 animate-fade-up"
    >
      <div class="w-20 h-20 rounded-3xl glass-amber flex items-center
                  justify-center text-4xl mb-6">
        🔬
      </div>
      <h2 class="text-2xl font-semibold mb-2"
          style="font-family:'Fraunces',serif; color: var(--text)">
        No report yet
      </h2>
      <p class="mb-8 max-w-xs leading-relaxed text-sm" style="color: var(--muted)">
        Head back to the home page and enter a research topic to get started.
      </p>
      <RouterLink
        to="/"
        class="btn-amber px-6 py-3 text-sm flex items-center gap-2 no-underline"
      >
        <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24"
             stroke="currentColor" stroke-width="2.5">
          <path stroke-linecap="round" stroke-linejoin="round"
                d="M10.5 19.5 3 12m0 0 7.5-7.5M3 12h18"/>
        </svg>
        Back to Home
      </RouterLink>
    </div>

  </main>
</template>

<script setup>
import { useResearchStore } from "../stores/research";
import ProgressTimeline  from "../components/ProgressTimeline.vue";
import ReportViewer      from "../components/ReportViewer.vue";
import CitationList      from "../components/CitationList.vue";
import ResearchPlan      from "../components/ResearchPlan.vue";
import TableOfContents   from "../components/TableOfContents.vue";

const store = useResearchStore();
</script>
