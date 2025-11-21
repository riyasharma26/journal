# app.py
import streamlit as st
from datetime import datetime
from typing import List, Dict

# -----------------------------
# Configuration / constants
# -----------------------------
PAGE_TITLE = "Moonlit Journal"
PAGE_ICON = "🌙"
FIREPLACE_URL = (
    "https://cdn.pixabay.com/download/audio/2021/12/15/audio_9e2866ae5d.mp3"
)
CLICK_SOUND_URL = (
    "https://cdn.pixabay.com/download/audio/2022/10/21/audio_4f7d4e5aef.mp3"
)
SPARKLE_INTERVAL_MS = 700  # how often a sparkle is created

# -----------------------------
# Utility / rendering helpers
# -----------------------------
def configure_page() -> None:
    st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="centered")


def render_global_css() -> None:
    """
    Centralized CSS for the notebook aesthetic and accessibility/contrast improvements.
    """
    st.markdown(
        """
        <style>
        :root{
            --bg-deep: #1e1a22;
            --paper: #faf7f0;
            --paper-accent: #fdf8f2;
            --text-dark: #2b2b2b;
            --accent: #c9a98d;
            --accent-dark: #b99880;
        }

        /* Page background */
        html, body, #root > div {
            background: var(--bg-deep) !important;
        }

        /* Notebook container */
        .notebook {
            max-width: 820px;
            margin: 20px auto 40px;
            padding: 22px;
            border-radius: 16px;
            background: linear-gradient(180deg, var(--paper) 0%, #fff 100%);
            box-shadow: 0 10px 30px rgba(0,0,0,0.55);
            border: 1px solid rgba(255,255,255,0.04);
        }

        /* Lined paper effect for the input and entries */
        .paper-lines {
            background: repeating-linear-gradient(
                to bottom,
                var(--paper-accent) 0px,
                var(--paper-accent) 28px,
                #f1e7dd 29px
            );
            border-radius: 12px;
            border: 2px solid #d8c6b8;
            padding: 14px;
            color: var(--text-dark);
        }

        /* Stronger text contrast */
        .paper-lines, .paper-lines p, .paper-lines span, .paper-lines li {
            color: var(--text-dark) !important;
            font-family: Georgia, 'Times New Roman', serif;
            font-weight: 500;
        }

        /* Streamlit-specific element adjustments */
        .stTextArea>div>div>textarea, .stTextInput>div>input {
            background: rgba(255,255,255,0.87) !important;
            color: var(--text-dark) !important;
            font-family: Georgia, serif !important;
        }

        /* Buttons */
        .stButton>button {
            background-color: var(--accent);
            color: #3e2c26;
            border-radius: 10px;
            padding: 8px 14px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.3);
            border: none;
        }
        .stButton>button:hover { background-color: var(--accent-dark); }

        /* Entry card */
        .entry {
            margin-bottom: 12px;
            padding: 12px;
            border-radius: 12px;
        }

        /* Sparkles (base) */
        @keyframes floatUp {
            0% { transform: translateY(0) scale(1); opacity: 1; }
            100% { transform: translateY(-160px) scale(0.6); opacity: 0; }
        }
        .sparkle {
            position: fixed;
            width: 6px;
            height: 6px;
            background: radial-gradient(circle, #fff8e6, #ffe2a8);
            border-radius: 50%;
            animation: floatUp 3.2s ease-in-out forwards;
            pointer-events: none;
            z-index: 99999;
            filter: drop-shadow(0 0 6px rgba(255,200,150,0.6));
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_header() -> None:
    st.markdown("<div class='notebook'><h1 style='margin:0'>🌙 Moonlit Fireplace Journal</h1>"
                "<p style='margin-top:6px; margin-bottom:12px; color:#e6dccc'>A warm, lined notebook for quiet thoughts.</p>",
                unsafe_allow_html=True)


def render_footer_wrapper_close() -> None:
    st.markdown("</div>", unsafe_allow_html=True)


def render_audio_controls() -> None:
    """
    Provide a user-visible control that starts the ambient fireplace.
    Clicking the Streamlit button satisfies the browser's user-gesture requirement
    and allows an audio element with autoplay to begin.
    """
    if "ambience_playing" not in st.session_state:
        st.session_state["ambience_playing"] = False

    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button("▶ Play Ambience"):
            # Setting this flag will render an autoplaying audio element below
            st.session_state["ambience_playing"] = True

        if st.button("⏸ Pause Ambience"):
            st.session_state["ambience_playing"] = False

    with col2:
        st.markdown(
            "<div style='color:#f2e9d8; font-family:Georgia; padding-top:6px;'>Tip: click Play Ambience once to enable fireplace and click sounds.</div>",
            unsafe_allow_html=True,
        )

    # If the user clicked Play Ambience, render a (hidden) autoplay audio element.
    if st.session_state.get("ambience_playing", False):
        # Render audio tag with autoplay — allowed because user gesture occurred on the Play button.
        st.markdown(
            f"""
            <audio id="__moonlit_ambience" autoplay loop style="display:none">
                <source src="{FIREPLACE_URL}" type="audio/mpeg">
            </audio>
            """,
            unsafe_allow_html=True,
        )


def inject_client_js() -> None:
    """
    Inject small JS to: (a) create sparkles, (b) play a short click sound when the user interacts with
    meaningful UI elements (buttons / textareas). This JS is intentionally scoped and minimal.
    """
    st.components.v1.html(
        f"""
        <div></div>
        <script>
        (() => {{
            const CLICK_SOUND = "{CLICK_SOUND_URL}";
            const SPARKLE_INTERVAL = {SPARKLE_INTERVAL_MS};

            // Create a single Audio object for click to avoid overlapping downloads.
            const clickAudio = new Audio(CLICK_SOUND);
            clickAudio.volume = 0.22;
            clickAudio.preload = "auto";

            // Play click sound only when clicking on an interactive element.
            document.addEventListener('click', (e) => {{
                // only play for visible controls: buttons & textareas & inputs
                const tag = e.target.tagName.toLowerCase();
                if (tag === 'button' || tag === 'textarea' || tag === 'input') {{
                    try {{ clickAudio.currentTime = 0; }} catch(err){{}} // reset
                    clickAudio.play().catch(()=>{{/* ignore playback errors */}});
                }}
            }}, true);

            // Sparkle generator (gentle)
            function createSparkle() {{
                const s = document.createElement('div');
                s.className = 'sparkle';
                s.style.left = Math.random() * (window.innerWidth - 30) + 'px';
                s.style.top = (window.innerHeight - 10) + 'px';
                s.style.opacity = (0.5 + Math.random() * 0.8).toString();
                // randomize duration slightly
                const dur = 2800 + Math.random() * 1200;
                s.style.animationDuration = (dur / 1000) + 's';
                document.body.appendChild(s);
                setTimeout(() => s.remove(), dur + 200);
            }}

            // Gentle steady sparkles, avoids heavy CPU usage.
            let sparkleTimer = setInterval(createSparkle, SPARKLE_INTERVAL);

            // Pause sparkles when the document is hidden or when the user navigates away.
            document.addEventListener('visibilitychange', () => {{
                if (document.hidden) {{
                    clearInterval(sparkleTimer);
                }} else {{
                    sparkleTimer = setInterval(createSparkle, SPARKLE_INTERVAL);
                }}
            }});
        }})(); 
        </script>
        """,
        height=0,
        scrolling=False,
    )


# -----------------------------
# Data model + persistence (session)
# -----------------------------
def get_entries() -> List[Dict[str, str]]:
    if "entries" not in st.session_state:
        st.session_state["entries"] = []
    return st.session_state["entries"]


def save_entry(text: str) -> None:
    if not text.strip():
        return
    entries = get_entries()
    entries.append({"text": text.strip(), "date": datetime.now().astimezone().strftime("%b %d, %Y • %I:%M %p")})
    st.session_state["entries"] = entries


# -----------------------------
# UI pieces
# -----------------------------
def render_entry_input() -> None:
    st.markdown("<div class='paper-lines'>", unsafe_allow_html=True)
    text = st.text_area("", placeholder="Write under the moonlight...", height=220)
    col1, col2 = st.columns([1, 6])
    with col1:
        if st.button("Save"):
            if text.strip():
                save_entry(text)
                st.success("Saved — your entry has been added to the notebook.")
            else:
                st.error("Please write something before saving.")
    with col2:
        st.markdown("<div style='color:#6b5854; font-family:Georgia; padding-top:6px;'>Your notebook saves for this browser session.</div>",
                    unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


def render_entries() -> None:
    entries = get_entries()
    st.markdown("<div style='margin-top:18px;'>", unsafe_allow_html=True)
    if not entries:
        st.info("Your notebook is empty — the night is ready for your first thought ✨")
    else:
        # Render entries newest first
        for e in reversed(entries):
            safe_text = e["text"].replace("\n", "<br>")  # basic preservation of newlines
            st.markdown(
                f"""
                <div class="paper-lines entry">
                    <div style="font-size:13px; color:#6b5854; margin-bottom:6px;"><strong>📅 {e['date']}</strong></div>
                    <div style="font-size:15px; line-height:1.35; color:#2b2b2b;">{safe_text}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
    st.markdown("</div>", unsafe_allow_html=True)


# -----------------------------
# Main
# -----------------------------
def main() -> None:
    configure_page()
    render_global_css()
    render_header()
    render_audio_controls()
    inject_client_js()

    # Input + entries live inside the notebook container
    st.markdown("<div class='notebook'>", unsafe_allow_html=True)
    render_entry_input()
    st.markdown("---", unsafe_allow_html=True)
    st.markdown("<h3 style='margin-bottom:8px; color:#6b5854'>📔 Notebook Pages</h3>", unsafe_allow_html=True)
    render_entries()
    st.markdown("</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
