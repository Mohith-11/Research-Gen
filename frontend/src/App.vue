<template>
  <!-- pt-16 = navbar height offset (64px), applied once here for all pages -->
  <div class="min-h-screen pt-16">
    <Navbar />
    <RouterView />
  </div>
</template>

<script setup>
import Navbar from "./components/Navbar.vue";
</script>