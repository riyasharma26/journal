import streamlit as st
from datetime import datetime

# -------------------------
# AESTHETIC / COZY STYLE SETTINGS
# -------------------------
st.set_page_config(page_title="Cozy Journal ✨", page_icon="🌙", layout="centered")

st.markdown(
    """
    <style>
        body {
            background-color: #f7efe5;
        }
        .main {
            background-color: #f7efe5 !important;
        }
        h1, h2, h3, h4, h5, h6, p {
            font-family: 'Georgia', serif;
            color: #5b4641;
        }
        textarea {
            background-color: #fdf7f2 !important;
            border-radius: 12px !important;
            border: 1px solid #e5d8cc !important;
            font-family: 'Georgia', serif !important;
            color: #4e3b35 !important;
        }
        .stButton>button {
            background-color: #e7d6c7;
            color: #4e3b35;
            font-family: 'Georgia', serif;
            border-radius: 12px;
            padding: 0.6rem 1.2rem;
            border: none;
        }
        .stButton>button:hover {
            background-color: #d7c4b2;
        }
        .entry-box {
            background-color: #fdf7f2;
            padding: 1.2rem;
            border-radius: 16px;
            border: 1px solid #e8ddd3;
            margin-bottom: 1rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title
st.markdown("# 🌙✨ Cozy Aesthetic Journal")
st.markdown("### A soft place to write your thoughts, dreams, and moments.")

# Store entries
if "entries" not in st.session_state:
    st.session_state.entries = []

# New Entry
st.markdown("## 📝 New Entry")
entry_text = st.text_area("", placeholder="Pour your heart out...", height=180)

if st.button("Save Entry ✧"):
    if entry_text.strip():
        st.session_state.entries.append({
            "text": entry_text,
            "date": datetime.now().strftime("%b %d, %Y • %I:%M %p")
        })
        st.success("Saved to your cozy journal ✨")
    else:
        st.error("Write something first, lovely ✧")

# Display Saved Entries
st.markdown("---")
st.markdown("## 📔 Your Past Entries")

if not st.session_state.entries:
    st.info("No entries yet — your cozy pages await ✨")
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
