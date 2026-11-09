from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Planner Tugas", page_icon="📝", layout="wide")

# Satu scrollbar saja: halaman Streamlit tidak boleh scroll,
# iframe dibuat setinggi layar dan scroll di dalamnya.
st.markdown(
    """
    <style>
    header, footer, #MainMenu {visibility: hidden;}
    html, body, .stApp, [data-testid="stAppViewContainer"],
    [data-testid="stMain"], section.main {overflow: hidden !important;}
    .block-container {padding: 0 !important; max-width: 100% !important;}
    [data-testid="stVerticalBlock"] {gap: 0 !important;}
    iframe {height: 100vh !important; display: block; border: 0;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = (Path(__file__).parent / "todo-planner.html").read_text(encoding="utf-8")
components.html(html, height=900, scrolling=True)
