import { defineStore } from "pinia";
import { markRaw } from "vue";
import api from "../services/api";

let _router = null;

const HISTORY_KEY = "rg_history";
const MAX_HISTORY  = 20;

export const useResearchStore = defineStore("research", {

  state: () => ({
    loading: false,
    topic: "",
    research_plan: "",
    report: "",
    citations: [],
    generatedAt: null,
    elapsedSeconds: null,
    agentStep: -1,

    // ── History (persisted to localStorage) ──────────────────────────────
    history: JSON.parse(localStorage.getItem(HISTORY_KEY) || "[]"),
  }),

  actions: {

    setRouter(router) {
      _router = markRaw(router);
    },

    async generateResearch(topic) {
      this.loading      = true;
      this.agentStep    = 0;
      this.report       = "";
      this.citations    = [];
      this.generatedAt  = null;
      this.elapsedSeconds = null;

      const startTime = Date.now();

      try {
        const response = await api.post("/research", { topic });

        this.topic          = response.data.topic;
        this.research_plan  = response.data.research_plan;
        this.report         = response.data.report;
        this.citations      = response.data.citations;
        this.generatedAt    = new Date().toISOString();
        this.elapsedSeconds = ((Date.now() - startTime) / 1000).toFixed(1);
        this.agentStep      = 6;

        // Auto-save to history after every successful generation
        this._saveToHistory();

        if (_router) _router.push("/research");

      } catch (error) {
        console.error(error);
      } finally {
        this.loading = false;
      }
    },

    // ── History helpers ───────────────────────────────────────────────────

    _saveToHistory() {
      const entry = {
        id:             Date.now(),
        topic:          this.topic,
        research_plan:  this.research_plan,
        report:         this.report,
        citations:      this.citations,
        generatedAt:    this.generatedAt,
        elapsedSeconds: this.elapsedSeconds,
      };
      this.history.unshift(entry);
      if (this.history.length > MAX_HISTORY) {
        this.history = this.history.slice(0, MAX_HISTORY);
      }
      this._persistHistory();
    },

    deleteHistory(id) {
      this.history = this.history.filter((e) => e.id !== id);
      this._persistHistory();
    },

    clearHistory() {
      this.history = [];
      localStorage.removeItem(HISTORY_KEY);
    },

    _persistHistory() {
      localStorage.setItem(HISTORY_KEY, JSON.stringify(this.history));
    },

    /** Load a saved history entry into the active report state. */
    loadFromHistory(entry) {
      this.topic          = entry.topic;
      this.research_plan  = entry.research_plan;
      this.report         = entry.report;
      this.citations      = entry.citations;
      this.generatedAt    = entry.generatedAt;
      this.elapsedSeconds = entry.elapsedSeconds;
      this.agentStep      = 6;
      this.loading        = false;
    },

    reset() {
      this.loading        = false;
      this.topic          = "";
      this.research_plan  = "";
      this.report         = "";
      this.citations      = [];
      this.generatedAt    = null;
      this.elapsedSeconds = null;
      this.agentStep      = -1;
    },
  },
});