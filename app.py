from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Planner Tugas", page_icon="📝", layout="wide")

# Sembunyikan header/footer bawaan Streamlit dan hilangkan padding
st.markdown(
    "<style>header,footer,#MainMenu{visibility:hidden}"
    ".block-container{padding:0!important;max-width:100%!important}</style>",
    unsafe_allow_html=True,
)

html = (Path(__file__).parent / "todo-planner.html").read_text(encoding="utf-8")
components.html(html, height=1200, scrolling=True)
