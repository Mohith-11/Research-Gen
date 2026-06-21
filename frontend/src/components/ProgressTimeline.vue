<template>
  <div class="flex flex-col items-center justify-center min-h-screen px-6 py-20">

    <!-- Header -->
    <div class="text-center mb-16 animate-fade-up">
      <p class="text-xs font-mono text-amber-400/70 uppercase tracking-widest mb-3">
        AI Agents Working
      </p>
      <h2 class="text-3xl sm:text-4xl font-semibold text-white mb-2" style="font-family:'Fraunces',serif">
        Generating your research
      </h2>
      <p class="text-gray-500 text-sm max-w-xs mx-auto leading-relaxed">
        Our autonomous agents are browsing, reading, and writing — this takes 20–120 seconds.
      </p>
    </div>

    <!-- Timeline -->
    <div class="w-full max-w-sm animate-scale-in delay-200">
      <div
        v-for="(step, i) in steps"
        :key="step.label"
        class="flex items-start gap-4"
      >
        <!-- Icon + connector column -->
        <div class="flex flex-col items-center">
          <!-- Step bubble -->
          <div
            :class="[
              'w-11 h-11 rounded-2xl flex items-center justify-center text-base shrink-0 transition-all duration-500',
              currentStep > i
                ? 'bg-gradient-to-br from-amber-400 to-amber-600 shadow-lg shadow-amber-400/30 scale-100'
                : currentStep === i
                ? 'glass border-2 border-amber-400/60 text-amber-400'
                : 'glass border border-white/8 text-gray-700'
            ]"
            :style="currentStep === i ? 'animation: pulse-ring 1.5s ease-out infinite' : ''"
          >
            <span v-if="currentStep > i" class="text-black font-bold text-sm">✓</span>
            <span v-else>{{ step.icon }}</span>
          </div>

          <!-- Connector line -->
          <div
            v-if="i < steps.length - 1"
            :class="[
              'w-px h-8 my-1 transition-all duration-700',
              currentStep > i
                ? 'bg-gradient-to-b from-amber-400/60 to-amber-400/20'
                : 'bg-white/5'
            ]"
          ></div>
        </div>

        <!-- Text -->
        <div class="pt-2 pb-7">
          <p
            :class="[
              'text-sm font-semibold leading-tight transition-all duration-300',
              currentStep > i ? 'text-amber-400' : currentStep === i ? 'text-white' : 'text-gray-700'
            ]"
          >
            {{ step.label }}
          </p>
          <p
            :class="[
              'text-xs mt-1 leading-relaxed transition-all duration-300',
              currentStep >= i ? 'text-gray-500' : 'text-gray-800'
            ]"
          >
            {{ step.description }}
          </p>
          <!-- Active indicator bar -->
          <div
            v-if="currentStep === i"
            class="mt-2 h-0.5 w-16 rounded-full bg-gradient-to-r from-amber-400 to-amber-400/0"
            style="animation: shimmer 1.5s ease infinite"
          ></div>
        </div>
      </div>
    </div>

    <!-- Elapsed timer -->
    <p class="mt-4 text-gray-700 text-xs font-mono animate-fade-up delay-500">
      {{ elapsedDisplay }}
    </p>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted, watch } from "vue";
import { useResearchStore } from "../stores/research";

const store = useResearchStore();

const steps = [
  { icon: "🔍", label: "Planner Agent",    description: "Breaking the topic into a structured research plan" },
  { icon: "🌐", label: "Search Agent",     description: "Searching the web for authoritative sources" },
  { icon: "📄", label: "Reader Agent",     description: "Reading and extracting content from each source" },
  { icon: "🧠", label: "Summarizer",       description: "Synthesizing information across all sources" },
  { icon: "🔗", label: "Citation Builder", description: "Compiling and validating all references" },
  { icon: "✍️", label: "Report Writer",    description: "Composing the final structured report" },
];

const currentStep = ref(0);
const elapsed = ref(0);
let stepInterval = null;
let timerInterval = null;

const elapsedDisplay = computed(() => {
  const m = Math.floor(elapsed.value / 60);
  const s = elapsed.value % 60;
  return m > 0 ? `${m}m ${s}s elapsed` : `${s}s elapsed`;
});

const start = () => {
  currentStep.value = 0;
  elapsed.value = 0;

  stepInterval = setInterval(() => {
    if (currentStep.value < steps.length - 1) currentStep.value++;
  }, 1800);

  timerInterval = setInterval(() => {
    elapsed.value++;
  }, 1000);
};

const stop = () => {
  clearInterval(stepInterval);
  clearInterval(timerInterval);
  stepInterval = null;
  timerInterval = null;
  currentStep.value = steps.length;
};

watch(() => store.loading, (loading) => {
  if (loading) start();
  else stop();
}, { immediate: true });

onUnmounted(() => stop());
</script>
