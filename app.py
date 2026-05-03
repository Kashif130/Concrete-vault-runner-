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
GAME_FILE = BASE_DIR / "concrete-vault-runner-v2.html"
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

#MainMenu, footer, header { visibility:hidden; }
[data-testid="stToolbar"],[data-testid="stDecoration"] { display:none !important; }
.block-container { padding:0 !important; max-width:100% !important; }
[data-testid="stMain"] { padding:0 !important; }
[data-testid="stMainBlockContainer"] { padding:0 !important; max-width:100% !important; }

/* Sidebar */
[data-testid="stSidebar"] { background:#0A0A0A !important; border-right:1px solid rgba(200,184,154,0.12); }
[data-testid="stSidebar"] * { color:#C8B89A !important; font-family:'Share Tech Mono',monospace !important; }
.sb-title { font-family:'Bebas Neue',sans-serif !important; font-size:20px !important; letter-spacing:4px; border-bottom:1px solid rgba(200,184,154,0.2); padding-bottom:8px; margin-bottom:12px; }
.sb-title span { color:#00FF88 !important; }
.ext-link { display:block; text-align:center; background:rgba(0,255,136,0.08); border:1px solid rgba(0,255,136,0.3); color:#00FF88 !important; text-decoration:none !important; font-size:11px; letter-spacing:3px; padding:8px; margin-bottom:6px; font-family:'Bebas Neue',sans-serif; }
.vault-row { display:flex; justify-content:space-between; align-items:center; padding:6px 0; border-bottom:1px solid rgba(200,184,154,0.07); font-size:10px; }
.vault-apy { font-size:12px; font-family:'Bebas Neue',sans-serif; color:#00FF88; }
.vault-chain { font-size:7px; opacity:.4; letter-spacing:2px; }
.stat-card { background:rgba(255,255,255,0.03); border:1px solid rgba(200,184,154,0.12); border-radius:3px; padding:8px 12px; margin-bottom:8px; }
.stat-card-lbl { font-size:8px; letter-spacing:3px; opacity:0.4; text-transform:uppercase; margin-bottom:3px; }
.stat-card-val { font-size:18px; font-family:'Bebas Neue',sans-serif; letter-spacing:2px; }
.green{color:#00FF88!important}.gold{color:#FFD700!important}.blue{color:#00C8FF!important}
.sb-divider { border:none; border-top:1px solid rgba(200,184,154,0.1); margin:12px 0; }

/* ── NAVBAR (always visible, above iframe) ── */
#cvr-nav {
    display:flex;
    align-items:center;
    background:#000;
    border-bottom:1px solid rgba(200,184,154,0.2);
    padding:0 12px;
    height:46px;
    font-family:'Share Tech Mono',monospace;
    color:#C8B89A;
    gap:0;
    width:100%;
    box-sizing:border-box;
}
#cvr-nav .nav-logo {
    font-size:22px;
    margin-right:14px;
    flex-shrink:0;
}
#cvr-nav .nav-stat {
    display:flex;
    flex-direction:column;
    align-items:center;
    flex:1;
    border-left:1px solid rgba(200,184,154,0.1);
    padding:4px 0;
    height:46px;
    justify-content:center;
}
#cvr-nav .nav-lbl {
    font-size:6px;
    letter-spacing:2px;
    opacity:.4;
    text-transform:uppercase;
}
#cvr-nav .nav-val {
    font-size:14px;
    font-weight:700;
    font-family:'Bebas Neue',sans-serif;
    letter-spacing:1px;
    margin-top:1px;
}
.c-gold{color:#FFD700}.c-green{color:#00FF88}.c-blue{color:#00C8FF}.c-orange{color:#FF6B35}
</style>
""", unsafe_allow_html=True)

# ── SIDEBAR ───────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="sb-title">🗿 <span>CONCRETE</span><br>VAULT RUNNER</div>', unsafe_allow_html=True)
    st.markdown("""
    <a class="ext-link" href="https://app.concrete.xyz/earn" target="_blank">▶ LAUNCH EARN APP</a>
    <a class="ext-link" href="https://points.concrete.xyz/home" target="_blank">⭐ CONCRETE POINTS</a>
    <a class="ext-link" href="https://concrete.xyz" target="_blank">🌐 CONCRETE.XYZ</a>
    """, unsafe_allow_html=True)
    st.markdown('<hr class="sb-divider">', unsafe_allow_html=True)

    st.markdown('<div style="font-size:9px;letter-spacing:3px;opacity:.4;margin-bottom:10px">🤖 AI TOOLS</div>', unsafe_allow_html=True)
    st.markdown("""
    <a class="ext-link" href="https://concrete-guide.streamlit.app/" target="_blank" style="background:rgba(0,200,255,0.08);border-color:rgba(0,200,255,0.3);color:#00C8FF !important;">📖 CONCRETE GUIDE</a>
    <div style="font-size:8px;opacity:.4;letter-spacing:1px;margin:-2px 0 8px;text-align:center">Learn DeFi &amp; how Concrete works</div>
    <a class="ext-link" href="https://concrete-vault.streamlit.app/" target="_blank" style="background:rgba(159,127,255,0.08);border-color:rgba(159,127,255,0.3);color:#9F7FFF !important;">🏦 VAULT EXPLORER</a>
    <div style="font-size:8px;opacity:.4;letter-spacing:1px;margin:-2px 0 8px;text-align:center">Browse &amp; compare live vaults</div>
    <a class="ext-link" href="https://concrete-assistant.streamlit.app/" target="_blank" style="background:rgba(255,107,53,0.08);border-color:rgba(255,107,53,0.3);color:#FF6B35 !important;">🤖 AI ASSISTANT</a>
    <div style="font-size:8px;opacity:.4;letter-spacing:1px;margin:-2px 0 8px;text-align:center">Ask anything about Concrete</div>
    """, unsafe_allow_html=True)
    st.markdown('<hr class="sb-divider">', unsafe_allow_html=True)

    vaults = [("DeFi USDT","8.5%","ETH"),("WBTC Vault","7.0%","ETH"),("WBERA","142.73%","BERA"),
              ("Movement ETH","20%","MOVE"),("frxUSD+","7.3%","ETH"),("Morpho USD","13.08%","ETH"),
              ("Corn Stables","10%","CORN"),("sEIGEN","9%","ETH"),("Bera Stables","9.29%","BERA")]
    st.markdown('<div style="font-size:9px;letter-spacing:3px;opacity:.4;margin-bottom:8px">LIVE VAULTS</div>', unsafe_allow_html=True)
    st.markdown("".join([f'<div class="vault-row"><div><div style="font-size:10px">{n}</div><div class="vault-chain">{c}</div></div><div class="vault-apy">{a}</div></div>' for n,a,c in vaults]), unsafe_allow_html=True)
    st.markdown('<hr class="sb-divider">', unsafe_allow_html=True)

    st.markdown("""
    <div class="stat-card"><div class="stat-card-lbl">ASSETS ON PLATFORM</div><div class="stat-card-val green">$902.3M</div></div>
    <div class="stat-card"><div class="stat-card-lbl">ASSETS PROCESSED</div><div class="stat-card-val gold">$11.25B</div></div>
    <div class="stat-card"><div class="stat-card-lbl">SMART CONTRACT AUDITS</div><div class="stat-card-val blue">6 FIRMS</div></div>
    """, unsafe_allow_html=True)
    st.markdown('<hr class="sb-divider">', unsafe_allow_html=True)

    controls = [("SPACE/↑/TAP","JUMP"),("↑ IN AIR","DOUBLE JUMP"),("↓/SWIPE","SLIDE"),
                ("ESC/P","PAUSE"),("🏦 VAULT","+APY"),("👜 BAGS","+PTS"),
                ("🛡️ SHIELD","BLOCK"),("⚡ BOOST","+SPEED"),("🌕 MOON","MEGA PTS"),("📉 CRASH","GAME OVER")]
    st.markdown('<div style="font-size:9px;letter-spacing:3px;opacity:.4;margin-bottom:8px">HOW TO PLAY</div>', unsafe_allow_html=True)
    st.markdown("".join([f'<div style="display:flex;justify-content:space-between;padding:3px 0;font-size:9px;border-bottom:1px solid rgba(200,184,154,0.06)"><span style="opacity:.5">{k}</span><span style="color:#00FF88">{a}</span></div>' for k,a in controls]), unsafe_allow_html=True)

# ── NAVBAR — rendered by Streamlit, always visible ────────────
st.markdown("""
<div id="cvr-nav">
  <div class="nav-logo">🗿</div>
  <div class="nav-stat">
    <span class="nav-lbl">BAGS</span>
    <span class="nav-val c-gold" id="nb-pts">0</span>
  </div>
  <div class="nav-stat">
    <span class="nav-lbl">APY</span>
    <span class="nav-val c-green" id="nb-apy">0.0%</span>
  </div>
  <div class="nav-stat">
    <span class="nav-lbl">VAULT</span>
    <span class="nav-val c-blue" id="nb-vault">—</span>
  </div>
  <div class="nav-stat">
    <span class="nav-lbl">LEVEL</span>
    <span class="nav-val" id="nb-lvl">1</span>
  </div>
  <div class="nav-stat">
    <span class="nav-lbl">BEST</span>
    <span class="nav-val c-orange" id="nb-best">0</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ── GAME (no HUD inside — stats shown in navbar above) ────────
components.html(game_html, height=620, scrolling=False)
