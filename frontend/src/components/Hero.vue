<template>
  <!-- min-h-[calc(100vh-4rem)] fills visible area below navbar. NO overflow-hidden - it traps scroll -->
  <section class="relative flex flex-col items-center justify-center text-center min-h-[calc(100vh-4rem)] px-6 pb-20">

    <!-- Floating ambient orbs -->
    <div class="pointer-events-none absolute inset-0 overflow-hidden">
      <div
        class="animate-float-orb absolute -top-32 -right-32 w-[600px] h-[600px] rounded-full opacity-30"
        style="background: radial-gradient(circle, rgba(155,140,255,0.18) 0%, transparent 70%)"
      ></div>
      <div
        class="animate-float-orb absolute -bottom-40 -left-40 w-[500px] h-[500px] rounded-full opacity-20"
        style="background: radial-gradient(circle, rgba(77,208,192,0.18) 0%, transparent 70%); animation-delay: -5s"
      ></div>
      <div
        class="absolute top-1/3 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[300px] h-[300px] rounded-full opacity-15"
        style="background: radial-gradient(circle, rgba(242,166,90,0.2) 0%, transparent 70%)"
      ></div>
    </div>

    <!-- Badge -->
    <div class="animate-fade-up relative flex items-center gap-2 glass rounded-full px-4 py-2 mb-8 border border-amber-400/20">
      <span class="relative flex h-1.5 w-1.5">
        <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-teal-400 opacity-75"></span>
        <span class="relative inline-flex rounded-full h-1.5 w-1.5 bg-teal-400"></span>
      </span>
      <span class="text-xs font-mono tracking-widest text-gray-400 uppercase">
        Autonomous Multi-Agent Research
      </span>
    </div>

    <!-- Headline -->
    <h1
      class="animate-fade-up delay-100 relative text-5xl sm:text-6xl md:text-7xl lg:text-8xl font-semibold leading-[1.05] max-w-5xl mb-6"
      style="font-family: 'Fraunces', serif"
    >
      Research,<br />
      <span class="text-shimmer">written while you wait.</span>
    </h1>

    <!-- Subheadline -->
    <p class="animate-fade-up delay-200 relative text-base sm:text-lg text-gray-400 leading-relaxed max-w-2xl mb-12">
      Generate publication-quality research reports using an autonomous AI pipeline powered by
      <span class="text-violet-400 font-medium">LangGraph</span>,
      <span class="text-amber-400 font-medium">Groq</span>, and
      <span class="text-teal-400 font-medium">OpenRouter</span>.
    </p>

    <!-- Search box -->
    <div class="animate-fade-up delay-300 relative w-full max-w-2xl">
      <SearchBox />
    </div>

    <!-- Feature pills -->
    <div class="animate-fade-up delay-500 relative flex flex-wrap justify-center gap-3 mt-10">
      <span v-for="tag in tags" :key="tag.label"
        class="flex items-center gap-1.5 text-xs font-mono text-gray-500 glass rounded-full px-3 py-1.5 border border-white/5"
      >
        <span>{{ tag.icon }}</span>
        <span>{{ tag.label }}</span>
      </span>
    </div>

  </section>
</template>

<script setup>
import SearchBox from "./SearchBox.vue";

const tags = [
  { icon: "🔍", label: "Web Search" },
  { icon: "📄", label: "Source Reading" },
  { icon: "🧠", label: "AI Synthesis" },
  { icon: "🔗", label: "Auto-Citations" },
  { icon: "✍️", label: "Report Writing" },
];
</script>