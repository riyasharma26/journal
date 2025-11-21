import streamlit as st
from datetime import datetime

# -------------------------------------------------
# FIXED VERSION — NO BROKEN UI, TEXT VISIBLE, SOUNDS WORKING,
# FLOATING SPARKLES INCLUDED, NO RAW CODE ON SCREEN
# -------------------------------------------------

st.set_page_config(page_title="Moonlit Journal 🌙", page_icon="🌙", layout="centered")

# -------------------------------------------------
# SAFE + CLEAN CSS (NO BROKEN TAGS)
# -------------------------------------------------
st.markdown(
    """
    <style>
        body {
            background-color: #1e1a22;
        }
        .main {
            background-color: #1e1a22 !important;
        }

        h1, h2, h3, h4, h5, h6, p, label {
            font-family: 'Georgia', serif;
            color: #f2e9d8;
        }

        /* Notebook background */
        .notebook-box, textarea {
            background: repeating-linear-gradient(
                to bottom,
                #fdf8f2 0px,
                #fdf8f2 28px,
                #f1e7dd 29px
            );
            border-radius: 12px;
            border: 2px solid #d8c6b8 !important;
            font-family: 'Georgia', serif !important;
            color: #4c3a32 !important;
        }

        textarea {
            padding: 12px !important;
        }

        /* Button */
        .stButton>button {
            background-color: #c9a98d;
            color: #3e2c26;
            font-family: 'Georgia', serif;
            border-radius: 12px;
            padding: 0.7rem 1.3rem;
            border: none;
            box-shadow: 0 2px 6px rgba(0,0,0,0.4);
        }
        .stButton>button:hover {
            background-color: #b99880;
        }

        /* Entry box */
        .entry-box {
            background: repeating-linear-gradient(
                to bottom,
                #fdf8f2 0px,
                #fdf8f2 28px,
                #f1e7dd 29px
            );
            padding: 1.2rem;
            border-radius: 16px;
            border: 2px solid #d8c6b8;
            margin-bottom: 1rem;
            box-shadow: 0 3px 12px rgba(0,0,0,0.35);
            color: #4c3a32;
        }

        /* Sparkles */
        @keyframes floatUp {
            0% {transform: translateY(0); opacity: 1;}
            100% {transform: translateY(-140px); opacity: 0;}
        }
        .sparkle {
            position: fixed;
            width: 6px;
            height: 6px;
            background: radial-gradient(circle, #fff8e6, #ffe2a8);
            border-radius: 50%;
            animation: floatUp 3s ease-in-out infinite;
            pointer-events: none;
            z-index: 99999;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------------------------------------
# AUDIO + SPARKLES JS (SAFE + FIXED)
# -------------------------------------------------
st.markdown(
    """
    <script>
        // Floating sparkles
        function createSparkle() {
            const s = document.createElement('div');
            s.classList.add('sparkle');
            s.style.left = Math.random() * window.innerWidth + 'px';
            s.style.top = (window.innerHeight - 10) + 'px';
            s.style.animationDuration = (2 + Math.random() * 2) + 's';
            document.body.appendChild(s);
            setTimeout(() => s.remove(), 3500);
        }
        setInterval(createSparkle, 650);

        // Click sound (allowed because user interacts)
        document.addEventListener('click', function() {
            var click = new Audio('https://cdn.pixabay.com/download/audio/2022/10/21/audio_4f7d4e5aef.mp3?filename=pop-124454.mp3');
            click.volume = 0.25;
            click.play();
        });
    </script>
    """,
    unsafe_allow_html=True,
)

# -------------------------------------------------
# TITLE
# -------------------------------------------------
st.markdown("# 🌙 Moonlit Fireplace Journal ✨")
st.markdown("### A warm, glowing notebook for nighttime reflections.")

# -------------------------------------------------
# MANUAL FIREPLACE AUDIO (AUTOPLAY BLOCKED BY BROWSERS)
# -------------------------------------------------
st.markdown(
    """
    <p style='color:#f2e9d8; font-family:Georgia;'>🎧 Click play for fireplace ambience:</p>
    <audio controls loop style="width:100%; border-radius:10px;">
        <source src="https://cdn.pixabay.com/download/audio/2021/12/15/audio_9e2866ae5d.mp3?filename=fireplace-crackle-96216.mp3" type="audio/mpeg">
    </audio>
    """,
    unsafe_allow_html=True,
)

# -------------------------------------------------
# STATE
# -------------------------------------------------
if "entries" not in st.session_state:
    st.session_state.entries = []

# -------------------------------------------------
# NEW ENTRY
# -------------------------------------------------
st.markdown("## 📝 New Entry")
entry_text = st.text_area("", placeholder="Write under the moonlight...", height=240)

if st.button("Save Entry ✨"):
    if entry_text.strip():
        st.session_state.entries.append({
            "text": entry_text,
            "date": datetime.now().astimezone().strftime("%b %d, %Y • %I:%M %p")
        })
        st.success("Saved ✨ Your words glow beautifully in the night.")
    else:
        st.error("Write something first 💛")

# -------------------------------------------------
# ENTRIES
# -------------------------------------------------
st.markdown("---")
st.markdown("## 📔 Notebook Pages")

if not st.session_state.entries:
    st.info("Your notebook awaits its first moonlit thought ✨")
else:
    for entry in reversed(st.session_state.entries):
        st.markdown(
            f"""
            <div class='entry-box'>
                <p><strong>📅 {entry['date']}</strong></p>
                <p>{entry['text']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
