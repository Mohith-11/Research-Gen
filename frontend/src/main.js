import { createApp } from "vue";
import { createPinia } from "pinia";

import App    from "./App.vue";
import router from "./router/index.js";

import "./assets/styles/main.css";

const app   = createApp(App);
const pinia = createPinia();

app.use(pinia);
app.use(router);

// Give the research store access to the router for programmatic navigation
import { useResearchStore } from "./stores/research.js";
const store = useResearchStore();
store.setRouter(router);

// Apply persisted theme before first paint
import { useAppStore } from "./stores/app.js";
const appStore = useAppStore();
appStore.init();

app.mount("#app");