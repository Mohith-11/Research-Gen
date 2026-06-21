import { createApp } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";
import router from "./router/index.js";

import "./assets/styles/main.css";

const app = createApp(App);
const pinia = createPinia();

app.use(pinia);
app.use(router);

// Give the store access to the router for programmatic navigation after generation
import { useResearchStore } from "./stores/research.js";
const store = useResearchStore();
store.setRouter(router);

app.mount("#app");