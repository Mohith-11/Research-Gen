import { createRouter, createWebHistory } from "vue-router";
import Home    from "../views/Home.vue";
import Results from "../views/Results.vue";
import History from "../views/History.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/research",
    name: "Results",
    component: Results,
  },
  {
    path: "/history",
    name: "History",
    component: History,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior() {
    return { top: 0, left: 0, behavior: "smooth" };
  },
});

export default router;
