import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="🗿 Concrete Vault Runner",
    page_icon="🗿",
    layout="wide",
    initial_sidebar_state="collapsed",
)

BASE_DIR = Path(__file__).parent
GAME_FILE = BASE_DIR / "concrete-vault-hub.html"
if not GAME_FILE.exists():
    candidates = sorted(BASE_DIR.glob("*.html"))
    GAME_FILE = candidates[0] if candidates else None
    if not GAME_FILE:
        st.error("Game HTML not found.")
        st.stop()

game_html = GAME_FILE.read_text(encoding="utf-8")

# ── FULL-SCREEN CSS — removes every Streamlit pixel ──────────
st.markdown("""
<style>
/* Hide all Streamlit UI chrome */
#MainMenu, footer, header,
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"],
[data-testid="collapsedControl"] { display: none !important; }

/* Zero all wrappers */
html, body {
    margin: 0 !important;
    padding: 0 !important;
    overflow: hidden !important;
    background: #050607 !important;
}
.block-container,
[data-testid="stMain"],
[data-testid="stMainBlockContainer"],
[data-testid="stVerticalBlock"],
[data-testid="stVerticalBlockBorderWrapper"],
section.main > div,
.appview-container,
.main {
    padding: 0 !important;
    margin: 0 !important;
    max-width: 100% !important;
    width: 100% !important;
    height: 100% !important;
}

/* Force iframe to cover the entire viewport */
iframe {
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    width: 100vw !important;
    height: 100vh !important;
    border: none !important;
    z-index: 9999 !important;
    display: block !important;
    margin: 0 !important;
    padding: 0 !important;
}
</style>
""", unsafe_allow_html=True)

# Render — CSS overrides height to 100vh regardless of this value
components.html(game_html, height=900, scrolling=False)
