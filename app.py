import streamlit as st
import random
import time
from supabase import create_client

# ==============================
# 🔐 CONFIG (Use Streamlit Secrets in production)
# ==============================
SUPABASE_URL = st.secrets.get("SUPABASE_URL", "")
SUPABASE_KEY = st.secrets.get("SUPABASE_KEY", "")

supabase = None
if SUPABASE_URL and SUPABASE_KEY:
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# ==============================
# 🎨 NEON GLASS UI
# ==============================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
}
.block-container {
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(12px);
    border-radius: 20px;
    padding: 20px;
}
.stButton>button {
    background: transparent;
    border: 2px solid #00f5ff;
    color: #00f5ff;
    border-radius: 12px;
    transition: 0.3s;
}
.stButton>button:hover {
    background: #00f5ff;
    color: black;
    box-shadow: 0 0 20px #00f5ff;
}
</style>
""", unsafe_allow_html=True)

# ==============================
# 🧠 GAME STATE
# ==============================
def init():
    defaults = {
        "score": 0,
        "stability": 100,
        "repairs": 3,
        "game_over": False
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

def reset():
    for k in ["score", "stability", "repairs", "game_over"]:
        del st.session_state[k]
    st.rerun()

# ==============================
# 🧠 AI DIFFICULTY
# ==============================
def difficulty():
    s = st.session_state.score
    stab = st.session_state.stability

    if s < 10:
        return 1
    elif s < 30:
        return 1.5
    elif stab > 70:
        return 2.5
    elif stab < 30:
        return 1.2
    return 2

# ==============================
# 🎲 SMART EVENTS
# ==============================
def smart_event():
    stab = st.session_state.stability
    s = st.session_state.score

    if stab > 80 and random.random() < 0.3:
        st.session_state.stability -= 25
        st.error("🐋 Whale Dump!")

    elif stab < 30 and random.random() < 0.4:
        st.session_state.stability += 15
        st.success("🛟 Recovery!")

    elif s > 20 and random.random() < 0.25:
        st.session_state.score += 5
        st.success("🚀 Momentum Boost!")

# ==============================
# 🏆 LEADERBOARD
# ==============================
def save_score(name, score):
    if supabase:
        supabase.table("leaderboard").insert({
            "username": name,
            "score": score
        }).execute()

def get_leaderboard():
    if supabase:
        res = supabase.table("leaderboard")\
            .select("*")\
            .order("score", desc=True)\
            .limit(10)\
            .execute()
        return res.data
    return []

# ==============================
# 🎮 GAME UI
# ==============================
def game():
    st.title("🗿 THE FLOOR IS CONCRETE")
    st.caption("Stack logic. Survive chaos.")

    # Stats
    c1, c2, c3 = st.columns(3)
    c1.metric("Yield", f"{st.session_state.score}x")
    c2.metric("Stability", f"{st.session_state.stability}%")
    c3.metric("Repairs", st.session_state.repairs)

    st.progress(max(0, st.session_state.stability) / 100)

    # Moai Mood
    if st.session_state.stability > 70:
        st.success("🗿 Floor is solid")
    elif st.session_state.stability > 30:
        st.warning("🧐 Shaking...")
    else:
        st.error("💢 Collapse imminent!")

    st.divider()

    if not st.session_state.game_over:

        diff = difficulty()

        c1, c2, c3 = st.columns(3)

        # 🏗️ Nexus
        if c1.button("🏗️ Nexus"):
            with st.spinner("Stacking..."):
                time.sleep(0.3)

            if random.random() < 0.85:
                st.session_state.score += 1
                dmg = random.randint(5, 10) * diff
                st.session_state.stability -= int(dmg)
            else:
                st.session_state.stability -= 20
                st.error("Failed!")

            smart_event()

        # 📊 Stability Block
        if c2.button("📊 Yield"):
            with st.spinner("Allocating..."):
                time.sleep(0.3)

            if random.random() < 0.7:
                gain = random.randint(2, 3)
                dmg = random.randint(10, 20) * diff
                st.session_state.score += gain
                st.session_state.stability -= int(dmg)
            else:
                st.session_state.stability -= 30
                st.error("Bad trade!")

            smart_event()

        # 🛡️ Repair
        if c3.button("🛡️ Repair"):
            if st.session_state.repairs > 0:
                heal = random.randint(10, 20)
                st.session_state.stability = min(100, st.session_state.stability + heal)
                st.session_state.repairs -= 1
            else:
                st.warning("No repairs left")

        # End conditions
        if st.session_state.stability <= 0:
            st.session_state.game_over = True

        if st.session_state.score >= 50:
            st.balloons()
            st.success("🏆 Unbreakable Floor!")
            st.session_state.game_over = True

    else:
        st.error(f"💀 Game Over at {st.session_state.score}x")

        name = st.text_input("Enter your name")
        if st.button("Submit Score"):
            if name:
                save_score(name, st.session_state.score)
                st.success("Saved!")

        st.button("🔄 Restart", on_click=reset)

    # ==============================
    # 🏆 LEADERBOARD DISPLAY
    # ==============================
    st.divider()
    st.subheader("🏆 Leaderboard")

    data = get_leaderboard()

    if data:
        for i, row in enumerate(data, 1):
            st.write(f"{i}. {row['username']} — {row['score']}x")
    else:
        st.caption("No scores yet")

# ==============================
# 🚀 RUN
# ==============================
init()
game()
