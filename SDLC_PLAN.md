# Agentic AI SDLC Plan — Vignesh Personal Portfolio Web Application

> **Author:** Vignesh | **Date:** November 2026  
> **Stack:** Python · Streamlit · IBM Granite (via IBM watsonx.ai) · ibm-watson-machine-learning

---

## 1. PROJECT OVERVIEW

Vignesh is a technical trainer and subject-matter expert specialising in **Agentic AI**, **Machine Learning**, and **Quantum Computing**. This project delivers a professional, AI-powered personal portfolio web application that:

- Showcases his profile, skills, courses delivered, and notable projects.
- Embeds an **Agentic AI assistant** powered by the **IBM Granite** language model to answer visitors' common queries (about Vignesh, his training offerings, and the technology domains he covers).
- Follows every phase of the **Agentic AI Software Development Life Cycle (SDLC)**.

---

## 2. AGENTIC AI SDLC PHASES

### Phase 1 — Requirements Engineering & Goal Definition

| Artefact | Detail |
|---|---|
| **Primary goal** | Personal portfolio + AI-powered visitor Q&A agent |
| **Agent task** | Answer natural-language questions about Vignesh, his expertise, and training programmes |
| **Model** | IBM Granite 3.x (ibm/granite-3-8b-instruct) via watsonx.ai |
| **Agent pattern** | ReAct-style single-turn agent with tool use (contact lookup, course catalogue) |
| **Success metric** | Agent answers queries accurately within 3 s with < 5 % hallucination rate |

**User stories:**
1. As a visitor, I can browse Vignesh's profile, skills, courses, and projects.
2. As a visitor, I can ask the AI assistant questions in plain English and receive accurate answers.
3. As Vignesh, I can update course/project data via config files without touching code.

---

### Phase 2 — System Design & Architecture

```
┌─────────────────────────────────────────────────────────┐
│                  Streamlit Frontend                     │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐  │
│  │  Home/   │ │  Skills  │ │ Courses/ │ │ Contact  │  │
│  │  About   │ │  Matrix  │ │ Projects │ │   Form   │  │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘  │
│                    ┌──────────────────┐                 │
│                    │  AI Chat Widget  │                 │
│                    └────────┬─────────┘                 │
└─────────────────────────────┼───────────────────────────┘
                              │ HTTPS / REST
                ┌─────────────▼──────────────┐
                │   IBM watsonx.ai API        │
                │   Model: granite-3-8b-      │
                │   instruct                  │
                │   (ibm-granite/granite-3-   │
                │    8b-instruct)             │
                └─────────────────────────────┘
```

**Component map:**

| File | Responsibility |
|---|---|
| `app.py` | Streamlit entry point, sidebar navigation |
| `pages/home.py` | Hero banner, about section |
| `pages/skills.py` | Skills matrix, radar chart |
| `pages/courses.py` | Courses delivered, testimonials |
| `pages/projects.py` | Project cards with tech tags |
| `pages/contact.py` | Contact form + social links |
| `components/ai_chat.py` | IBM Granite chat widget (agent loop) |
| `components/agent_tools.py` | Tool definitions for the ReAct agent |
| `data/profile.py` | Centralised profile data (easy to update) |
| `requirements.txt` | Pinned dependencies |
| `run_portfolio.bat` | One-click Windows launcher |
| `.streamlit/config.toml` | Theme configuration |

---

### Phase 3 — Agent Design (Agentic AI Layer)

**Agent type:** Single-turn ReAct agent (Reason + Act)

**System prompt strategy:**
- Inject Vignesh's full profile as grounding context.
- Define tools: `get_courses()`, `get_skills()`, `get_contact_info()`.
- Instruct the model to use tools when the query maps to structured data.
- Hard-limit output tokens to 512 for fast responses.

**Tool catalogue:**

| Tool | Input | Output |
|---|---|---|
| `get_courses` | topic (optional) | List of courses Vignesh delivers |
| `get_skills` | category (optional) | Skill list with proficiency levels |
| `get_contact_info` | — | Email, LinkedIn, phone placeholder |
| `get_projects` | — | Project summaries |

**Guardrails:**
- Off-topic queries (e.g., political, harmful) → polite decline.
- Max context window: 4 096 tokens (Granite 3 default).
- Temperature: 0.3 (factual, low-creativity mode).

---

### Phase 4 — Development (Implementation)

All source code is implemented across the file structure in Phase 2.

**Key implementation choices:**
- `ibm-watsonx-ai` SDK for Granite model calls (replaces deprecated `ibm-watson-machine-learning`).
- `streamlit-chat` for chat message bubbles.
- Profile data centralised in `data/profile.py` for easy maintenance.
- `.env` file (gitignored) stores `WATSONX_API_KEY` and `WATSONX_PROJECT_ID`.

---

### Phase 5 — Testing & Evaluation

| Test type | Tool / Method | Acceptance criteria |
|---|---|---|
| Unit — agent tools | `pytest` | All tool functions return expected schema |
| Integration — Granite call | Manual + `pytest` | Response in < 5 s, no HTTP errors |
| UI smoke test | Manual Streamlit run | All pages render, no Python errors |
| Agent faithfulness | 10-question golden set | ≥ 90 % correct answers |
| Hallucination check | Manual review | No fabricated course names or dates |

---

### Phase 6 — Deployment

**Local (default):** `run_portfolio.bat` installs deps and launches `streamlit run app.py`.

**Cloud options (future):**
- Streamlit Community Cloud (free tier, connect GitHub repo).
- IBM Code Engine (containerised deployment).
- AWS/GCP via Docker image.

**Environment variables required:**
```
WATSONX_API_KEY=<your-ibm-cloud-api-key>
WATSONX_PROJECT_ID=<your-watsonx-project-id>
WATSONX_URL=https://us-south.ml.cloud.ibm.com
```

---

### Phase 7 — Monitoring & Continuous Improvement

| Concern | Approach |
|---|---|
| Query logging | Append user questions + agent answers to `logs/chat_log.csv` |
| Drift detection | Monthly review of low-confidence responses |
| Model upgrade | Swap model ID string in `data/profile.py` config block |
| Feedback loop | Thumbs up/down widget → updates golden test set |

---

## 3. TECHNOLOGY STACK

| Layer | Technology |
|---|---|
| Frontend | Streamlit 1.40+ |
| AI model | IBM Granite 3 8B Instruct (ibm/granite-3-8b-instruct) |
| AI SDK | ibm-watsonx-ai |
| Data | Python dicts / JSON (no database needed for MVP) |
| Charting | Plotly Express |
| Styling | Custom CSS via `st.markdown` |
| Platform | Python 3.10+ / Windows / Mac / Linux |

---

## 4. RISK REGISTER

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| watsonx API key not configured | High | High | App shows clear setup banner; chat widget disabled gracefully |
| Granite model deprecation | Low | Medium | Model ID is a single config constant |
| Streamlit version incompatibility | Low | Low | Pinned in requirements.txt |
| PII in chat logs | Medium | High | Logs stored locally; no cloud upload |

---

## 5. DEFINITION OF DONE

- [ ] All 6 portfolio pages render without errors.
- [ ] AI chat widget sends a query to IBM Granite and displays a response.
- [ ] Agent uses tools to ground responses in Vignesh's real profile data.
- [ ] `.bat` file launches the app with a single double-click.
- [ ] Source code is modular (each page/component in its own file).
- [ ] README or this SDLC plan is present in the project root.

---

*End of SDLC Plan*
