"""Projects showcase page."""
import streamlit as st
from data.profile import PROJECTS

STATUS_COLOR = {
    "Live": "#68d391",
    "Completed": "#63b3ed",
    "In Progress": "#f6ad55",
}


def render():
    st.markdown('<div class="section-heading">Projects & Builds</div>', unsafe_allow_html=True)
    st.markdown(
        "<p style='color:#a0aec0'>A selection of technical projects spanning Agentic AI, "
        "Quantum Computing, and MLOps.</p>",
        unsafe_allow_html=True,
    )

    cols_per_row = 2
    rows = [PROJECTS[i:i + cols_per_row] for i in range(0, len(PROJECTS), cols_per_row)]

    for row in rows:
        cols = st.columns(cols_per_row, gap="medium")
        for col, project in zip(cols, row):
            status_color = STATUS_COLOR.get(project["status"], "#a0aec0")
            tech_badges = " ".join(
                f'<span class="tech-badge">{t}</span>' for t in project["tech"]
            )

            with col:
                st.markdown(
                    f"""
<div class="portfolio-card" style="height:100%; border-top:3px solid {status_color}">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem">
        <div style="font-size:1.1rem; font-weight:700; color:#e2e8f0">{project['title']}</div>
        <span style="background:{status_color}22; color:{status_color}; border:1px solid {status_color};
              border-radius:20px; padding:2px 10px; font-size:0.78rem; white-space:nowrap; margin-left:8px">
            {project['status']}
        </span>
    </div>
    <div style="color:#a0aec0; font-size:0.9rem; line-height:1.6; margin-bottom:0.75rem">
        {project['description']}
    </div>
    <div>{tech_badges}</div>
</div>
""",
                    unsafe_allow_html=True,
                )

    st.markdown("<br>", unsafe_allow_html=True)

    # ── GitHub CTA ─────────────────────────────────────────────────────────────
    st.markdown(
        """
<div style="text-align:center; padding:1.25rem; background:#1a1f2e;
     border:1px solid #2d3748; border-radius:12px">
    <div style="color:#a0aec0">
        🔗 More projects and code samples available on
        <a href="https://github.com/vignesh" style="color:#63b3ed">GitHub</a>
    </div>
</div>
""",
        unsafe_allow_html=True,
    )
