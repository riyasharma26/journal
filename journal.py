import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Aesthetic Journal", page_icon="🪄", layout="centered")

st.markdown("# 🪄 Aesthetic Journal")
st.markdown("Write your thoughts, save your memories.")

# Load entries stored in session state
if "entries" not in st.session_state:
    st.session_state.entries = []

# Journal input
st.markdown("### New Entry")
entry_text = st.text_area("", placeholder="Write your thoughts here...", height=150)

if st.button("Save Entry"):
    if entry_text.strip():
        st.session_state.entries.append({
            "text": entry_text,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M")
        })
        st.success("Entry saved!")
    else:
        st.error("Cannot save an empty entry.")

# Display entries
st.markdown("---")
st.markdown("### 📔 Your Saved Entries")

if not st.session_state.entries:
    st.info("No entries yet. Start writing above!")
else:
    for entry in reversed(st.session_state.entries):
        with st.container():
            st.markdown(f"**Date:** {entry['date']}")
            st.markdown(f"{entry['text']}")
            st.markdown("---")
