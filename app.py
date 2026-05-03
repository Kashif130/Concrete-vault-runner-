import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="🗿 Concrete Vault Runner",
    page_icon="🗿",
    layout="wide",
    initial_sidebar_state="expanded",
)

BASE_DIR = Path(__file__).parent
GAME_FILE = BASE_DIR / "concrete-vault-hub.html"
if not GAME_FILE.exists():
    candidates = sorted(BASE_DIR.glob("*.html"))
    GAME_FILE = candidates[0] if candidates else None
    if not GAME_FILE:
        st.error("Game HTML not found."); st.stop()

game_html = GAME_FILE.read_text(encoding="utf-8")

# ── GLOBAL CSS ────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Bebas+Neue&display=swap');

/* Hide Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
[data-testid="stToolbar"],
[data-testid="stDecoration"] { display: none !important; }

/* Remove all padding from main area */
.block-container { padding: 0 !important; max-width: 100% !important; }
[data-testid="stMain"] { padding: 0 !important; }
[data-testid="stMainBlockContainer"] { padding: 0 !important; max-width: 100% !important; }

/* Make iframe fill height */
iframe { display: block; border: none; }

/* ── SIDEBAR STYLING ── */
[data-testid="stSidebar"] {
    background: #08090a !important;
    border-right: 1px solid rgba(0,232,122,0.15) !important;
    min-width: 260px !important;
    max-width: 260px !important;
}
[data-testid="stSidebar"] * {
    color: #c8b99a !important;
    font-family: 'Share Tech Mono', monospace !important;
}
[data-testid="stSidebarContent"] {
    padding: 0 !important;
}

/* Logo block */
.sb-logo-wrap {
    padding: 16px 14px 14px;
    border-bottom: 1px solid rgba(0,232,122,0.12);
    background: linear-gradient(135deg, rgba(0,232,122,0.06) 0%, transparent 70%);
    margin-bottom: 0;
}
.sb-logo-row {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 8px;
}
.sb-logo-icon {
    width: 40px;
    height: 40px;
    border-radius: 5px;
    background: rgba(0,232,122,0.1);
    border: 1px solid rgba(0,232,122,0.25);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 22px;
    line-height: 1;
    flex-shrink: 0;
}
.sb-logo-title {
    font-family: 'Bebas Neue', sans-serif !important;
    font-size: 16px !important;
    letter-spacing: 4px;
    line-height: 1.2;
}
.sb-logo-title span { color: #00e87a !important; }
.sb-logo-sub {
    font-size: 7px !important;
    letter-spacing: 2px;
    opacity: 0.4;
    margin-top: 2px;
}
.sb-tagline {
    font-size: 7.5px !important;
    letter-spacing: 1.5px;
    opacity: 0.45;
    line-height: 1.9;
}

/* Section divider */
.sb-divider {
    border: none;
    border-top: 1px solid rgba(0,232,122,0.1);
    margin: 0;
}
.sb-section {
    padding: 12px 14px;
    border-bottom: 1px solid rgba(255,255,255,0.05);
}
.sb-sec-title {
    font-size: 7px !important;
    letter-spacing: 3px;
    text-transform: uppercase;
    opacity: 0.35;
    margin-bottom: 9px;
}

/* External links */
.ext-link {
    display: flex;
    align-items: center;
    gap: 8px;
    background: rgba(0,232,122,0.06);
    border: 1px solid rgba(0,232,122,0.2);
    color: #00e87a !important;
    text-decoration: none !important;
    font-size: 9px !important;
    letter-spacing: 2px;
    padding: 7px 10px;
    margin-bottom: 5px;
    border-radius: 2px;
    font-family: 'Bebas Neue', sans-serif !important;
    transition: all .15s;
}
.ext-link:hover { background: rgba(0,232,122,0.12); border-color: rgba(0,232,122,0.45); }

/* Tool links */
.tool-link {
    display: flex;
    align-items: center;
    gap: 8px;
    border: 1px solid rgba(255,255,255,0.07);
    padding: 7px 10px;
    margin-bottom: 5px;
    border-radius: 2px;
    font-size: 9px !important;
    letter-spacing: 1px;
    text-decoration: none !important;
    transition: all .15s;
}
.tool-link.blue  { background: rgba(0,200,255,0.06); border-color: rgba(0,200,255,0.2); color: #00c8ff !important; }
.tool-link.purple{ background: rgba(159,127,255,0.06); border-color: rgba(159,127,255,0.2); color: #9f7fff !important; }
.tool-link.orange{ background: rgba(255,107,53,0.06); border-color: rgba(255,107,53,0.2); color: #ff6b35 !important; }

/* Vault rows */
.vault-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 5px 0;
    border-bottom: 1px solid rgba(255,255,255,0.05);
    font-size: 9px !important;
}
.vault-row:last-child { border-bottom: none; }
.vault-name { opacity: 0.75; }
.vault-chain { font-size: 7px !important; opacity: 0.35; letter-spacing: 2px; }
.vault-apy {
    font-family: 'Bebas Neue', sans-serif !important;
    font-size: 12px !important;
    color: #00e87a !important;
}

/* Stat cards */
.stat-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(200,184,154,0.1);
    border-radius: 2px;
    padding: 8px 11px;
    margin-bottom: 6px;
}
.stat-card-lbl {
    font-size: 7px !important;
    letter-spacing: 3px;
    opacity: 0.35;
    text-transform: uppercase;
    margin-bottom: 3px;
}
.stat-card-val {
    font-family: 'Bebas Neue', sans-serif !important;
    font-size: 17px !important;
    letter-spacing: 2px;
}
.green { color: #00e87a !important; }
.gold  { color: #f5c842 !important; }
.blue  { color: #29b6f6 !important; }

/* Controls table */
.ctrl-row {
    display: flex;
    justify-content: space-between;
    padding: 3px 0;
    font-size: 8.5px !important;
    border-bottom: 1px solid rgba(255,255,255,0.04);
}
.ctrl-row:last-child { border-bottom: none; }
.ctrl-key {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.12);
    padding: 1px 5px;
    border-radius: 2px;
    font-size: 7.5px !important;
    color: #d4cfc8 !important;
}
.ctrl-lbl { opacity: 0.5; }

/* Footer links */
.sb-footer { padding: 12px 14px; }
.sb-footer-link {
    display: block;
    font-size: 8px !important;
    letter-spacing: 1.5px;
    opacity: 0.4;
    text-decoration: none !important;
    color: #c8b99a !important;
    padding: 3px 0;
    transition: opacity .15s;
}
.sb-footer-link:hover { opacity: 0.9; color: #00e87a !important; }

</style>
""", unsafe_allow_html=True)

# ── SIDEBAR ───────────────────────────────────────────────────
with st.sidebar:

    # Logo / Brand
    st.markdown("""
    <div class="sb-logo-wrap">
      <div class="sb-logo-row">
        <div class="sb-logo-icon">🗿</div>
        <div>
          <div class="sb-logo-title">VAULT <span>RUNNER</span></div>
          <div class="sb-logo-sub">BY CONCRETE.XYZ</div>
        </div>
      </div>
      <div class="sb-tagline">
        DEPOSIT INTO VAULTS · EARN APY<br>
        COLLECT BAGS · DODGE CRASHES<br>
        BUILD COMBOS · REACH THE MOON
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Concrete Apps
    st.markdown("""
    <div class="sb-section">
      <div class="sb-sec-title">🔗 Concrete Apps</div>
      <a class="ext-link" href="https://app.concrete.xyz/earn" target="_blank">🏦&nbsp; LAUNCH EARN APP</a>
      <a class="ext-link" href="https://points.concrete.xyz/home" target="_blank">⭐&nbsp; CONCRETE POINTS</a>
      <a class="ext-link" href="https://concrete.xyz" target="_blank">🌐&nbsp; CONCRETE.XYZ</a>
    </div>
    """, unsafe_allow_html=True)

    # AI Tools
    st.markdown("""
    <div class="sb-section">
      <div class="sb-sec-title">🤖 AI Tools</div>
      <a class="tool-link blue" href="https://concrete-guide.streamlit.app/" target="_blank">📖&nbsp; Concrete Guide</a>
      <div style="font-size:7.5px;opacity:.3;letter-spacing:1px;margin:-2px 0 7px 2px">Learn DeFi &amp; how Concrete works</div>
      <a class="tool-link purple" href="https://concrete-vault.streamlit.app/" target="_blank">💼&nbsp; Vault Explorer</a>
      <div style="font-size:7.5px;opacity:.3;letter-spacing:1px;margin:-2px 0 7px 2px">Browse &amp; compare live vaults</div>
      <a class="tool-link orange" href="https://concrete-assistant.streamlit.app/" target="_blank">🤖&nbsp; AI Assistant</a>
      <div style="font-size:7.5px;opacity:.3;letter-spacing:1px;margin:-2px 0 2px 2px">Ask anything about Concrete</div>
    </div>
    """, unsafe_allow_html=True)

    # Live Vaults
    vaults = [
        ("DeFi USDT",   "8.5%",    "ETH",  "#00e87a"),
        ("WBTC Vault",  "7.0%",    "ETH",  "#f5c842"),
        ("WBERA",       "142.73%", "BERA", "#ff7043"),
        ("Movement ETH","20%",     "MOVE", "#29b6f6"),
        ("frxUSD+",     "7.3%",    "ETH",  "#b8ff9f"),
        ("Morpho USD",  "13.08%",  "ETH",  "#a78bfa"),
        ("Corn Stables","10%",     "CORN", "#ffcc44"),
        ("sEIGEN",      "9%",      "ETH",  "#00e87a"),
        ("Bera Stables","9.29%",   "BERA", "#ff9f44"),
    ]
    vault_rows = "".join([
        f'<div class="vault-row">'
        f'<div><div class="vault-name">{n}</div><div class="vault-chain">{c}</div></div>'
        f'<div class="vault-apy" style="color:{col}">{a}</div>'
        f'</div>'
        for n, a, c, col in vaults
    ])
    st.markdown(f"""
    <div class="sb-section">
      <div class="sb-sec-title">📊 Live Vaults</div>
      {vault_rows}
    </div>
    """, unsafe_allow_html=True)

    # Platform Stats
    st.markdown("""
    <div class="sb-section">
      <div class="sb-sec-title">📈 Platform Stats</div>
      <div class="stat-card"><div class="stat-card-lbl">Assets on Platform</div><div class="stat-card-val green">$902.3M</div></div>
      <div class="stat-card"><div class="stat-card-lbl">Assets Processed</div><div class="stat-card-val gold">$11.25B</div></div>
      <div class="stat-card"><div class="stat-card-lbl">Smart Contract Audits</div><div class="stat-card-val blue">6 FIRMS</div></div>
    </div>
    """, unsafe_allow_html=True)

    # Controls
    controls = [
        ("SPACE / ↑ / TAP", "JUMP"),
        ("↑ IN AIR",         "DOUBLE JUMP"),
        ("↓ / SWIPE DOWN",  "SLIDE"),
        ("ESC / P",          "PAUSE"),
        ("🏦 VAULT",         "+APY"),
        ("👜 BAGS",          "+POINTS"),
        ("🛡️ SHIELD",        "BLOCK HIT"),
        ("⚡ BOOST",         "+SPEED"),
        ("🌕 MOON",          "MEGA PTS"),
        ("📉 CRASH",         "GAME OVER"),
    ]
    ctrl_rows = "".join([
        f'<div class="ctrl-row"><span class="ctrl-lbl">{k}</span><span class="ctrl-key">{v}</span></div>'
        for k, v in controls
    ])
    st.markdown(f"""
    <div class="sb-section">
      <div class="sb-sec-title">⌨ How to Play</div>
      {ctrl_rows}
    </div>
    """, unsafe_allow_html=True)

    # Footer
    st.markdown("""
    <div class="sb-footer">
      <a class="sb-footer-link" href="https://x.com/ConcreteXYZ" target="_blank">↗ X / Twitter</a>
      <a class="sb-footer-link" href="https://discord.gg/concretexyz" target="_blank">↗ Discord</a>
      <a class="sb-footer-link" href="https://docs.concrete.xyz" target="_blank">↗ Docs</a>
    </div>
    """, unsafe_allow_html=True)


# ── GAME ──────────────────────────────────────────────────────
# Render the full game HTML — it has its own internal nav + sidebar toggle
components.html(game_html, height=700, scrolling=False)
