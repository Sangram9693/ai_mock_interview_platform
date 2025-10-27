import streamlit as st
from elements.Button import Button
from constants.StringConstant import TITLE

st.title(TITLE)

if Button("Save"):
    st.subheader("Testing")