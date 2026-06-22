<div align="center">

<h1>🔬 ResearchGen AI</h1>

<p><strong>Autonomous multi-agent research reports, written while you wait.</strong></p>

<p>
  <img src="https://img.shields.io/badge/Vue-3-42b883?style=flat-square&logo=vue.js&logoColor=white" alt="Vue 3"/>
  <img src="https://img.shields.io/badge/FastAPI-0.100+-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/LangGraph-0.2+-1a1a2e?style=flat-square" alt="LangGraph"/>
  <img src="https://img.shields.io/badge/Groq-LLaMA_3-f55036?style=flat-square" alt="Groq"/>
  <img src="https://img.shields.io/badge/Tailwind_CSS-4-38bdf8?style=flat-square&logo=tailwindcss&logoColor=white" alt="Tailwind"/>
  <img src="https://img.shields.io/badge/license-MIT-blue?style=flat-square" alt="MIT"/>
</p>

</div>

---

ResearchGen AI is a full-stack web application that generates **publication-quality research reports** from a single topic prompt. A LangGraph multi-agent pipeline autonomously plans, searches the web, reads sources, synthesises findings, compiles citations, and writes the final report — all in under two minutes.

## ✨ Features

| Feature | Description |
|---|---|
| 🤖 **Autonomous pipeline** | 6-agent LangGraph graph: Planner → Search → Reader → Summarizer → Citation → Writer |
| 📄 **Markdown reports** | Structured, prose-quality output with headings, citations, and code blocks |
| 🔗 **Auto-citations** | Sources fetched and linked automatically via Tavily search |
| 📚 **Research History** | Every report auto-saved to localStorage; browse, reload, or delete past reports |
| 📑 **Table of Contents** | Auto-generated from report headings; highlights active section as you scroll |
| 🔢 **Word count & read time** | Shown in the report metadata bar alongside topic, sources, and date |
| 📄 **PDF Export** | One-click print-to-PDF with a clean, styled print stylesheet |
| 🌙 **Dark / Light mode** | Toggle persisted to `localStorage`; smooth CSS variable transitions |
| 📋 **Research Plan Viewer** | Collapsible card showing the AI-generated research plan used for each report |
| ⬇️ **Markdown download** | Export any report as a `.md` file |

---

## 🏗️ Architecture

```
researchgen-ai/
├── backend/                  # FastAPI + LangGraph
│   ├── agents/               # 6 LangGraph agent nodes
│   │   ├── planner.py        # Breaks topic into structured research plan
│   │   ├── search.py         # Web search via Tavily
│   │   ├── reader.py         # Reads & extracts content from URLs
│   │   ├── summarizer.py     # Synthesises findings across sources
│   │   ├── citation.py       # Compiles & validates references
│   │   └── report.py         # Writes the final markdown report
│   ├── graph/
│   │   ├── state.py          # LangGraph state schema
│   │   └── workflow.py       # Graph definition & compilation
│   ├── api/routes.py         # POST /research endpoint
│   ├── models/               # Pydantic request / response models
│   └── main.py               # FastAPI app with CORS
│
└── frontend/                 # Vue 3 + Vite + Tailwind CSS 4
    └── src/
        ├── stores/
        │   ├── research.js   # Report state + history management
        │   └── app.js        # Theme (dark/light) state
        ├── components/
        │   ├── Navbar.vue
        │   ├── Hero.vue
        │   ├── SearchBox.vue
        │   ├── ProgressTimeline.vue
        │   ├── ReportViewer.vue
        │   ├── CitationList.vue
        │   ├── ResearchPlan.vue   # ← collapsible plan viewer
        │   ├── TableOfContents.vue # ← TOC w/ IntersectionObserver
        │   ├── HistoryCard.vue    # ← history entry card
        │   └── ThemeToggle.vue   # ← dark/light toggle
        ├── views/
        │   ├── Home.vue
        │   ├── Results.vue
        │   └── History.vue       # ← /history page
        └── utils/slug.js         # heading → anchor ID utility
```

---

## 🤖 Agent Pipeline

```
User Prompt
    │
    ▼
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Planner   │───▶│   Search    │───▶│   Reader    │
│  (Groq LLM) │    │  (Tavily)   │    │  (Groq LLM) │
└─────────────┘    └─────────────┘    └─────────────┘
                                              │
                                              ▼
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Report    │◀───│  Citation   │◀───│ Summarizer  │
│  (OpenRtr.) │    │  (Groq LLM) │    │  (Groq LLM) │
└─────────────┘    └─────────────┘    └─────────────┘
    │
    ▼
Markdown Report + Citations JSON
```

| Agent | Model | Task |
|---|---|---|
| Planner | Groq (LLaMA 3) | Creates a structured research plan |
| Search | Tavily API | Finds authoritative web sources |
| Reader | Groq (LLaMA 3) | Extracts key content from each URL |
| Summarizer | Groq (LLaMA 3) | Synthesises findings across all sources |
| Citation | Groq (LLaMA 3) | Validates and formats references |
| Report | OpenRouter | Writes the final long-form report |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Node.js 18+
- API keys for: **Groq**, **Tavily**, **OpenRouter**, **Google** (optional)

### 1. Clone the repo

```bash
git clone https://github.com/Mohith-11/Research-Gen.git
cd Research-Gen
```

### 2. Backend setup

```bash
cd backend

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Edit .env and fill in your API keys (see below)

# Start the API server
uvicorn main:app --reload
```

The backend will be available at `http://localhost:8000`.  
Interactive API docs: `http://localhost:8000/docs`

### 3. Frontend setup

```bash
cd frontend

# Install dependencies
npm install

# Start the dev server
npm run dev
```

The app will be available at `http://localhost:5173`.

---

## 🔑 Environment Variables

Create `backend/.env` with the following keys:

```env
# Required — LLM for all agent nodes
GROQ_API_KEY=gsk_...

# Required — web search for the Search agent
TAVILY_API_KEY=tvly-...

# Required — final report writing (via OpenRouter)
OPENROUTER_API_KEY=sk-or-v1-...

# Optional — additional provider
GOOGLE_API_KEY=AIza...
```

> **⚠️ Never commit your `.env` file.** It is already listed in `.gitignore`.

---

## 📡 API Reference

### `POST /research`

Generate a research report for a given topic.

**Request body:**
```json
{ "topic": "Quantum Computing in Drug Discovery" }
```

**Response:**
```json
{
  "topic": "Quantum Computing in Drug Discovery",
  "research_plan": "1. Introduction to quantum computing...",
  "report": "# Quantum Computing in Drug Discovery\n\n...",
  "citations": [
    { "url": "https://example.com/paper", "title": "Quantum algorithms..." }
  ]
}
```

---

## 🛠️ Tech Stack

### Backend
| Library | Role |
|---|---|
| **FastAPI** | REST API framework |
| **LangGraph** | Multi-agent orchestration graph |
| **Groq** | LLM inference (LLaMA 3, ultra-fast) |
| **OpenRouter** | LLM routing for report generation |
| **Tavily** | Web search API |
| **Pydantic** | Request/response validation |

### Frontend
| Library | Role |
|---|---|
| **Vue 3** | Reactive component framework |
| **Vite 8** | Build tool & dev server |
| **Pinia** | State management (research + theme) |
| **Vue Router 5** | Client-side routing |
| **Tailwind CSS 4** | Utility-first styling |
| **markdown-it** | Markdown → HTML rendering |
| **@fontsource** | Inter, Fraunces, JetBrains Mono |

---

## 🎨 UI Highlights

- **Dark / Light mode** — toggle persisted to `localStorage`
- **Glassmorphism** — frosted glass cards throughout (`backdrop-filter: blur(20px)`)
- **Animated progress timeline** — live step tracker while agents run (20–120s)
- **Sticky sidebar** — Research Plan, Citations, and Table of Contents
- **Scroll-aware TOC** — `IntersectionObserver` highlights current section
- **PDF export** — browser-native `window.print()` with clean print stylesheet
- **Research history** — auto-saved to `localStorage`, up to 20 reports

---

## 📁 Folder Structure

```
researchgen-ai/
├── backend/
│   ├── agents/
│   ├── api/
│   ├── graph/
│   ├── models/
│   ├── prompts/
│   ├── providers/
│   ├── tools/
│   ├── main.py
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── assets/styles/main.css
│   │   ├── components/
│   │   ├── router/
│   │   ├── stores/
│   │   ├── utils/
│   │   └── views/
│   ├── index.html
│   └── package.json
├── docker-compose.yml
└── README.md
```

---

## 🤝 Contributing

1. Fork the repo
2. Create a feature branch: `git checkout -b feat/your-feature`
3. Commit your changes: `git commit -m "feat: add your feature"`
4. Push to the branch: `git push origin feat/your-feature`
5. Open a Pull Request

---

## 📄 License

MIT © [Mohith-11](https://github.com/Mohith-11)
