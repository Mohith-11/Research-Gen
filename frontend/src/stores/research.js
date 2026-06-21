import { defineStore } from "pinia";
import { markRaw } from "vue";
import api from "../services/api";

let _router = null;

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

    }),

    actions: {

        setRouter(router) {
            _router = markRaw(router);
        },

        async generateResearch(topic) {

            this.loading = true;
            this.agentStep = 0;
            this.report = "";
            this.citations = [];
            this.generatedAt = null;
            this.elapsedSeconds = null;

            const startTime = Date.now();

            try {

                const response = await api.post("/research", { topic });

                this.topic = response.data.topic;
                this.research_plan = response.data.research_plan;
                this.report = response.data.report;
                this.citations = response.data.citations;
                this.generatedAt = new Date().toISOString();
                this.elapsedSeconds = ((Date.now() - startTime) / 1000).toFixed(1);
                this.agentStep = 6;

                if (_router) {
                    _router.push("/research");
                }

            } catch (error) {

                console.error(error);

            } finally {

                this.loading = false;

            }

        },

        reset() {
            this.loading = false;
            this.topic = "";
            this.research_plan = "";
            this.report = "";
            this.citations = [];
            this.generatedAt = null;
            this.elapsedSeconds = null;
            this.agentStep = -1;
        }

    }

});