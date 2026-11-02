"""Contact page."""
import streamlit as st
from data.profile import EMAIL, LINKEDIN, GITHUB, LOCATION, NAME


def render():
    st.markdown('<div class="section-heading">Get in Touch</div>', unsafe_allow_html=True)
    st.markdown(
        "<p style='color:#a0aec0'>Interested in a training engagement, collaboration, "
        "or just want to connect? Reach out through any of the channels below.</p>",
        unsafe_allow_html=True,
    )

    left, right = st.columns([1, 1], gap="large")

    # ── Contact info ───────────────────────────────────────────────────────────
    with left:
        st.markdown('<div style="font-size:1.1rem; font-weight:700; color:#63b3ed; margin-bottom:1rem">Contact Details</div>', unsafe_allow_html=True)

        channels = [
            ("📧", "Email", EMAIL, f"mailto:{EMAIL}"),
            ("💼", "LinkedIn", "linkedin.com/in/vignesh", LINKEDIN),
            ("🐙", "GitHub", "github.com/vignesh", GITHUB),
            ("📍", "Location", LOCATION, None),
        ]
        for icon, label, value, href in channels:
            link = f'<a href="{href}" style="color:#63b3ed; text-decoration:none">{value}</a>' if href else f'<span style="color:#e2e8f0">{value}</span>'
            st.markdown(
                f"""
<div class="portfolio-card" style="padding:0.75rem 1rem; margin-bottom:0.5rem">
    <span style="font-size:1.2rem; margin-right:10px">{icon}</span>
    <span style="color:#a0aec0; margin-right:8px">{label}:</span>
    {link}
</div>
""",
                unsafe_allow_html=True,
            )

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(
            """
<div style="background:#1a1f2e; border:1px solid #2d3748; border-radius:10px; padding:1rem">
    <div style="color:#b794f4; font-weight:600; margin-bottom:0.5rem">🕐 Response Time</div>
    <div style="color:#a0aec0; font-size:0.9rem">
        Typically responds within 24–48 hours on business days.
        For urgent training enquiries, email directly.
    </div>
</div>
""",
            unsafe_allow_html=True,
        )

    # ── Contact form ───────────────────────────────────────────────────────────
    with right:
        st.markdown('<div style="font-size:1.1rem; font-weight:700; color:#63b3ed; margin-bottom:1rem">Send a Message</div>', unsafe_allow_html=True)

        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Your Name *", placeholder="e.g. Priya Sharma")
            email = st.text_input("Your Email *", placeholder="priya@company.com")
            subject = st.selectbox(
                "Subject *",
                [
                    "Training Enquiry",
                    "Corporate Workshop",
                    "Collaboration / Research",
                    "Speaking Engagement",
                    "Other",
                ],
            )
            message = st.text_area("Message *", placeholder="Tell me what you have in mind…", height=140)
            submitted = st.form_submit_button("📤 Send Message", use_container_width=True)

            if submitted:
                if not name or not email or not message:
                    st.error("Please fill in all required fields (*)")
                elif "@" not in email:
                    st.error("Please enter a valid email address.")
                else:
                    # In production, integrate with an email API or form backend here
                    st.success(
                        f"✅ Thank you, **{name}**! Your message has been received. "
                        f"{NAME} will get back to you at **{email}** shortly."
                    )

    # ── Affiliations ───────────────────────────────────────────────────────────
    st.markdown("<hr style='border-color:#2d3748; margin:2rem 0'>", unsafe_allow_html=True)
    st.markdown('<div class="section-heading">Affiliations</div>', unsafe_allow_html=True)

    affiliations = [
        ("🔷", "IBM SkillsBuild", "Official training partner — Agentic AI & Watson"),
        ("🎓", "Edunet Foundation", "National AI literacy programmes for students"),
        ("📊", "Gartner Programme", "Enterprise technology research & training"),
    ]

    cols = st.columns(len(affiliations))
    for col, (icon, org, role) in zip(cols, affiliations):
        with col:
            st.markdown(
                f"""
<div class="portfolio-card" style="text-align:center">
    <div style="font-size:2rem; margin-bottom:0.5rem">{icon}</div>
    <div style="font-weight:700; color:#63b3ed; margin-bottom:0.25rem">{org}</div>
    <div style="color:#a0aec0; font-size:0.85rem">{role}</div>
</div>
""",
                unsafe_allow_html=True,
            )
