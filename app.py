import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# ─── PAGE CONFIG ──────────────────────────────────────────────
st.set_page_config(
    page_title="🗿 Concrete Vault Runner",
    page_icon="🗿",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── LOAD GAME HTML ───────────────────────────────────────────
BASE_DIR = Path(__file__).parent
GAME_FILE = BASE_DIR / "concrete-vault-runner-v2.html"
if not GAME_FILE.exists():
    candidates = sorted(BASE_DIR.glob("*.html"))
    if candidates:
        GAME_FILE = candidates[0]
    else:
        st.error("Game HTML file not found.")
        st.stop()

game_html = GAME_FILE.read_text(encoding="utf-8")

# ─── GLOBAL CSS ───────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Bebas+Neue&display=swap');

/* Hide Streamlit chrome completely */
#MainMenu, footer, header { visibility:hidden; }
.block-container { padding:0 !important; max-width:100% !important; }
[data-testid="stAppViewContainer"] > section:first-child { padding:0 !important; }
[data-testid="stMain"] { padding:0 !important; }
[data-testid="stMainBlockContainer"] { padding:0 !important; max-width:100% !important; }
section.main > div { padding:0 !important; }
[data-testid="stToolbar"] { display:none !important; }
[data-testid="stDecoration"] { display:none !important; }

/* Sidebar */
[data-testid="stSidebar"] { background:#0A0A0A !important; border-right:1px solid rgba(200,184,154,0.12); }
[data-testid="stSidebar"] * { color:#C8B89A !important; font-family:'Share Tech Mono',monospace !important; }

.sb-title { font-family:'Bebas Neue',sans-serif !important; font-size:20px !important; letter-spacing:4px; color:#C8B89A !important; border-bottom:1px solid rgba(200,184,154,0.2); padding-bottom:8px; margin-bottom:12px; }
.sb-title span { color:#00FF88 !important; }

.ext-link { display:block; text-align:center; background:rgba(0,255,136,0.08); border:1px solid rgba(0,255,136,0.3); color:#00FF88 !important; text-decoration:none !important; font-size:11px; letter-spacing:3px; padding:8px; margin-bottom:6px; font-family:'Bebas Neue',sans-serif; }
.ext-link:hover { background:rgba(0,255,136,0.18); }

.vault-row { display:flex; justify-content:space-between; align-items:center; padding:6px 0; border-bottom:1px solid rgba(200,184,154,0.07); font-size:10px; }
.vault-apy { font-size:12px; font-family:'Bebas Neue',sans-serif; color:#00FF88; }
.vault-chain { font-size:7px; opacity:.4; letter-spacing:2px; }

.stat-card { background:rgba(255,255,255,0.03); border:1px solid rgba(200,184,154,0.12); border-radius:3px; padding:8px 12px; margin-bottom:8px; }
.stat-card-lbl { font-size:8px; letter-spacing:3px; opacity:0.4; text-transform:uppercase; margin-bottom:3px; }
.stat-card-val { font-size:18px; font-family:'Bebas Neue',sans-serif; letter-spacing:2px; }
.green { color:#00FF88 !important; } .gold { color:#FFD700 !important; } .blue { color:#00C8FF !important; }

.sb-divider { border:none; border-top:1px solid rgba(200,184,154,0.1); margin:12px 0; }

/* Game iframe - zero margin */
iframe[title="game"] { display:block !important; border:none !important; margin:0 !important; padding:0 !important; }
</style>
""", unsafe_allow_html=True)

# ─── SIDEBAR ──────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="sb-title">🗿 <span>CONCRETE</span><br>VAULT RUNNER</div>', unsafe_allow_html=True)

    st.markdown("""
    <a class="ext-link" href="https://app.concrete.xyz/earn" target="_blank">▶ LAUNCH EARN APP</a>
    <a class="ext-link" href="https://points.concrete.xyz/home" target="_blank">⭐ CONCRETE POINTS</a>
    <a class="ext-link" href="https://concrete.xyz" target="_blank">🌐 CONCRETE.XYZ</a>
    """, unsafe_allow_html=True)

    st.markdown('<hr class="sb-divider">', unsafe_allow_html=True)

    # AI TOOLS
    st.markdown('<div style="font-size:9px;letter-spacing:3px;opacity:.4;margin-bottom:10px">🤖 AI TOOLS</div>', unsafe_allow_html=True)
    st.markdown("""
    <a class="ext-link" href="https://concrete-guide.streamlit.app/" target="_blank"
       style="background:rgba(0,200,255,0.08);border-color:rgba(0,200,255,0.3);color:#00C8FF !important;">
       📖 CONCRETE GUIDE
    </a>
    <div style="font-size:8px;opacity:.4;letter-spacing:1px;margin:-2px 0 8px;text-align:center">Learn DeFi &amp; how Concrete works</div>
    <a class="ext-link" href="https://concrete-vault.streamlit.app/" target="_blank"
       style="background:rgba(159,127,255,0.08);border-color:rgba(159,127,255,0.3);color:#9F7FFF !important;">
       🏦 VAULT EXPLORER
    </a>
    <div style="font-size:8px;opacity:.4;letter-spacing:1px;margin:-2px 0 8px;text-align:center">Browse &amp; compare live vaults</div>
    <a class="ext-link" href="https://concrete-assistant.streamlit.app/" target="_blank"
       style="background:rgba(255,107,53,0.08);border-color:rgba(255,107,53,0.3);color:#FF6B35 !important;">
       🤖 AI ASSISTANT
    </a>
    <div style="font-size:8px;opacity:.4;letter-spacing:1px;margin:-2px 0 8px;text-align:center">Ask anything about Concrete</div>
    """, unsafe_allow_html=True)

    st.markdown('<hr class="sb-divider">', unsafe_allow_html=True)

    # LIVE VAULTS
    st.markdown('<div style="font-size:9px;letter-spacing:3px;opacity:.4;margin-bottom:8px">LIVE VAULTS</div>', unsafe_allow_html=True)
    vaults = [
        ("DeFi USDT","8.5%","ETH"), ("WBTC Vault","7.0%","ETH"),
        ("WBERA","142.73%","BERA"), ("Movement ETH","20%","MOVE"),
        ("frxUSD+","7.3%","ETH"), ("Morpho USD","13.08%","ETH"),
        ("Corn Stables","10%","CORN"), ("sEIGEN","9%","ETH"),
        ("Bera Stables","9.29%","BERA"),
    ]
    vault_html = ""
    for name, apy, chain in vaults:
        vault_html += f'<div class="vault-row"><div><div style="font-size:10px">{name}</div><div class="vault-chain">{chain}</div></div><div class="vault-apy">{apy}</div></div>'
    st.markdown(vault_html, unsafe_allow_html=True)

    st.markdown('<hr class="sb-divider">', unsafe_allow_html=True)

    # PROTOCOL STATS
    st.markdown('<div style="font-size:9px;letter-spacing:3px;opacity:.4;margin-bottom:8px">PROTOCOL STATS</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="stat-card"><div class="stat-card-lbl">ASSETS ON PLATFORM</div><div class="stat-card-val green">$902.3M</div></div>
    <div class="stat-card"><div class="stat-card-lbl">ASSETS PROCESSED</div><div class="stat-card-val gold">$11.25B</div></div>
    <div class="stat-card"><div class="stat-card-lbl">SMART CONTRACT AUDITS</div><div class="stat-card-val blue">6 FIRMS</div></div>
    """, unsafe_allow_html=True)

    st.markdown('<hr class="sb-divider">', unsafe_allow_html=True)

    # HOW TO PLAY
    st.markdown('<div style="font-size:9px;letter-spacing:3px;opacity:.4;margin-bottom:8px">HOW TO PLAY</div>', unsafe_allow_html=True)
    controls = [
        ("SPACE / ↑ / TAP","JUMP"), ("↑ IN AIR","DOUBLE JUMP"),
        ("↓ / SWIPE DOWN","SLIDE"), ("ESC / P","PAUSE"),
        ("🏦 VAULT","+APY"), ("👜 BAGS","+POINTS"),
        ("🛡️ SHIELD","BLOCK HIT"), ("⚡ BOOST","+SPEED"),
        ("🌕 MOON","MEGA PTS"), ("📉 CRASH","GAME OVER"),
    ]
    ctrl_html = ""
    for key, action in controls:
        ctrl_html += f'<div style="display:flex;justify-content:space-between;padding:3px 0;font-size:9px;border-bottom:1px solid rgba(200,184,154,0.06)"><span style="opacity:.5">{key}</span><span style="color:#00FF88">{action}</span></div>'
    st.markdown(ctrl_html, unsafe_allow_html=True)

    st.markdown('<hr class="sb-divider">', unsafe_allow_html=True)

    backers = ["POLYCHAIN","VanEck","YZi Labs","Portal Ventures","Hashed","Tribe Capital"]
    st.markdown('<div style="font-size:9px;letter-spacing:3px;opacity:.4;margin-bottom:6px">BACKED BY</div>', unsafe_allow_html=True)
    st.markdown('<div style="line-height:2">' + ''.join([f'<span style="font-size:8px;opacity:.4;margin-right:8px">{b}</span>' for b in backers]) + '</div>', unsafe_allow_html=True)

# ─── MAIN GAME — use components.html (NOT iframe/base64) ──────
components.html(game_html, height=700, scrolling=False)
