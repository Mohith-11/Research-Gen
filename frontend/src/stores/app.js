import { defineStore } from "pinia";

export const useAppStore = defineStore("app", {
  state: () => ({
    theme: localStorage.getItem("rg_theme") || "dark",
  }),

  actions: {
    /** Call once in main.js to restore persisted theme on page load. */
    init() {
      this._apply(this.theme);
    },

    toggleTheme() {
      this.theme = this.theme === "dark" ? "light" : "dark";
      localStorage.setItem("rg_theme", this.theme);
      this._apply(this.theme);
    },

    _apply(theme) {
      if (theme === "light") {
        document.documentElement.setAttribute("data-theme", "light");
      } else {
        document.documentElement.removeAttribute("data-theme");
      }
    },
  },
});
