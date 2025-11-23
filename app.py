import streamlit as st
from snyderlogic import SnyderLogic  # Assumes file in same dir

st.title("🧠 SnyderLogic Demo: Adaptive Reasoning Live")
sl = SnyderLogic()

if st.button("Run Adaptive Demo"):
    with st.container():
        sl.update_rule("Capital of France", "Paris")
        sl.update_rule("Capital of France", "Marseille")
        sl.update_rule("Water state", "Wet")
        sl.update_rule("Math: 2+2", "5")
        sl.challenge_rules()
        for line in sl.history:
            st.write(line)
    st.download_button("Download Knowledge", json.dumps(sl.rules, indent=2), "snyder.json")

st.sidebar.info(f"Coherence: {sl.coherence:.3f} | Budget: {sl.adaptation_budget}/500")
