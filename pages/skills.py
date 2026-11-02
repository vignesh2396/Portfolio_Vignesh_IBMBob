"""Skills matrix page with interactive Plotly charts."""
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from data.profile import SKILLS


def render():
    st.markdown('<div class="section-heading">Skills Matrix</div>', unsafe_allow_html=True)

    # ── Build dataframe ────────────────────────────────────────────────────────
    df = pd.DataFrame(SKILLS, columns=["Skill", "Category", "Proficiency"])

    categories = df["Category"].unique().tolist()
    selected_cat = st.selectbox(
        "Filter by category", ["All"] + categories, key="skills_cat_filter"
    )
    filtered = df if selected_cat == "All" else df[df["Category"] == selected_cat]

    # ── Tab layout ─────────────────────────────────────────────────────────────
    tab1, tab2, tab3 = st.tabs(["📊 Bar Chart", "🕸️ Radar Chart", "📋 Table"])

    with tab1:
        fig = px.bar(
            filtered.sort_values("Proficiency", ascending=True),
            x="Proficiency",
            y="Skill",
            color="Category",
            orientation="h",
            color_discrete_sequence=px.colors.qualitative.Pastel,
            template="plotly_dark",
            title="Skill Proficiency (%)",
        )
        fig.update_layout(
            paper_bgcolor="#1a1f2e",
            plot_bgcolor="#1a1f2e",
            margin=dict(l=10, r=10, t=40, b=10),
            xaxis_range=[0, 100],
            height=450,
            legend_title_text="Category",
        )
        fig.update_traces(marker_line_width=0)
        st.plotly_chart(fig, use_container_width=True)

    with tab2:
        # Radar — one spoke per category, value = max proficiency
        cat_max = df.groupby("Category")["Proficiency"].mean().reset_index()
        cats = cat_max["Category"].tolist()
        vals = cat_max["Proficiency"].tolist()
        # close the polygon
        cats_closed = cats + [cats[0]]
        vals_closed = vals + [vals[0]]

        fig_radar = go.Figure()
        fig_radar.add_trace(
            go.Scatterpolar(
                r=vals_closed,
                theta=cats_closed,
                fill="toself",
                fillcolor="rgba(99,179,237,0.2)",
                line=dict(color="#63b3ed", width=2),
                name="Avg Proficiency",
            )
        )
        fig_radar.update_layout(
            polar=dict(
                bgcolor="#1a1f2e",
                radialaxis=dict(visible=True, range=[0, 100], color="#4a5568"),
                angularaxis=dict(color="#a0aec0"),
            ),
            paper_bgcolor="#1a1f2e",
            font=dict(color="#e2e8f0"),
            title="Average Proficiency per Domain",
            height=420,
            margin=dict(l=40, r=40, t=60, b=40),
        )
        st.plotly_chart(fig_radar, use_container_width=True)

    with tab3:
        # Custom HTML table
        rows_html = ""
        for _, row in filtered.iterrows():
            bar = f"""
<div class="skill-bar-bg">
  <div class="skill-bar-fill" style="width:{row['Proficiency']}%"></div>
</div>"""
            rows_html += f"""
<tr>
  <td style="padding:8px 12px; color:#e2e8f0">{row['Skill']}</td>
  <td style="padding:8px 12px; color:#a0aec0">{row['Category']}</td>
  <td style="padding:8px 12px; min-width:160px">{bar}<span style="color:#63b3ed; font-size:0.85rem">{row['Proficiency']}%</span></td>
</tr>"""

        st.markdown(f"""
<table style="width:100%; border-collapse:collapse; background:#1a1f2e; border-radius:10px; overflow:hidden">
  <thead>
    <tr style="background:#2d3748">
      <th style="padding:10px 12px; text-align:left; color:#63b3ed">Skill</th>
      <th style="padding:10px 12px; text-align:left; color:#63b3ed">Category</th>
      <th style="padding:10px 12px; text-align:left; color:#63b3ed">Proficiency</th>
    </tr>
  </thead>
  <tbody>{rows_html}</tbody>
</table>
""", unsafe_allow_html=True)
