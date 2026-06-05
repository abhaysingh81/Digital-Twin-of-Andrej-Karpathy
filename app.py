"""
SECTION 5: INTERACTIVE DEMO — app.py
Run with: streamlit run app.py

Full Karpathy Digital Twin chat interface with:
  - Streaming responses
  - Memory dashboard sidebar
  - Source citations display
  - Session controls
  - Timeline indicator
"""

import os
import sys
import time
import json
from pathlib import Path
import re
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

# ── Path setup ────────────────────────────────────────────
ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))

# ══════════════════════════════════════════════════════════
# PAGE CONFIG (must be first Streamlit call)
# ══════════════════════════════════════════════════════════
st.set_page_config(
    page_title="Andrej Karpathy — Digital Twin",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ══════════════════════════════════════════════════════════
# CUSTOM CSS — dark terminal aesthetic with amber accents
# ══════════════════════════════════════════════════════════
st.markdown("""
<style>
/* ── Font import ── */
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;600&family=Space+Grotesk:wght@300;400;500;600&display=swap');

/* ── Root variables ── */
:root {
    --bg-primary:    #0d1117;
    --bg-secondary:  #161b22;
    --bg-tertiary:   #21262d;
    --amber:         #f0a500;
    --amber-dim:     #a37000;
    --green:         #3fb950;
    --blue:          #58a6ff;
    --text-primary:  #e6edf3;
    --text-muted:    #8b949e;
    --border:        #30363d;
    --user-bg:       #1c2128;
    --bot-bg:        #161b22;
    --code-bg:       #0d1117;
    --radius:        8px;
}

/* ── Global reset ── */
html, body, .main, [data-testid="stAppViewContainer"] {
    background-color: var(--bg-primary) !important;
    color: var(--text-primary) !important;
    font-family: 'Space Grotesk', sans-serif !important;
}

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
[data-testid="stToolbar"] { display: none; }

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background-color: var(--bg-secondary) !important;
    border-right: 1px solid var(--border) !important;
}
[data-testid="stSidebar"] * { color: var(--text-primary) !important; }

/* ── Title area ── */
.karpathy-header {
    display: flex;
    align-items: center;
    gap: 14px;
    padding: 18px 0 10px 0;
    border-bottom: 1px solid var(--border);
    margin-bottom: 20px;
}
.karpathy-avatar {
    width: 52px;
    height: 52px;
    border-radius: 50%;
    background: linear-gradient(135deg, var(--amber) 0%, #e05800 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 26px;
    flex-shrink: 0;
    box-shadow: 0 0 16px rgba(240,165,0,0.3);
}
.karpathy-title h1 {
    margin: 0;
    font-size: 1.4rem;
    font-weight: 600;
    color: var(--amber) !important;
    font-family: 'JetBrains Mono', monospace !important;
}
.karpathy-title p {
    margin: 2px 0 0 0;
    font-size: 0.78rem;
    color: var(--text-muted) !important;
    font-family: 'JetBrains Mono', monospace !important;
}

/* ── Timeline badge ── */
.timeline-badge {
    display: inline-block;
    background: var(--bg-tertiary);
    border: 1px solid var(--amber-dim);
    border-radius: 20px;
    padding: 3px 12px;
    font-size: 0.72rem;
    font-family: 'JetBrains Mono', monospace;
    color: var(--amber) !important;
    margin-bottom: 12px;
}

/* ── Chat messages ── */
.chat-container {
    max-height: 65vh;
    overflow-y: auto;
    padding: 8px 0;
    scrollbar-width: thin;
    scrollbar-color: var(--border) transparent;
}

.message-wrapper {
    display: flex;
    flex-direction: column;
    gap: 4px;
    margin-bottom: 20px;
    animation: fadeSlideIn 0.25s ease-out;
}

@keyframes fadeSlideIn {
    from { opacity: 0; transform: translateY(8px); }
    to   { opacity: 1; transform: translateY(0); }
}

.message-header {
    font-size: 0.72rem;
    font-family: 'JetBrains Mono', monospace;
    color: var(--text-muted) !important;
    padding: 0 4px;
}
.message-header.user-header { color: var(--blue) !important; }
.message-header.bot-header  { color: var(--amber) !important; }

.message-bubble {
    border-radius: var(--radius);
    padding: 14px 18px;
    line-height: 1.65;
    font-size: 0.94rem;
    max-width: 100%;
    white-space: pre-wrap;
    word-break: break-word;
}

.user-bubble {
    background: var(--user-bg);
    border: 1px solid var(--border);
    border-left: 3px solid var(--blue);
    color: var(--text-primary) !important;
}

.bot-bubble {
    background: var(--bot-bg);
    border: 1px solid var(--border);
    border-left: 3px solid var(--amber);
    color: var(--text-primary) !important;
}

/* ── Code blocks inside messages ── */
.message-bubble code {
    background: var(--code-bg);
    border: 1px solid var(--border);
    border-radius: 4px;
    padding: 0 4px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.85rem;
    color: var(--green) !important;
}

.message-bubble pre {
    background: var(--code-bg) !important;
    border: 1px solid var(--border);
    border-left: 3px solid var(--amber-dim);
    border-radius: var(--radius);
    padding: 14px;
    overflow-x: auto;
    margin: 12px 0;
}

.message-bubble pre code {
    background: none;
    border: none;
    padding: 0;
    font-size: 0.82rem;
    color: #e2c08d !important;
}

/* ── Citation chips ── */
.citation-chip {
    display: inline-block;
    background: rgba(240,165,0,0.08);
    border: 1px solid var(--amber-dim);
    border-radius: 4px;
    padding: 1px 8px;
    font-size: 0.72rem;
    font-family: 'JetBrains Mono', monospace;
    color: var(--amber) !important;
    margin: 2px 3px;
}

/* ── Input area ── */
.stTextInput input, [data-testid="stChatInput"] textarea {
    background-color: var(--bg-tertiary) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius) !important;
    color: var(--text-primary) !important;
    font-family: 'Space Grotesk', sans-serif !important;
    caret-color: var(--amber) !important;
}
.stTextInput input:focus, [data-testid="stChatInput"] textarea:focus {
    border-color: var(--amber) !important;
    box-shadow: 0 0 0 2px rgba(240,165,0,0.15) !important;
    outline: none !important;
}

/* ── Buttons ── */
.stButton > button {
    background-color: var(--bg-tertiary) !important;
    border: 1px solid var(--border) !important;
    color: var(--text-primary) !important;
    border-radius: var(--radius) !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 0.82rem;
    transition: all 0.15s;
}
.stButton > button:hover {
    border-color: var(--amber) !important;
    color: var(--amber) !important;
}

/* ── Memory dashboard cards ── */
.mem-card {
    background: var(--bg-tertiary);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 12px 14px;
    margin-bottom: 10px;
}
.mem-card-title {
    font-size: 0.72rem;
    font-family: 'JetBrains Mono', monospace;
    color: var(--amber) !important;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 6px;
}
.mem-fact {
    font-size: 0.8rem;
    color: var(--text-muted) !important;
    padding: 3px 0;
    border-bottom: 1px solid rgba(48,54,61,0.5);
    line-height: 1.4;
}
.mem-fact:last-child { border-bottom: none; }

/* ── Metric boxes ── */
.metric-row {
    display: flex;
    gap: 8px;
    margin-bottom: 12px;
}
.metric-box {
    flex: 1;
    background: var(--bg-tertiary);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 10px;
    text-align: center;
}
.metric-value {
    font-size: 1.4rem;
    font-weight: 600;
    color: var(--amber) !important;
    font-family: 'JetBrains Mono', monospace;
}
.metric-label {
    font-size: 0.65rem;
    color: var(--text-muted) !important;
    text-transform: uppercase;
    letter-spacing: 0.06em;
}

/* ── Dividers ── */
hr { border-color: var(--border) !important; margin: 16px 0; }

/* ── Status dots ── */
.status-dot {
    width: 8px; height: 8px;
    border-radius: 50%;
    display: inline-block;
    margin-right: 6px;
    animation: pulse 2s infinite;
}
.status-dot.green  { background: var(--green); }
.status-dot.amber  { background: var(--amber); }
@keyframes pulse {
    0%,100% { opacity: 1; }
    50%      { opacity: 0.4; }
}

/* ── Spinner override ── */
[data-testid="stSpinner"] { color: var(--amber) !important; }

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--border); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: var(--amber-dim); }
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════
# IMPORTS (after path setup)
# ══════════════════════════════════════════════════════════
try:
    from core.agent import KarpathyAgent
    from rag.pipeline import CAREER_PHASES, detect_career_phase
    AGENT_AVAILABLE = True
except ImportError as e:
    AGENT_AVAILABLE = False
    IMPORT_ERROR = str(e)

# ══════════════════════════════════════════════════════════
# SESSION STATE INIT
# ══════════════════════════════════════════════════════════
def init_state():
    defaults = {
        "messages":        [],       # list of {role, content, timestamp}
        "agent":           None,
        "api_key_set":     False,
        "last_phase":      "general",
        "total_turns":     0,
        "facts_learned":   0,
        "rag_chunks":      0,
        "show_dashboard":  False,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()

# ══════════════════════════════════════════════════════════
# HELPER FUNCTIONS
# ══════════════════════════════════════════════════════════

PHASE_LABELS = {
    "stanford":   "🎓 Stanford Era (2011–2015)",
    "openai_v1":  "🔬 OpenAI v1 (2015–2017)",
    "tesla":      "🚗 Tesla Autopilot (2017–2022)",
    "openai_v2":  "⚡ OpenAI v2 / LLMs (2022–2023)",
    "eureka":     "🌟 Eureka Labs (2024–present)",
    "general":    "🧠 General Knowledge",
}

def phase_label(phase: str) -> str:
    return PHASE_LABELS.get(phase, "🧠 General")

def extract_citations(text: str) -> list[str]:
    """Pull [Source: ...] patterns from response text."""
    return re.findall(r'\[Source:[^\]]+\]', text)

def render_message(role: str, content: str, timestamp: str = ""):
    """Render a single chat message with citations highlighted."""
    if role == "user":
        header_class = "user-header"
        bubble_class = "user-bubble"
        name = "You"
        icon = "👤"
    else:
        header_class = "bot-header"
        bubble_class = "bot-bubble"
        name = "Andrej Karpathy"
        icon = "🧠"

    citations = extract_citations(content)
    display_content = content
    for cit in citations:
        display_content = display_content.replace(
            cit,
            f'<span class="citation-chip">{cit}</span>'
        )

    st.markdown(f"""
    <div class="message-wrapper">
        <div class="message-header {header_class}">{icon} {name} {f'· {timestamp}' if timestamp else ''}</div>
        <div class="message-bubble {bubble_class}">{display_content}</div>
    </div>
    """, unsafe_allow_html=True)

def render_memory_dashboard(agent: KarpathyAgent):
    """Render the memory visualization in the sidebar."""
    dashboard = agent.get_memory_dashboard()
    mem = dashboard["memory"]
    rag = dashboard["rag"]

    # Metrics
    lt_facts = mem["long_term"]["total_facts"]
    st_turns = mem["short_term"]["turns"]
    rag_chunks = rag["total_chunks"]

    st.markdown(f"""
    <div class="metric-row">
        <div class="metric-box">
            <div class="metric-value">{lt_facts}</div>
            <div class="metric-label">User Facts</div>
        </div>
        <div class="metric-box">
            <div class="metric-value">{st_turns}</div>
            <div class="metric-label">Session Turns</div>
        </div>
        <div class="metric-box">
            <div class="metric-value">{rag_chunks}</div>
            <div class="metric-label">RAG Chunks</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Long-term facts by category
    by_cat = mem["long_term"].get("by_category", {})
    cat_icons = {
        "background":      "🧬",
        "goal":            "🎯",
        "project":         "🔨",
        "struggle":        "⚠️",
        "preference":      "⚙️",
        "knowledge_level": "📊",
    }

    if by_cat:
        st.markdown("**Long-Term Memory**")
        for cat, facts in by_cat.items():
            icon = cat_icons.get(cat, "📌")
            facts_html = "".join(
                f'<div class="mem-fact">• {f["content"]}</div>'
                for f in facts[:4]  # show max 4 per category
            )
            st.markdown(f"""
            <div class="mem-card">
                <div class="mem-card-title">{icon} {cat.replace("_", " ").title()}</div>
                {facts_html}
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="mem-card">
            <div class="mem-card-title">💡 Long-Term Memory</div>
            <div class="mem-fact">No user facts extracted yet.<br>
            Tell me about your background or what you're building!</div>
        </div>
        """, unsafe_allow_html=True)

    # Recent conversation preview
    recent = mem["short_term"]["recent_preview"]
    if recent:
        with st.expander("📼 Recent Conversation"):
            st.code(recent, language=None)


# ══════════════════════════════════════════════════════════
# SIDEBAR
# ══════════════════════════════════════════════════════════

with st.sidebar:
    # Header
    st.markdown("""
    <div style="text-align:center; padding: 8px 0 16px 0;">
        <div style="font-size:2.2rem; margin-bottom:4px;">🧠</div>
        <div style="font-family:'JetBrains Mono',monospace; font-size:0.9rem;
                    color:#f0a500; font-weight:600;">KARPATHY TWIN</div>
        <div style="font-size:0.68rem; color:#8b949e; font-family:'JetBrains Mono',monospace;">
            Powered by Gemini 2.5 Flash</div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # API Key input
    api_key = st.text_input(
        "Google API Key",
        value=os.environ.get("GOOGLE_API_KEY", ""),
        type="password",
        placeholder="AIza...",
        help="Get your key at https://aistudio.google.com/",
    )

    # Initialize agent
    if api_key and not st.session_state.api_key_set:
        with st.spinner("🔧 Initializing Twin..."):
            try:
                st.session_state.agent = KarpathyAgent(
                    google_api_key=api_key,
                    chroma_persist_dir=str(ROOT / "data" / "chromadb"),
                    profile_path=str(ROOT / "data" / "memory" / "user_profile.json"),
                    bootstrap_demo=True,
                )
                st.session_state.api_key_set = True
                st.session_state.rag_chunks = st.session_state.agent.get_rag_stats()["total_chunks"]
                st.success("✓ Twin initialized!")
            except Exception as e:
                st.error(f"Init failed: {e}")

    st.divider()

    # Status
    if st.session_state.api_key_set:
        st.markdown(f"""
        <div style="font-size:0.78rem; color:#8b949e; font-family:'JetBrains Mono',monospace;">
            <span class="status-dot green"></span>ONLINE &nbsp;|&nbsp;
            <span style="color:#f0a500;">Gemini 2.5 Flash</span>
        </div>
        <div style="font-size:0.72rem; color:#8b949e; margin-top:4px;">
            📚 {st.session_state.rag_chunks} knowledge chunks indexed
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="font-size:0.78rem; color:#8b949e; font-family:'JetBrains Mono',monospace;">
            <span class="status-dot amber"></span>AWAITING API KEY
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # Memory Dashboard
    st.markdown("### 🗃️ Memory Dashboard")
    if st.session_state.api_key_set and st.session_state.agent:
        render_memory_dashboard(st.session_state.agent)
    else:
        st.caption("Connect your API key to see memory state.")

    st.divider()

    # Controls
    st.markdown("### ⚙️ Controls")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 New Session", use_container_width=True):
            if st.session_state.agent:
                st.session_state.agent.reset_session()
            st.session_state.messages = []
            st.session_state.last_phase = "general"
            st.session_state.total_turns = 0
            st.rerun()
    with col2:
        if st.button("🗑️ Clear Memory", use_container_width=True):
            if st.session_state.agent:
                st.session_state.agent.memory.clear_all()
            st.session_state.messages = []
            st.rerun()

    st.divider()

    # Suggested prompts
    st.markdown("### 💡 Try Asking")
    suggestions = [
        "Explain backpropagation from scratch",
        "How did Tesla's Autopilot perception stack work?",
        "What is Software 2.0?",
        "Walk me through the attention mechanism",
        "What's your advice for training neural nets?",
        "Tell me about nanoGPT",
    ]
    for prompt in suggestions:
        if st.button(f"› {prompt}", use_container_width=True, key=f"sug_{prompt[:20]}"):
            st.session_state["injected_prompt"] = prompt
            st.rerun()


# ══════════════════════════════════════════════════════════
# MAIN CONTENT
# ══════════════════════════════════════════════════════════

# Header
st.markdown("""
<div class="karpathy-header">
    <div class="karpathy-avatar">🧠</div>
    <div class="karpathy-title">
        <h1>Andrej Karpathy</h1>
        <p>Digital Twin · AI Researcher · Educator · Former Tesla AI Director & OpenAI Scientist</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Timeline badge
phase_text = phase_label(st.session_state.last_phase)
st.markdown(f'<div class="timeline-badge">🕐 Active Era: {phase_text}</div>', unsafe_allow_html=True)

# ── Welcome message ─────────────────────────────────────
if not st.session_state.messages:
    with st.chat_message("assistant", avatar="🧠"):
        welcome = (
            "Hey! I'm Andrej Karpathy — or at least, a pretty faithful digital twin of me. "
            "I'm here to talk deep learning, neural networks, LLMs, backprop, "
            "the whole stack — from scratch if needed.\n\n"
            "Fair warning: I'm going to go deep. I believe the best way to "
            "understand something is to build it yourself. So if you ask me "
            "how attention works, I'm probably going to end up writing some PyTorch.\n\n"
            "What are you working on? What do you want to understand today?"
        )
        st.write(welcome)
        st.session_state.messages.append({
            "role": "assistant",
            "content": welcome,
            "timestamp": time.strftime("%H:%M"),
        })

# ── Render conversation history ──────────────────────────
for msg in st.session_state.messages[1:]:  # skip welcome (already rendered above)
    avatar = "🧠" if msg["role"] == "assistant" else "👤"
    with st.chat_message(msg["role"], avatar=avatar):
        content = msg["content"]
        citations = extract_citations(content)
        display = content
        for cit in citations:
            display = display.replace(
                cit,
                f'`{cit}`'
            )
        st.markdown(display)

# ── Handle injected prompt (from sidebar buttons) ────────
injected = st.session_state.pop("injected_prompt", None)

# ── Chat input ───────────────────────────────────────────
prompt = st.chat_input(
    "Ask Karpathy anything about neural networks, LLMs, backprop, or AI...",
    disabled=not st.session_state.api_key_set,
) or injected

if prompt:
    if not st.session_state.api_key_set or not st.session_state.agent:
        st.warning("⚠️ Please enter your Google API Key in the sidebar to start chatting.")
        st.stop()

    # ── Show user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt,
        "timestamp": time.strftime("%H:%M"),
    })
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    # ── Detect timeline phase for badge
    phase = detect_career_phase(prompt)
    st.session_state.last_phase = phase

    # ── Stream response
    with st.chat_message("assistant", avatar="🧠"):
        message_placeholder = st.empty()
        full_response = ""
        thinking_placeholder = st.empty()
        thinking_placeholder.markdown(
            "<span style='color:#8b949e; font-family:JetBrains Mono; font-size:0.8rem;'>"
            "⟳ thinking...</span>",
            unsafe_allow_html=True
        )
        try:
            for chunk in st.session_state.agent.chat_stream(prompt):
                full_response += chunk
                # Format citations inline
                display = full_response
                citations = extract_citations(display)
                for cit in citations:
                    display = display.replace(cit, f'`{cit}`')
                thinking_placeholder.empty()
                message_placeholder.markdown(display + "▌")

            # Final render without cursor
            display = full_response
            citations = extract_citations(display)
            for cit in citations:
                display = display.replace(cit, f'`{cit}`')
            message_placeholder.markdown(display)

        except Exception as e:
            thinking_placeholder.empty()
            error_msg = (
                f"⚠️ Something went sideways: `{e}`\n\n"
                "Check your API key and make sure Gemini 2.5 Flash is accessible."
            )
            message_placeholder.markdown(error_msg)
            full_response = error_msg

    # ── Persist to state
    st.session_state.messages.append({
        "role": "assistant",
        "content": full_response,
        "timestamp": time.strftime("%H:%M"),
    })
    st.session_state.total_turns += 1

    # ── Update sidebar metrics
    if st.session_state.agent:
        viz = st.session_state.agent.memory.get_visualization()
        st.session_state.facts_learned = viz["long_term"]["total_facts"]

    st.rerun()

# ── Footer ───────────────────────────────────────────────
st.markdown("""
<div style="text-align:center; padding:20px 0 8px 0;
            font-size:0.68rem; color:#30363d;
            font-family:'JetBrains Mono',monospace;">
    Digital Twin of Andrej Karpathy · AIMS DTU Summer Project 2026 ·
    <span style="color:#f0a500;">Gemini 2.5 Flash</span> · RAG + Dual-Layer Memory
</div>
""", unsafe_allow_html=True)
