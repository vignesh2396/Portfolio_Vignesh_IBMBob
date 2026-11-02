"""Courses delivered page."""
import streamlit as st
from data.profile import COURSES, TESTIMONIALS

LEVEL_COLOR = {
    "Beginner": "#68d391",
    "Beginner → Intermediate": "#f6ad55",
    "Beginner → Advanced": "#fc8181",
    "Intermediate → Advanced": "#b794f4",
}


def render():
    st.markdown('<div class="section-heading">Courses & Training Programmes</div>', unsafe_allow_html=True)
    st.markdown(
        "<p style='color:#a0aec0'>Explore the training programmes Vignesh delivers. "
        "Each is customisable for your organisation's level and domain.</p>",
        unsafe_allow_html=True,
    )

    # ── Course cards ───────────────────────────────────────────────────────────
    for course in COURSES:
        level_color = LEVEL_COLOR.get(course["level"], "#63b3ed")
        topics_html = " ".join(f'<span class="tech-badge">{t}</span>' for t in course["topics"])

        st.markdown(
            f"""
<div class="portfolio-card" style="border-left: 4px solid {level_color}">
    <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:0.5rem">
        <div>
            <div style="font-size:1.15rem; font-weight:700; color:#e2e8f0">{course['title']}</div>
            <div style="color:#a0aec0; font-size:0.9rem; margin-top:4px">
                🎯 {course['audience']} &nbsp;|&nbsp; ⏱️ {course['duration']} &nbsp;|&nbsp; 🏢 {course['delivered_to']}
            </div>
        </div>
        <span style="background:{level_color}22; color:{level_color}; border:1px solid {level_color};
              border-radius:20px; padding:3px 12px; font-size:0.8rem; white-space:nowrap">
            {course['level']}
        </span>
    </div>
    <div style="margin-top:0.75rem">{topics_html}</div>
</div>
""",
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Booking CTA ────────────────────────────────────────────────────────────
    st.markdown(
        """
<div style="background:linear-gradient(135deg,#1a1f2e,#2d3748);
     border:1px solid #4299e1; border-radius:12px; padding:1.5rem; text-align:center">
    <div style="font-size:1.2rem; font-weight:700; color:#63b3ed; margin-bottom:0.5rem">
        📩 Book a Custom Training
    </div>
    <div style="color:#a0aec0">
        Need a tailored workshop for your team? Reach out via the Contact page
        or email directly to discuss duration, topics, and scheduling.
    </div>
</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Testimonials ───────────────────────────────────────────────────────────
    st.markdown('<div class="section-heading">What Participants Say</div>', unsafe_allow_html=True)

    cols = st.columns(len(TESTIMONIALS))
    for col, t in zip(cols, TESTIMONIALS):
        with col:
            st.markdown(
                f"""
<div class="portfolio-card" style="border-top:3px solid #b794f4; height:100%">
    <div style="color:#e2e8f0; font-style:italic; font-size:0.95rem">"{t['text']}"</div>
    <div style="margin-top:1rem">
        <div style="color:#b794f4; font-weight:600">{t['name']}</div>
        <div style="color:#a0aec0; font-size:0.85rem">{t['role']}</div>
    </div>
</div>
""",
                unsafe_allow_html=True,
            )
