import streamlit as st
from snyderlogic.core import SnyderLogic

st.title("SnyderLogic Demo")
sl = SnyderLogic()
statement = st.text_input("Enter belief to update:")
if st.button("Update"):
    result = sl.update(statement)
    st.write(result)
st.download_button("Export Knowledge", json.dumps(sl.beliefs, indent=2), "snyder.json")
