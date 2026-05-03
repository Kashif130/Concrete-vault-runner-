import streamlit as st
import random
import time

# ======================
# INIT
# ======================
st.set_page_config(page_title="Moai Stack Rush", layout="centered")

if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.stability = 100
    st.session_state.repair = 2
    st.session_state.log = "Start stacking your Moai tower!"

# ======================
# UI STYLE
# ======================
st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle, #0a0a0a, #001a2b);
    color: white;
}
.block-container {
    background: rgba(255,255,255,0.06);
    backdrop-filter: blur(10px);
    border-radius: 15px;
    padding: 20px;
}
.stButton>button {
    border: 1px solid #00f5ff;
    color: #00f5ff;
    border-radius: 10px;
    transition: 0.2s;
}
.stButton>button:hover {
    background: #00f5ff;
    color: black;
}
</style>
""", unsafe_allow_html=True)

# ======================
# TITLE
# ======================
st.title("🗿 CONCRETE MOAI: STACK RUSH")
st.caption("Build the tallest unstable Moai without collapsing it")

# ======================
# STATS
# ======================
col1, col2, col3 = st.columns(3)
col1.metric("Score", st.session_state.score)
col2.metric("Stability", f"{st.session_state.stability}%")
col3.metric("Repairs", st.session_state.repair)

st.progress(max(0, st.session_state.stability) / 100)

st.write("---")

# ======================
# GAME LOGIC
# ======================
def collapse_check(chance):
    if random.random() < chance:
        damage = random.randint(15, 40)
        st.session_state.stability -= damage
        st.session_state.log = f"💥 Tower hit (-{damage} stability)"
        return True
    return False

# ======================
# BUTTONS
# ======================
c1, c2, c3, c4 = st.columns(4)

# 🟦 SAFE BLOCK
if c1.button("🟦 Safe"):
    st.session_state.score += 1
    st.session_state.stability -= random.randint(3, 7)
    collapse_check(0.1)
    st.session_state.log = "🟦 Safe block placed"

# 🟥 HEAVY BLOCK
if c2.button("🟥 Heavy"):
    st.session_state.score += 3
    st.session_state.stability -= random.randint(8, 15)
    collapse_check(0.25)
    st.session_state.log = "🟥 Heavy block stacked"

# ⚡ BOOST
if c3.button("⚡ Boost"):
    st.session_state.score += 5
    st.session_state.stability -= random.randint(12, 25)
    collapse_check(0.4)
    st.session_state.log = "⚡ High risk drop!"

# 🛠️ REPAIR
if c4.button("🛠️ Repair"):
    if st.session_state.repair > 0:
        st.session_state.stability = min(100, st.session_state.stability + 25)
        st.session_state.repair -= 1
        st.session_state.log = "🛠️ Structure repaired"
    else:
        st.session_state.log = "No repairs left!"

# ======================
# END GAME
# ======================
if st.session_state.stability <= 0:
    st.error("💀 TOWER COLLAPSED!")
    st.stop()

if st.session_state.score >= 30:
    st.balloons()
    st.success("🏆 MOAI TOWER COMPLETED!")

# ======================
# LOG
# ======================
st.write("---")
st.info(st.session_state.log)
