"""Home / Hero page."""
import streamlit as st
from data.profile import NAME, TAGLINE, BIO, LINKEDIN, GITHUB, EMAIL


def render():
    # ── Hero section ───────────────────────────────────────────────────────────
    col1, col2 = st.columns([3, 1], gap="large")

    with col1:
        st.markdown(
            f'<div class="hero-title">{NAME}</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<p style="font-size:1.15rem; color:#a0aec0; margin-top:0.5rem">{TAGLINE}</p>',
            unsafe_allow_html=True,
        )
        st.markdown("<br>", unsafe_allow_html=True)

        c1, c2, c3 = st.columns(3)
        with c1:
            if st.button("📚 View Courses", use_container_width=True):
                st.session_state.page = "courses"
                st.rerun()
        with c2:
            if st.button("🤖 Ask AI Assistant", use_container_width=True):
                st.session_state.page = "chat"
                st.rerun()
        with c3:
            if st.button("📬 Get in Touch", use_container_width=True):
                st.session_state.page = "contact"
                st.rerun()

    with col2:
        st.markdown(
            """
<div style='text-align:center; padding:1rem;
     background:linear-gradient(135deg,#1a1f2e,#2d3748);
     border:2px solid #4299e1; border-radius:50%;
     width:140px; height:140px; line-height:120px;
     font-size:4rem; margin:auto;'>🧑‍💻</div>
""",
            unsafe_allow_html=True,
        )

    st.markdown("<hr style='border-color:#2d3748; margin:2rem 0'>", unsafe_allow_html=True)

    # ── Stats row ──────────────────────────────────────────────────────────────
    stats = [
        ("5+", "Courses Delivered"),
        ("500+", "Professionals Trained"),
        ("4", "Projects Completed"),
        ("3", "Domains of Expertise"),
    ]
    cols = st.columns(len(stats))
    for col, (num, label) in zip(cols, stats):
        with col:
            st.markdown(
                f"""
<div class="stat-tile">
    <div class="stat-number">{num}</div>
    <div class="stat-label">{label}</div>
</div>
""",
                unsafe_allow_html=True,
            )

    st.markdown("<br>", unsafe_allow_html=True)

    # ── About section ──────────────────────────────────────────────────────────
    st.markdown('<div class="section-heading">About Me</div>', unsafe_allow_html=True)
    st.markdown(BIO)

    # ── Expertise domains ──────────────────────────────────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-heading">Domains of Expertise</div>', unsafe_allow_html=True)

    domains = [
        (
            "🤖", "Agentic AI",
            "Building and training on autonomous AI agents, LLM orchestration with IBM Granite, "
            "RAG pipelines, prompt engineering, and LangChain / LlamaIndex.",
            "#4299e1",
        ),
        (
            "📈", "Machine Learning",
            "End-to-end ML: supervised/unsupervised learning, deep learning, NLP, MLOps, "
            "and model deployment on cloud platforms.",
            "#b794f4",
        ),
        (
            "⚛️", "Quantum Computing",
            "Quantum fundamentals through advanced Qiskit programming, variational circuits, "
            "Grover / Shor algorithms, and quantum-classical hybrid ML.",
            "#68d391",
        ),
    ]

    cols = st.columns(3)
    for col, (icon, title, desc, color) in zip(cols, domains):
        with col:
            st.markdown(
                f"""
<div class="portfolio-card" style="border-top: 3px solid {color}">
    <div style="font-size:2rem; margin-bottom:0.5rem">{icon}</div>
    <div style="font-size:1.1rem; font-weight:700; color:{color}; margin-bottom:0.5rem">{title}</div>
    <div style="color:#a0aec0; font-size:0.9rem">{desc}</div>
</div>
""",
                unsafe_allow_html=True,
            )

    # ── Footer ─────────────────────────────────────────────────────────────────
    st.markdown(
        f"""
<div class="portfolio-footer">
    <a href="{LINKEDIN}" style="color:#63b3ed; margin:0 12px">LinkedIn</a> |
    <a href="{GITHUB}" style="color:#63b3ed; margin:0 12px">GitHub</a> |
    <a href="mailto:{EMAIL}" style="color:#63b3ed; margin:0 12px">Email</a>
    <br><br>© 2026 {NAME} · Powered by IBM Granite &amp; Streamlit
</div>
""",
        unsafe_allow_html=True,
    )
