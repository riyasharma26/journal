import streamlit as st
from datetime import datetime

# -------------------------
# COZY / GIRLY / WARM VIBES + AUDIO
# -------------------------
st.set_page_config(page_title="Cozy Journal ✨", page_icon="🌸", layout="centered")

# Inject custom CSS + audio + click sounds
st.markdown(
    """
    <style>
        body {
            background-color: #fcefe8;
        }
        .main {
            background-color: #fcefe8 !important;
        }
        h1, h2, h3, h4, h5, h6, p {
            font-family: 'Georgia', serif;
            color: #6b4a46;
        }
        textarea {
            background-color: #fff6f2 !important;
            border-radius: 14px !important;
            border: 1px solid #f1d9d2 !important;
            font-family: 'Georgia', serif !important;
            color: #5a3f3a !important;
        }
        .stButton>button {
            background-color: #f3d6d1;
            color: #5a3f3a;
            font-family: 'Georgia', serif;
            border-radius: 14px;
            padding: 0.7rem 1.3rem;
            border: none;
            box-shadow: 0 2px 6px rgba(0,0,0,0.08);
        }
        .stButton>button:hover {
            background-color: #eac7c1;
        }
        .entry-box {
            background-color: #fff6f2;
            padding: 1.3rem;
            border-radius: 18px;
            border: 1px solid #f1d9d2;
            margin-bottom: 1rem;
            box-shadow: 0 2px 10px rgba(0,0,0,0.06);
        }
    </style>

    <!-- Soft lofi background ambience -->
    <audio autoplay loop volume="0.4">
        <source src="https://cdn.pixabay.com/download/audio/2022/03/15/audio_9c383746b8.mp3?filename=lofi-study-112191.mp3" type="audio/mpeg">
    </audio>

    <!-- Soft click sound for buttons -->
    <script>
        function playClick() {
            var audio = new Audio('https://cdn.pixabay.com/download/audio/2022/03/15/audio_b7afb6bbf4.mp3?filename=click-124467.mp3');
            audio.volume = 0.4;
            audio.play();
        }
        document.addEventListener('click', playClick);
    </script>
    """,
    unsafe_allow_html=True,
)

# Title
st.markdown("# 🌸✨ Soft & Girly Cozy Journal")
st.markdown("### A warm pastel space for your sweetest thoughts.")

# Store entries
if "entries" not in st.session_state:
    st.session_state.entries = []

# New Entry
st.markdown("## 🧸 New Entry")
entry_text = st.text_area("", placeholder="Write something cute...", height=200)

if st.button("Save Entry 💖"):
    if entry_text.strip():
        st.session_state.entries.append({
            "text": entry_text,
            "date": datetime.now().astimezone().strftime("%b %d, %Y • %I:%M %p")
        })
        st.success("Saved ✨ Your journal loves your energy ✨")
    else:
        st.error("Write a little something first, sweetheart 💗")

# Display Saved Entries
st.markdown("---")
st.markdown("## 📔 Past Entries ✨")

if not st.session_state.entries:
    st.info("Your pages are waiting for your magic ✨💗")
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
