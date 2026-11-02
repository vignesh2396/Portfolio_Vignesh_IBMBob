"""
Vignesh Personal Portfolio — Main Application Entry Point
"""
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# ── Page config (must be first Streamlit call) ─────────────────────────────────
st.set_page_config(
    page_title="Vignesh | AI & Quantum Expert",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Shared CSS ─────────────────────────────────────────────────────────────────
def inject_global_css():
    st.markdown("""
<style>
/* ── Base ── */
html, body, [class*="css"] {
    font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f1117 0%, #1a1f2e 100%);
    border-right: 1px solid #2d3748;
}
[data-testid="stSidebar"] * {
    color: #e2e8f0 !important;
}
[data-testid="stSidebar"] .stButton > button {
    background: transparent;
    border: 1px solid #4a5568;
    color: #e2e8f0 !important;
    border-radius: 8px;
    width: 100%;
    margin-bottom: 4px;
    transition: all 0.2s;
}
[data-testid="stSidebar"] .stButton > button:hover {
    background: #2d3748 !important;
    border-color: #63b3ed !important;
}

/* ── Cards ── */
.portfolio-card {
    background: #1a1f2e;
    border: 1px solid #2d3748;
    border-radius: 12px;
    padding: 1.25rem 1.5rem;
    margin-bottom: 1rem;
    transition: border-color 0.2s;
}
.portfolio-card:hover {
    border-color: #4299e1;
}

/* ── Hero gradient text ── */
.hero-title {
    font-size: 3rem;
    font-weight: 800;
    background: linear-gradient(135deg, #63b3ed 0%, #b794f4 50%, #68d391 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1.2;
}

/* ── Badges ── */
.tech-badge {
    display: inline-block;
    background: #2d3748;
    color: #90cdf4;
    border: 1px solid #4a5568;
    border-radius: 20px;
    padding: 2px 12px;
    font-size: 0.8rem;
    margin: 2px;
}

/* ── Section headings ── */
.section-heading {
    font-size: 1.8rem;
    font-weight: 700;
    color: #63b3ed;
    border-bottom: 2px solid #2d3748;
    padding-bottom: 0.5rem;
    margin-bottom: 1.5rem;
}

/* ── Skill bar ── */
.skill-bar-bg {
    background: #2d3748;
    border-radius: 9999px;
    height: 8px;
    width: 100%;
    margin-top: 4px;
}
.skill-bar-fill {
    background: linear-gradient(90deg, #4299e1, #b794f4);
    border-radius: 9999px;
    height: 8px;
}

/* ── Stat tiles ── */
.stat-tile {
    text-align: center;
    padding: 1.5rem 1rem;
    background: #1a1f2e;
    border: 1px solid #2d3748;
    border-radius: 12px;
}
.stat-number {
    font-size: 2.5rem;
    font-weight: 800;
    color: #63b3ed;
}
.stat-label {
    color: #a0aec0;
    font-size: 0.9rem;
}

/* ── Chat ── */
[data-testid="stChatMessage"] {
    background: #1a1f2e;
    border: 1px solid #2d3748;
    border-radius: 10px;
    margin-bottom: 0.5rem;
}

/* ── Remove default Streamlit top padding ── */
.main .block-container {
    padding-top: 1rem;
}

/* ── Footer ── */
.portfolio-footer {
    text-align: center;
    color: #4a5568;
    font-size: 0.8rem;
    border-top: 1px solid #2d3748;
    padding-top: 1rem;
    margin-top: 3rem;
}
</style>
""", unsafe_allow_html=True)


# ── Navigation ─────────────────────────────────────────────────────────────────
def sidebar_nav():
    with st.sidebar:
        st.markdown("""
<div style='text-align:center; padding: 1.5rem 0 1rem'>
    <div style='font-size:3rem'>🧠</div>
    <div style='font-size:1.2rem; font-weight:700; color:#63b3ed'>Vignesh</div>
    <div style='font-size:0.8rem; color:#a0aec0; margin-top:4px'>
        AI · ML · Quantum Trainer
    </div>
</div>
<hr style='border-color:#2d3748; margin:0 0 1rem'>
""", unsafe_allow_html=True)

        pages = {
            "🏠  Home": "home",
            "💡  Skills": "skills",
            "📚  Courses": "courses",
            "🚀  Projects": "projects",
            "🤖  AI Assistant": "chat",
            "📬  Contact": "contact",
        }

        if "page" not in st.session_state:
            st.session_state.page = "home"

        for label, key in pages.items():
            active = st.session_state.page == key
            style = "background:#2d3748; border-color:#63b3ed;" if active else ""
            if st.button(label, key=f"nav_{key}", use_container_width=True):
                st.session_state.page = key
                st.rerun()

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(
            "<div style='font-size:0.72rem; color:#4a5568; text-align:center;'>"
            "Powered by IBM Granite 🔷</div>",
            unsafe_allow_html=True,
        )


# ── Page router ────────────────────────────────────────────────────────────────
def main():
    inject_global_css()
    sidebar_nav()

    page = st.session_state.get("page", "home")

    if page == "home":
        from pages.home import render
        render()
    elif page == "skills":
        from pages.skills import render
        render()
    elif page == "courses":
        from pages.courses import render
        render()
    elif page == "projects":
        from pages.projects import render
        render()
    elif page == "chat":
        from components.ai_chat import render_chat
        render_chat()
    elif page == "contact":
        from pages.contact import render
        render()


if __name__ == "__main__":
    main()
