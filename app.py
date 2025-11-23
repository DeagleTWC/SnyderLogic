# app.py — SnyderLogic live demo
# Deploy this file + requirements.txt → instant working demo

import streamlit as st
from snyderlogic import SnyderLogic  # assumes your file is named snyderlogic.py

st.set_page_config(page_title="SnyderLogic", layout="centered")
st.title("SnyderLogic — Adaptive Reasoning Demo")
st.caption("Type any fact. Try conflicting statements (e.g. Paris vs Marseille)")

if "sl" not in st.session_state:
    st.session_state.sl = SnyderLogic(inquiry_budget=500)

sl = st.session_state.sl

statement = st.text_input("Enter a belief / fact", placeholder="The capital of France is Paris")

col1, col2 = st.columns([1, 3])
if col1.button("Update", type="primary"):
    with st.container():
        result = sl.update(statement)
        st.write(result)
        st.caption(f"Budget remaining: {sl.inquiry_budget} | Coherence: {sl.coherence:.3f}")

if st.button("Run classic conflict test"):
    sl = SnyderLogic()
    st.session_state.sl = sl
    tests = [
        "The capital of France is Paris",
        "The capital of France is Marseille",
        "Water is wet",
        "2 + 2 = 5"
    ]
    for stmt in tests:
        st.write(f"→ {stmt}")
        st.code(sl.update(stmt), language=None)

if st.download_button("Export knowledge.json", data=sl.to_json(), file_name="snyder_knowledge.json"):
    st.success("Downloaded")
