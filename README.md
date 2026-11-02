# 🧠 Vignesh — AI & Quantum Expert Portfolio

A personal portfolio website built with **Streamlit**, powered by **Google Gemini 2.5 Flash** as an intelligent AI assistant. Built as part of the **IBM SkillsBuild × Edunet Foundation × Gartner Program**.

[![Streamlit](https://img.shields.io/badge/Streamlit-1.66+-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://python.org)
[![Google Gemini](https://img.shields.io/badge/Gemini-2.5%20Flash-4285F4?logo=google&logoColor=white)](https://aistudio.google.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## ✨ Features

| Page | Description |
|---|---|
| 🏠 **Home** | Hero section, bio, stats, and testimonials |
| 💡 **Skills** | Skill bars across Agentic AI, ML, Quantum, Programming |
| 📚 **Courses** | Full catalogue of training courses delivered |
| 🚀 **Projects** | Showcase of AI, Quantum & ML projects |
| 🤖 **AI Assistant** | Gemini-powered ReAct chat agent — ask anything about Vignesh |
| 📬 **Contact** | Contact form and social links |

---

## 🏗️ Project Structure

```
Portfolio_Vignesh_IBMBob/
├── app.py                  # Main entry point — page config, CSS, navigation
├── requirements.txt        # Python dependencies
├── .env.example            # Environment variable template
├── .streamlit/
│   └── config.toml         # Streamlit theme (dark mode, custom colours)
├── data/
│   └── profile.py          # All portfolio data (skills, courses, projects, bio)
├── components/
│   ├── ai_chat.py          # Gemini-powered AI chat component
│   └── agent_tools.py      # ReAct agent tool functions
└── pages/
    ├── home.py
    ├── skills.py
    ├── courses.py
    ├── projects.py
    └── contact.py
```

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/vignesh2396/Portfolio_Vignesh_IBMBob.git
cd Portfolio_Vignesh_IBMBob
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy the example file and fill in your credentials:

```bash
cp .env.example .env
```

Edit `.env`:

```env
GEMINI_API_KEY=your-google-gemini-api-key-here
```

> Get a free Gemini API key at [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

### 5. Run the app

```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🔧 Configuration

### Environment Variables

| Variable | Required | Description |
|---|---|---|
| `GEMINI_API_KEY` | ✅ Yes | Google Gemini API key for the AI assistant |

> Without `GEMINI_API_KEY`, the app runs in **demo mode** — all pages except the AI Assistant are fully functional.

### Streamlit Theme

The dark theme is pre-configured in [`.streamlit/config.toml`](.streamlit/config.toml):

```toml
[theme]
base                     = "dark"
primaryColor             = "#63b3ed"
backgroundColor          = "#0f1117"
secondaryBackgroundColor = "#1a1f2e"
textColor                = "#e2e8f0"
```

---

## 🤖 AI Assistant — How It Works

The AI Assistant uses a **ReAct (Reason + Act) agent** pattern:

1. User sends a question
2. Gemini 2.5 Flash reasons about what tool (if any) to use
3. If a tool call is detected (`TOOL_CALL: {...}`), the tool runs and the result is fed back
4. Gemini produces a final grounded answer

**Available tools:**

| Tool | Description |
|---|---|
| `get_courses(topic)` | Lists training courses, optionally filtered by topic |
| `get_skills(category)` | Lists skills by category |
| `get_contact_info()` | Returns email, LinkedIn, and location |
| `get_projects()` | Lists all project summaries |

---

## 📦 Dependencies

```
streamlit>=1.40.0
google-genai>=1.0.0
plotly>=5.22.0
pandas>=2.2.0
python-dotenv>=1.0.0
streamlit-option-menu>=0.3.12
```

---

## 🛠️ Customisation

All portfolio data lives in a single file: [`data/profile.py`](data/profile.py).

Edit it to update:
- Personal info (name, bio, email, LinkedIn, GitHub)
- Skills list and proficiency percentages
- Courses catalogue
- Projects showcase
- Testimonials
- Agent system prompt

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgements

- Built during the **IBM SkillsBuild × Edunet Foundation × Gartner Program 2026**
- AI assistant powered by **Google Gemini 2.5 Flash**
- Portfolio UI built with **Streamlit**
- Developed with **IBM Bob** (AI-assisted development)
