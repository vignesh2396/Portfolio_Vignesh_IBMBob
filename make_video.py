"""
make_video.py  —  150-second portfolio slideshow  (moviepy 1.0.3 + Pillow)
Generates: Portfolio_Video.mp4 in the same directory as this script.

Strategy: pre-render every frame as a PIL image at a low FPS (12), then hand
the frame list to ImageSequenceClip — no expensive make_frame callbacks.

Usage:
    python make_video.py
"""

import os
import textwrap
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import ImageSequenceClip

# ── Output ─────────────────────────────────────────────────────────────────────
OUTPUT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "Portfolio_Video.mp4")
W, H  = 1280, 720
FPS   = 12          # render FPS — keeps frame count manageable
TRANS = 0.5         # cross-dissolve duration (seconds)

# ── Brand colours ──────────────────────────────────────────────────────────────
BG_DARK     = (15,  17,  23)
SURFACE     = (26,  31,  46)
ACCENT_BLUE = (99,  179, 237)
ACCENT_PURP = (183, 148, 244)
ACCENT_GRN  = (104, 211, 145)
TEXT_MAIN   = (226, 232, 240)
TEXT_MUTED  = (160, 174, 192)
BORDER      = (45,  55,  72)


# ── Fonts ──────────────────────────────────────────────────────────────────────
def _font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = (
        ["arialbd.ttf", "Arial Bold.ttf", "DejaVuSans-Bold.ttf",
         "C:/Windows/Fonts/arialbd.ttf"] if bold
        else ["arial.ttf", "Arial.ttf", "DejaVuSans.ttf",
              "C:/Windows/Fonts/arial.ttf"]
    )
    for name in candidates:
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            pass
    return ImageFont.load_default()


def _wrap(text: str, chars: int) -> list:
    return textwrap.wrap(text, width=max(chars, 10)) or [text]


# ── Slide renderer ─────────────────────────────────────────────────────────────
def render_slide(
    title: str,
    body: list,
    accent: tuple,
    subtitle: str = "",
    tag: str = "",
    progress: float = 0.0,
    right_col: list = None,
) -> np.ndarray:
    """Return a (H, W, 3) uint8 array for one frame."""
    img  = Image.new("RGB", (W, H), BG_DARK)
    draw = ImageDraw.Draw(img)

    # gradient top band
    for y in range(110):
        t = y / 109
        r = int(SURFACE[0]*(1-t) + BG_DARK[0]*t)
        g = int(SURFACE[1]*(1-t) + BG_DARK[1]*t)
        b = int(SURFACE[2]*(1-t) + BG_DARK[2]*t)
        draw.line([(0, y), (W, y)], fill=(r, g, b))

    # left accent stripe
    draw.rectangle([(0, 0), (5, H)], fill=accent)

    # progress bar
    bw = int(W * min(progress, 1.0))
    draw.rectangle([(0, H-6), (W, H)],    fill=BORDER)
    draw.rectangle([(0, H-6), (bw, H)],   fill=accent)

    # tag pill
    if tag:
        tf = _font(18)
        bb = draw.textbbox((0, 0), f"  {tag}  ", font=tf)
        tw = bb[2]-bb[0]; th = bb[3]-bb[1]
        tx, ty = 40, 28
        draw.rounded_rectangle([(tx, ty), (tx+tw+8, ty+th+8)],
                                radius=10, fill=SURFACE, outline=accent)
        draw.text((tx+4, ty+4), f"  {tag}  ", font=tf, fill=accent)

    # title
    title_y = 78 if tag else 48
    draw.text((40, title_y), title, font=_font(50, bold=True), fill=TEXT_MAIN)

    # subtitle
    sub_y = title_y + 64
    if subtitle:
        draw.text((42, sub_y), subtitle, font=_font(25), fill=TEXT_MUTED)
        sub_y += 40

    # horizontal rule
    rule_y = sub_y + 8
    draw.line([(40, rule_y), (W-40, rule_y)], fill=BORDER, width=2)
    body_y = rule_y + 22

    col_x  = 40
    col_w  = (W - 80) if right_col is None else (W // 2 - 60)
    col_chars = max(col_w // 11, 20)

    bf = _font(22); blt = _font(20)

    def draw_lines(lines, x, y, width_chars, bullet_color=accent):
        for line in lines:
            if y > H - 40:
                break
            if line.startswith("•"):
                for part in _wrap(line, width_chars):
                    draw.ellipse([(x+4, y+9), (x+12, y+17)], fill=bullet_color)
                    draw.text((x+20, y), part.lstrip("• "), font=blt, fill=TEXT_MAIN)
                    y += 29
            elif line.startswith("──"):
                draw.line([(x, y+10), (x+col_w, y+10)], fill=BORDER, width=1)
                y += 22
            elif line == "":
                y += 12
            else:
                for part in _wrap(line, width_chars):
                    draw.text((x, y), part, font=bf, fill=TEXT_MAIN)
                    y += 31
        return y

    draw_lines(body, col_x, body_y, col_chars, accent)

    if right_col:
        rx = W // 2 + 20
        draw.line([(W//2, body_y-10), (W//2, H-30)], fill=BORDER, width=1)
        draw_lines(right_col, rx, body_y, col_chars, ACCENT_PURP)

    # watermark
    draw.text((W-290, H-26), "IBM SkillsBuild × Edunet × Gartner 2026",
              font=_font(15), fill=BORDER)

    return np.array(img)


# ── Slide definitions — 7 slides × ~21 s ≈ 150 s total ───────────────────────
SLIDES = [
    # 0 — Title card (20 s)
    dict(
        duration=20, tag="IBM SkillsBuild × Edunet × Gartner 2026",
        title="Vignesh", subtitle="AI  ·  Machine Learning  ·  Quantum Computing",
        accent=ACCENT_BLUE,
        body=[
            "Technical Trainer & Practitioner",
            "",
            "• Agentic AI  |  LLM Orchestration  |  IBM Granite",
            "• Supervised & Unsupervised Machine Learning",
            "• Quantum Computing with Qiskit",
            "• Python  ·  Streamlit  ·  Docker  ·  MLOps",
            "",
            "Portfolio built with Streamlit + IBM Bob",
        ],
    ),
    # 1 — About (22 s)
    dict(
        duration=22, tag="About",
        title="Who is Vignesh?", subtitle="", accent=ACCENT_PURP,
        body=[
            "Passionate technical trainer with deep expertise in three",
            "cutting-edge domains:",
            "",
            "• Agentic AI — LLM orchestration, IBM Granite, watsonx.ai,",
            "  RAG pipelines, LangChain / LlamaIndex",
            "• Machine Learning — supervised & unsupervised, deep learning,",
            "  NLP, MLOps, Scikit-learn, XGBoost",
            "• Quantum Computing — Qiskit, Grover / Shor algorithms,",
            "  VQC, Quantum Machine Learning",
            "",
            "Affiliated with IBM SkillsBuild & Edunet Foundation,",
            "driving AI literacy at scale across India.",
        ],
    ),
    # 2 — Skills (22 s, two columns)
    dict(
        duration=22, tag="Skills",
        title="Core Competencies", subtitle="Proficiency levels",
        accent=ACCENT_GRN,
        body=[
            "AGENTIC AI",
            "• Agentic AI / LLM Orchestration    95 %",
            "• Prompt Engineering                92 %",
            "• IBM Granite & watsonx.ai          90 %",
            "• RAG Pipelines                     88 %",
            "• LangChain / LlamaIndex            85 %",
        ],
        right_col=[
            "MACHINE LEARNING",
            "• Supervised Learning               93 %",
            "• NLP & Text Analytics              90 %",
            "• Deep Learning (PyTorch/TF)        88 %",
            "• Scikit-learn / XGBoost            91 %",
            "",
            "QUANTUM COMPUTING",
            "• Qiskit                            85 %",
            "• Quantum Algorithms                80 %",
            "• Quantum Machine Learning          78 %",
        ],
    ),
    # 3 — Courses (22 s)
    dict(
        duration=22, tag="Courses Delivered",
        title="Training Catalogue", subtitle="5 flagship programmes",
        accent=ACCENT_BLUE,
        body=[
            "1  Agentic AI: Fundamentals to Advanced      [3 Days]",
            "   ReAct agents · Tool use · LangGraph · IBM Granite · RAG",
            "──",
            "2  Machine Learning Bootcamp                 [5 Days]",
            "   Supervised & Unsupervised · Deep Learning · NLP · MLOps",
            "──",
            "3  Quantum Computing with Qiskit             [2 Days]",
            "   Qubits · Gates · Grover/Shor · VQC · QML",
            "──",
            "4  IBM watsonx.ai for Enterprise             [1 Day]",
            "   Prompt Lab · Granite models · AutoAI · Responsible AI",
            "──",
            "5  Python for Data Science & AI              [4 Days]",
            "   Python essentials · NumPy/Pandas · Visualisation · ML intro",
        ],
    ),
    # 4 — Projects (22 s)
    dict(
        duration=22, tag="Projects",
        title="Featured Work", subtitle="", accent=ACCENT_PURP,
        body=[
            "[Live]      AI-Powered Portfolio Chatbot",
            "            IBM Granite ReAct agent · Streamlit · watsonx.ai",
            "──",
            "[Done]      Quantum-Enhanced Fraud Detection",
            "            Hybrid VQC pipeline · Qiskit · Scikit-learn",
            "──",
            "[Done]      RAG Corporate Knowledge Base",
            "            LangChain · FAISS · IBM Granite embeddings",
            "──",
            "[Active]    AutoML Training Accelerator",
            "            No-code ML builder · Streamlit · Docker · FastAPI",
        ],
    ),
    # 5 — Tech Stack (22 s)
    dict(
        duration=22, tag="Tech Stack",
        title="Portfolio: Under the Hood",
        subtitle="Built during IBM SkillsBuild × Edunet × Gartner 2026",
        accent=ACCENT_GRN,
        body=[
            "FRONTEND",
            "• Streamlit 1.66+  —  multi-page dark-themed app",
            "• Custom CSS  —  gradient hero, skill bars, card UI",
            "",
            "AI LAYER",
            "• Google Gemini 2.5 Flash  —  primary LLM",
            "• ReAct (Reason + Act) agent pattern",
            "• Tools: get_skills · get_courses · get_projects · get_contact",
            "",
            "INFRASTRUCTURE",
            "• Python 3.10+  ·  Plotly  ·  Pandas  ·  python-dotenv",
            "• Developed with IBM Bob (AI-assisted development)",
        ],
    ),
    # 6 — Outro (20 s)
    dict(
        duration=20, tag="Connect",
        title="Let's Build the Future",
        subtitle="Reach out for training, collaboration, or a conversation",
        accent=ACCENT_BLUE,
        body=[
            "Email      vignesh@example.com",
            "LinkedIn   linkedin.com/in/vignesh",
            "GitHub     github.com/vignesh2396",
            "Location   India",
            "",
            '"From zero to building your own ReAct agent in three days."',
            "                                         — Meera K., IIT",
            "",
            '"Quantum Computing workshop opened a completely new',
            ' dimension for my research."',
            "                                 — Arjun R., ML Engineer, TCS",
        ],
    ),
]


# ── Frame builder ──────────────────────────────────────────────────────────────
def build_frames() -> list:
    """
    Pre-render every frame (at FPS) for all slides + cross-dissolve transitions.
    Returns a flat list of (H, W, 3) uint8 arrays.
    """
    durations  = [s["duration"] for s in SLIDES]
    total_dur  = sum(durations)
    cumulative = 0.0
    frames     = []

    print(f"Pre-rendering {total_dur}s video at {FPS} fps …")

    for idx, slide in enumerate(SLIDES):
        dur   = slide["duration"]
        n_f   = int(dur * FPS)
        sp    = cumulative / total_dur
        ep    = (cumulative + dur) / total_dur
        rc    = slide.get("right_col")

        prev_last = frames[-1] if frames else None

        for fi in range(n_f):
            t    = fi / max(n_f - 1, 1)
            prog = sp + (ep - sp) * t
            frame = render_slide(
                title    = slide["title"],
                body     = slide["body"],
                accent   = slide["accent"],
                subtitle = slide.get("subtitle", ""),
                tag      = slide.get("tag", ""),
                progress = prog,
                right_col= rc,
            )

            # Cross-dissolve at the very start of this slide
            if prev_last is not None and fi < int(TRANS * FPS):
                alpha = fi / max(int(TRANS * FPS) - 1, 1)
                frame = (prev_last * (1 - alpha) + frame * alpha).astype(np.uint8)

            frames.append(frame)

        cumulative += dur
        pct = int(cumulative / total_dur * 100)
        print(f"  Slide {idx+1}/{len(SLIDES)} done  ({pct}%)")

    return frames


# ── Main ───────────────────────────────────────────────────────────────────────
def main():
    frames = build_frames()
    print(f"\nTotal frames: {len(frames)}  ({len(frames)/FPS:.1f} s)")
    print(f"Writing → {OUTPUT_FILE}\n")

    clip = ImageSequenceClip(frames, fps=FPS)

    # gentle fade-in / fade-out on first and last ~1 s
    fade_f = FPS
    for i in range(min(fade_f, len(frames))):
        alpha = i / fade_f
        frames[i] = (frames[i] * alpha).astype(np.uint8)
    for i in range(1, min(fade_f + 1, len(frames))):
        alpha = i / fade_f
        frames[-i] = (frames[-i] * alpha).astype(np.uint8)

    clip = ImageSequenceClip(frames, fps=FPS)   # rebuild after fade edits
    clip.write_videofile(
        OUTPUT_FILE,
        fps=FPS,
        codec="libx264",
        audio=False,
        preset="fast",
        ffmpeg_params=["-crf", "22", "-pix_fmt", "yuv420p"],
        logger="bar",
    )
    print(f"\n✅  Done!  Saved to:\n    {OUTPUT_FILE}\n")


if __name__ == "__main__":
    main()
