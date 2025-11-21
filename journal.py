import streamlit as st
from datetime import datetime

# -------------------------------------------------
# MOON + FIREPLACE VIBE • COZY NOTEBOOK THEME
# -------------------------------------------------
st.set_page_config(page_title="Moonlit Journal 🌙", page_icon="🌙", layout="centered")

# CSS + AUDIO + NOTEBOOK LINES
st.markdown(
    """
    <style>
        body {
            background-color: #1e1a22; /* deep moonlit purple */
        }
        .main {
            background-color: #1e1a22 !important;
        }

        /* Soft warm text */
        h1, h2, h3, h4, h5, h6, p, label {
            font-family: 'Georgia', serif;
            color: #f2e9d8;
        }

        /* Notebook page background */
        .notebook {
            background: repeating-linear-gradient(
                to bottom,
                #fdf8f2 0px,
                #fdf8f2 28px,
                #f1e7dd 29px
            );
            border-radius: 18px;
            padding: 1.4rem;
            border: 2px solid #d8c6b8;
            box-shadow: 0 4px 14px rgba(0,0,0,0.4);
            margin-bottom: 1.2rem;
        }

        /* Textarea notebook style */
        textarea {
            background: repeating-linear-gradient(
                to bottom,
                #fdf8f2 0px,
                #fdf8f2 28px,
                #f1e7dd 29px
            ) !important;
            border-radius: 12px !important;
            border: 2px solid #d8c6b8 !important;
            font-family: 'Georgia', serif !important;
            color: #4c3a32 !important;
            padding: 12px !important;
        }

        /* Button styling */
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

        /* Cozy glow */
        .glow {
            text-shadow: 0 0 12px rgba(255, 203, 143, 0.6);
        }
            /* Floating stars & sparkles */
        @keyframes floatUp {
            0% { transform: translateY(0); opacity: 1; }
            100% { transform: translateY(-120px); opacity: 0; }
        }
        .sparkle {
            position: fixed;
            width: 6px;
            height: 6px;
            background: radial-gradient(circle, #fff8e6, #ffe2a8);
            border-radius: 50%;
            animation: floatUp 3s linear infinite;
            pointer-events: none;
            z-index: 9999;
        }
    </style>


    <!-- Fireplace + night ambience (user must click play—browsers block autoplay) -->
    <p style='color:#f2e9d8; font-family:Georgia; margin-top:10px;'>🎧 For full cozy vibes, click play:</p>
    <audio controls loop style="width:100%; border-radius:10px;">
        <source src="https://cdn.pixabay.com/download/audio/2021/12/15/audio_9e2866ae5d.mp3?filename=fireplace-crackle-96216.mp3" type="audio/mpeg">
    </audio>

    <!-- Soft click sound -->
    <script>
        function playClick() {
            var click = new Audio('https://cdn.pixabay.com/download/audio/2022/10/21/audio_4f7d4e5aef.mp3?filename=pop-124454.mp3');
            click.volume = 0.2;
            click.play();
        }
        document.addEventListener('click', playClick);
    </script>

<!-- Floating Sparkles Script -->
<script>
    function createSparkle() {
        const sparkle = document.createElement('div');
        sparkle.classList.add('sparkle');
        sparkle.style.left = Math.random() * window.innerWidth + 'px';
        sparkle.style.top = (window.innerHeight - 20) + 'px';
        sparkle.style.animationDuration = (2 + Math.random() * 2) + 's';
        sparkle.style.opacity = Math.random();
        document.body.appendChild(sparkle);
        setTimeout(() => sparkle.remove(), 4000);
    }
    setInterval(createSparkle, 600);
</script>
    """,
    unsafe_allow_html=True,
)

# -------------------------------------------------
# TITLE
# -------------------------------------------------
st.markdown("# 🌙 Moonlit Fireplace Journal ✨")
st.markdown("### A warm, glowing notebook for nighttime thoughts.")

# Store entries
if "entries" not in st.session_state:
    st.session_state.entries = []

# New Entry
st.markdown("## 📝 New Entry")
entry_text = st.text_area("", placeholder="Write under the moonlight...", height=240)

if st.button("Save Entry ✨"):
    if entry_text.strip():
        st.session_state.entries.append({
            "text": entry_text,
            "date": datetime.now().astimezone().strftime("%b %d, %Y • %I:%M %p")
        })
        st.success("Your words are now part of the night sky ✨")
    else:
        st.error("Write something first 💛")

# -------------------------------------------------
# DISPLAY ENTRIES
# -------------------------------------------------
st.markdown("---")
st.markdown("## 📔 Notebook Pages")

if not st.session_state.entries:
    st.info("Your notebook is waiting for its first moonlit entry ✨")
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
