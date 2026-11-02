"""
Gemini-powered AI chat component.
Uses the new google-genai SDK (replaces deprecated google-generativeai).
Handles: Gemini client setup, ReAct agent loop, Streamlit chat UI.
"""
import os
import json
import re
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from data.profile import (
    AGENT_SYSTEM_PROMPT,
    GEMINI_MODEL_ID,
    GEMINI_PARAMS,
    NAME,
)
from components.agent_tools import TOOLS, TOOL_DESCRIPTIONS

# ── Gemini client (cached) ─────────────────────────────────────────────────────

@st.cache_resource(show_spinner=False)
def _get_client():
    """Initialise and return a Gemini client (cached across reruns)."""
    api_key = os.getenv("GEMINI_API_KEY", "")
    if not api_key:
        return None
    try:
        from google import genai
        client = genai.Client(api_key=api_key)
        return client
    except Exception as e:
        st.error(f"Gemini init error: {e}")
        return None


# ── ReAct agent loop ───────────────────────────────────────────────────────────

def _build_contents(history: list[dict], user_message: str) -> list[dict]:
    """Build a google-genai compatible contents list from conversation history."""
    contents = []
    for msg in history[-6:]:          # last 6 turns for context window
        role = "user" if msg["role"] == "user" else "model"
        contents.append({"role": role, "parts": [{"text": msg["content"]}]})
    contents.append({"role": "user", "parts": [{"text": user_message}]})
    return contents


def _parse_tool_call(text: str):
    """Check if the model output contains a tool call JSON block."""
    pattern = r'TOOL_CALL:\s*(\{.*\})'
    match = re.search(pattern, text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(1))
        except json.JSONDecodeError:
            pass
    return None


def _extract_text(response) -> str:
    """Safely extract text from a google-genai GenerateContentResponse."""
    if response is None:
        return ""
    # Fast path: .text property exists and is populated
    try:
        if response.text:
            return response.text.strip()
    except Exception:
        pass
    # Fallback: walk candidates → parts
    try:
        for candidate in (response.candidates or []):
            parts = getattr(getattr(candidate, "content", None), "parts", None) or []
            for part in parts:
                t = getattr(part, "text", None)
                if t:
                    return t.strip()
    except Exception:
        pass
    return ""


def _run_agent(client, user_message: str, history: list[dict]) -> str:
    """Single-turn ReAct agent: reason → optionally call a tool → respond."""
    from google.genai import types

    system_prompt = f"{AGENT_SYSTEM_PROMPT}\n\n{TOOL_DESCRIPTIONS}"
    contents = _build_contents(history, user_message)

    config = types.GenerateContentConfig(
        system_instruction=system_prompt,
        max_output_tokens=GEMINI_PARAMS["max_output_tokens"],
        temperature=GEMINI_PARAMS["temperature"],
        top_k=GEMINI_PARAMS["top_k"],
        top_p=GEMINI_PARAMS["top_p"],
    )

    try:
        response = client.models.generate_content(
            model=GEMINI_MODEL_ID,
            contents=contents,
            config=config,
        )
        text = _extract_text(response)

        # Check for tool call
        tool_call = _parse_tool_call(text)
        if tool_call:
            tool_name = tool_call.get("tool", "")
            tool_args = tool_call.get("args", {})
            if tool_name in TOOLS:
                tool_result = TOOLS[tool_name](**tool_args)
                # Second pass: inject tool result and ask for final answer
                contents.append({"role": "model", "parts": [{"text": text}]})
                contents.append({
                    "role": "user",
                    "parts": [{"text": f"Tool result:\n{tool_result}\n\nNow provide your final answer to the user."}]
                })
                final = client.models.generate_content(
                    model=GEMINI_MODEL_ID,
                    contents=contents,
                    config=config,
                )
                return _extract_text(final)

        # Remove any leftover TOOL_CALL artifacts
        text = re.sub(r'TOOL_CALL:\s*\{.*?\}', '', text, flags=re.DOTALL).strip()
        return text

    except Exception as e:
        return f"⚠️ I encountered an error: {e}. Please check your API credentials."


# ── Streamlit chat UI ─────────────────────────────────────────────────────────

def render_chat():
    """Render the full AI chat section inside a Streamlit page."""
    st.markdown("## 🤖 Ask the AI Assistant")
    st.markdown(
        f"Powered by **Google Gemini** · Ask me anything about {NAME}'s expertise, courses, or projects."
    )

    client = _get_client()

    # ── Setup warning if credentials missing ──────────────────────────────────
    if client is None:
        st.warning(
            "⚙️ **AI Assistant not configured.** "
            "Create a `.env` file in the project root with your Gemini API key:\n\n"
            "```\nGEMINI_API_KEY=your-gemini-api-key\n```\n\n"
            "Get a free API key at [aistudio.google.com](https://aistudio.google.com/app/apikey).",
            icon="🔑",
        )
        _render_demo_fallback()
        return

    # ── Session state ─────────────────────────────────────────────────────────
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
        st.session_state.chat_history.append({
            "role": "assistant",
            "content": (
                f"👋 Hello! I'm {NAME}'s AI assistant, powered by Google Gemini. "
                f"Ask me anything about his expertise, courses, or projects!"
            ),
        })

    # ── Display history ───────────────────────────────────────────────────────
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # ── Input ─────────────────────────────────────────────────────────────────
    if prompt := st.chat_input("Ask something, e.g. 'What courses does Vignesh offer?'"):
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Thinking…"):
                answer = _run_agent(
                    client, prompt,
                    st.session_state.chat_history[:-1],
                )
            st.markdown(answer)
            st.session_state.chat_history.append({"role": "assistant", "content": answer})

        _append_log(prompt, answer)

    # ── Clear button ──────────────────────────────────────────────────────────
    if st.button("🗑️ Clear conversation", key="clear_chat"):
        st.session_state.chat_history = []
        st.rerun()


def _render_demo_fallback():
    """Show a demo-mode chat when credentials are not set."""
    DEMO_ANSWERS = {
        "course": (
            "Vignesh offers 5 courses: Agentic AI Fundamentals to Advanced (3 days), "
            "Machine Learning Bootcamp (5 days), Quantum Computing with Qiskit (2 days), "
            "IBM watsonx.ai for Enterprise (1 day), and Python for Data Science & AI (4 days)."
        ),
        "skill": (
            "Vignesh's top skills span Agentic AI (IBM Granite, RAG, LangChain), "
            "Machine Learning (PyTorch, NLP, MLOps), and Quantum Computing (Qiskit, VQC)."
        ),
        "contact": "You can reach Vignesh at vignesh@example.com or via the Contact page.",
        "project": (
            "Vignesh's notable projects include an AI Portfolio Chatbot (Gemini + Streamlit), "
            "a Quantum-Enhanced Fraud Detection pipeline (Qiskit + Scikit-learn), "
            "and an enterprise RAG Knowledge Base."
        ),
    }
    DEFAULT = (
        "I'm running in demo mode (no API key configured). "
        "Try asking about 'courses', 'skills', 'contact', or 'projects'!"
    )

    if "demo_history" not in st.session_state:
        st.session_state.demo_history = [
            {"role": "assistant", "content": "👋 Demo mode — Gemini not connected. Ask me about Vignesh!"}
        ]

    for msg in st.session_state.demo_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Try: 'What courses does Vignesh offer?'", key="demo_input"):
        st.session_state.demo_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        p_lower = prompt.lower()
        answer = next((v for k, v in DEMO_ANSWERS.items() if k in p_lower), DEFAULT)
        st.session_state.demo_history.append({"role": "assistant", "content": answer})
        with st.chat_message("assistant"):
            st.markdown(answer)


def _append_log(question: str, answer: str):
    """Append a Q&A pair to the local chat log CSV."""
    import csv, pathlib
    from datetime import datetime
    log_dir = pathlib.Path("logs")
    log_dir.mkdir(exist_ok=True)
    log_file = log_dir / "chat_log.csv"
    write_header = not log_file.exists()
    with open(log_file, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(["timestamp", "question", "answer"])
        writer.writerow([datetime.utcnow().isoformat(), question, answer])
