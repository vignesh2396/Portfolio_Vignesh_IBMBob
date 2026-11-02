"""
Central data store for Vignesh's portfolio.
Edit this file to update any profile information.
"""

# ── Personal ─────────────────────────────────────────────────────────────────
NAME = "Vignesh"
TAGLINE = "Technical Trainer & Expert in Agentic AI · Machine Learning · Quantum Computing"
EMAIL = "vignesh@example.com"
LINKEDIN = "https://linkedin.com/in/vignesh"
GITHUB = "https://github.com/vignesh"
LOCATION = "India"
BIO = """
Vignesh is a passionate technical trainer and practitioner with deep expertise in 
**Agentic AI**, **Machine Learning**, and **Quantum Computing**. With hands-on 
industry experience and a talent for breaking down complex concepts, he has trained 
hundreds of professionals and students across premier organisations. He is affiliated 
with **IBM SkillsBuild** and **Edunet Foundation**, driving AI literacy at scale.
"""

# ── Gemini AI configuration ───────────────────────────────────────────────────
GEMINI_MODEL_ID = "gemini-2.5-flash"
GEMINI_PARAMS = {
    "max_output_tokens": 2048,
    "temperature": 0.3,
    "top_k": 40,
    "top_p": 0.9,
}

# ── IBM watsonx.ai configuration (kept for reference) ─────────────────────────
WATSONX_MODEL_ID = "ibm/granite-3-8b-instruct"
WATSONX_URL = "https://us-south.ml.cloud.ibm.com"
GRANITE_PARAMS = {
    "max_new_tokens": 512,
    "temperature": 0.3,
    "top_k": 40,
    "top_p": 0.9,
    "repetition_penalty": 1.1,
}

# ── Skills ────────────────────────────────────────────────────────────────────
SKILLS = [
    # (Skill Name, Category, Proficiency 0-100)
    ("Agentic AI / LLM Orchestration", "Agentic AI", 95),
    ("IBM Granite & watsonx.ai", "Agentic AI", 90),
    ("Prompt Engineering", "Agentic AI", 92),
    ("RAG Pipelines", "Agentic AI", 88),
    ("LangChain / LlamaIndex", "Agentic AI", 85),
    ("Supervised Learning", "Machine Learning", 93),
    ("Deep Learning (PyTorch/TF)", "Machine Learning", 88),
    ("NLP & Text Analytics", "Machine Learning", 90),
    ("MLOps & Model Deployment", "Machine Learning", 82),
    ("Scikit-learn / XGBoost", "Machine Learning", 91),
    ("Qiskit", "Quantum Computing", 85),
    ("Quantum Algorithms", "Quantum Computing", 80),
    ("Variational Quantum Circuits", "Quantum Computing", 75),
    ("Quantum Machine Learning", "Quantum Computing", 78),
    ("Python", "Programming", 96),
    ("Streamlit / Gradio", "Programming", 90),
    ("Docker / Cloud Deploy", "Programming", 78),
]

# ── Courses Delivered ─────────────────────────────────────────────────────────
COURSES = [
    {
        "title": "Agentic AI Fundamentals to Advanced",
        "audience": "Engineers, Data Scientists",
        "duration": "3 Days",
        "topics": ["ReAct agents", "Tool use", "LangGraph", "IBM Granite", "RAG"],
        "delivered_to": "IBM SkillsBuild cohorts, Edunet Foundation",
        "level": "Beginner → Advanced",
    },
    {
        "title": "Machine Learning Bootcamp",
        "audience": "Fresh graduates, Working professionals",
        "duration": "5 Days",
        "topics": ["Supervised / Unsupervised learning", "Deep Learning", "NLP", "MLOps"],
        "delivered_to": "Gartner partner institutions, College workshops",
        "level": "Beginner → Intermediate",
    },
    {
        "title": "Quantum Computing with Qiskit",
        "audience": "Researchers, Senior engineers",
        "duration": "2 Days",
        "topics": ["Qubit fundamentals", "Gates & circuits", "Grover / Shor", "VQC", "QML"],
        "delivered_to": "Research institutes, IBM TechXchange events",
        "level": "Intermediate → Advanced",
    },
    {
        "title": "IBM watsonx.ai for Enterprise",
        "audience": "Business analysts, IT leads",
        "duration": "1 Day",
        "topics": ["Prompt Lab", "Granite models", "AutoAI", "Responsible AI"],
        "delivered_to": "Enterprise clients via IBM SB4Academia",
        "level": "Beginner",
    },
    {
        "title": "Python for Data Science & AI",
        "audience": "Students, Career switchers",
        "duration": "4 Days",
        "topics": ["Python essentials", "NumPy / Pandas", "Visualisation", "ML intro"],
        "delivered_to": "Edunet Foundation national programme",
        "level": "Beginner",
    },
]

# ── Projects ──────────────────────────────────────────────────────────────────
PROJECTS = [
    {
        "title": "AI-Powered Portfolio Chatbot",
        "description": "This very application — an IBM Granite-based ReAct agent embedded in a Streamlit portfolio to answer visitor queries.",
        "tech": ["Streamlit", "IBM Granite 3", "watsonx.ai", "Python"],
        "status": "Live",
        "link": "#",
    },
    {
        "title": "Quantum-Enhanced Fraud Detection",
        "description": "Hybrid classical-quantum ML pipeline using Qiskit's VQC for credit card fraud detection on imbalanced datasets.",
        "tech": ["Qiskit", "Scikit-learn", "Python", "IBM Quantum"],
        "status": "Completed",
        "link": "#",
    },
    {
        "title": "RAG-based Corporate Knowledge Base",
        "description": "Enterprise RAG system using IBM Granite embeddings + FAISS vector store to answer HR policy questions.",
        "tech": ["LangChain", "FAISS", "IBM Granite", "Streamlit"],
        "status": "Completed",
        "link": "#",
    },
    {
        "title": "AutoML Training Accelerator",
        "description": "No-code ML pipeline builder for educators — upload CSV, pick target column, train and deploy in 3 clicks.",
        "tech": ["Streamlit", "AutoML", "Docker", "FastAPI"],
        "status": "In Progress",
        "link": "#",
    },
]

# ── Testimonials ──────────────────────────────────────────────────────────────
TESTIMONIALS = [
    {
        "name": "Priya S.",
        "role": "Data Scientist, IBM",
        "text": "Vignesh's Agentic AI bootcamp was the most practical training I've attended. Complex concepts made crystal clear!",
    },
    {
        "name": "Arjun R.",
        "role": "ML Engineer, TCS",
        "text": "The Quantum Computing workshop opened a completely new dimension for my research. Vignesh is an exceptional communicator.",
    },
    {
        "name": "Meera K.",
        "role": "Student, IIT",
        "text": "From zero to building my own ReAct agent in three days. The training quality is truly world-class.",
    },
]

# ── Agent system prompt ───────────────────────────────────────────────────────
AGENT_SYSTEM_PROMPT = f"""You are a helpful AI assistant for {NAME}'s personal portfolio website.
Your job is to answer visitors' questions about {NAME}, his expertise, courses, and projects.

## About {NAME}
{BIO}

## Expertise Areas
- Agentic AI: LLM orchestration, IBM Granite, watsonx.ai, RAG, prompt engineering, LangChain
- Machine Learning: supervised/unsupervised learning, deep learning, NLP, MLOps
- Quantum Computing: Qiskit, quantum algorithms, VQC, quantum ML

## Courses Delivered
1. Agentic AI Fundamentals to Advanced (3 days) — ReAct agents, Tool use, LangGraph, IBM Granite, RAG
2. Machine Learning Bootcamp (5 days) — Supervised/Unsupervised learning, Deep Learning, NLP, MLOps
3. Quantum Computing with Qiskit (2 days) — Qubits, Gates, Grover/Shor, VQC, QML
4. IBM watsonx.ai for Enterprise (1 day) — Prompt Lab, Granite models, AutoAI, Responsible AI
5. Python for Data Science & AI (4 days) — Python essentials, NumPy/Pandas, ML intro

## Contact
- Email: {EMAIL}
- LinkedIn: {LINKEDIN}
- Location: {LOCATION}

## Instructions
- Answer only questions related to {NAME}, his skills, courses, projects, or the technology domains above.
- For off-topic questions, politely say you can only help with {NAME}'s portfolio.
- Be concise, friendly, and professional.
- If asked about booking a training, direct the visitor to the Contact page or email.
- Do NOT make up facts not present above.
"""
