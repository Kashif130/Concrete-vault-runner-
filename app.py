import streamlit as st
import random
import time
import json
import os

# =========================
# 🎨 UI THEME (NEON GLASS)
# =========================
st.set_page_config(page_title="Concrete Moai Core", layout="centered")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #000000, #0a0f1c, #001a2b);
    color: white;
}

.block-container {
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(12px);
    border-radius: 18px;
    padding: 20px;
}

.stButton>button {
    border: 1px solid #00f5ff;
    color: #00f5ff;
    background: transparent;
    border-radius: 10px;
    transition: 0.3s;
}

.stButton>button:hover {
    background: #00f5ff;
    color: black;
    box-shadow: 0 0 15px #00f5ff;
}
</style>
""", unsafe_allow_html=True)

# =========================
# 🧠 GAME STATE
# =========================
if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.stability = 100
    st.session_state.repairs = 3
    st.session_state.game_over = False
    st.session_state.log = "Moai Core initialized..."

# =========================
# 🏆 LOCAL LEADERBOARD (JSON FILE)
# =========================
LEADERBOARD_FILE = "leaderboard.json"

def load_leaderboard():
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r") as f:
            return json.load(f)
    return []

def save_score(name, score):
    data = load_leaderboard()
    data.append({"name": name, "score": score})
    data = sorted(data, key=lambda x: x["score"], reverse=True)[:10]

    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(data, f)

def show_leaderboard():
    st.subheader("🏆 Leaderboard")
    data = load_leaderboard()
    if not data:
        st.caption("No scores yet")
        return
    for i, d in enumerate(data, 1):
        st.write(f"{i}. {d['name']} — {d['score']}x")

# =========================
# 🧠 AI DIFFICULTY ENGINE
# =========================
def difficulty():
    s = st.session_state.score
    stbl = st.session_state.stability

    if s < 10:
        return 1
    elif stbl > 70:
        return 2.5
    elif stbl < 30:
        return 1.2
    return 2

# =========================
# 🎲 AI EVENTS
# =========================
def ai_event():
    r = random.random()

    if r < 0.12:
        loss = random.randint(10, 25)
        st.session_state.stability -= loss
        st.session_state.log = f"💥 Market Crash (-{loss})"

    elif r < 0.25:
        gain = random.randint(2, 5)
        st.session_state.score += gain
        st.session_state.log = f"🚀 AI Boost (+{gain})"

# =========================
# 🎮 GAME UI
# =========================
st.title("🗿 CONCRETE MOAI CORE")
st.caption("Build. Survive. Adapt.")

col1, col2, col3 = st.columns(3)
col1.metric("Score", st.session_state.score)
col2.metric("Stability", f"{st.session_state.stability}%")
col3.metric("Repairs", st.session_state.repairs)

st.progress(max(0, st.session_state.stability) / 100)

st.write("---")

# =========================
# 🎯 GAME LOGIC
# =========================
if not st.session_state.game_over:

    diff = difficulty()

    c1, c2, c3 = st.columns(3)

    # 🏗️ BUILD
    if c1.button("🏗️ Build Block"):
        time.sleep(0.2)

        if random.random() < 0.8:
            st.session_state.score += 1
            st.session_state.stability -= int(8 * diff)
            st.session_state.log = "🏗️ Block placed"
        else:
            st.session_state.stability -= 20
            st.session_state.log = "❌ Build failed"

        ai_event()

    # 📊 RISKY YIELD
    if c2.button("📊 High Yield"):
        time.sleep(0.2)

        if random.random() < 0.7:
            st.session_state.score += 2
            st.session_state.stability -= int(15 * diff)
            st.session_state.log = "📊 Profit gained"
        else:
            st.session_state.stability -= 30
            st.session_state.log = "📉 Bad allocation"

        ai_event()

    # 🛡️ REPAIR
    if c3.button("🛡️ Repair"):
        if st.session_state.repairs > 0:
            st.session_state.stability = min(100, st.session_state.stability + 20)
            st.session_state.repairs -= 1
            st.session_state.log = "🛡️ Stabilized"
        else:
            st.session_state.log = "No repairs left"

    # WIN / LOSE CONDITIONS
    if st.session_state.stability <= 0:
        st.session_state.game_over = True

    if st.session_state.score >= 50:
        st.balloons()
        st.success("🏆 YOU BUILT AN UNBREAKABLE STRUCTURE!")
        st.session_state.game_over = True

else:
    st.error(f"💀 GAME OVER — Score: {st.session_state.score}")

    name = st.text_input("Enter your name for leaderboard")

    if st.button("Submit Score"):
        if name:
            save_score(name, st.session_state.score)
            st.success("Saved!")

    if st.button("Restart Game"):
        for k in st.session_state.keys():
            del st.session_state[k]
        st.rerun()

# =========================
# 🧾 LOG + LEADERBOARD
# =========================
st.write("---")
st.info(st.session_state.log)

show_leaderboard()
