import streamlit as st

def Button(label: str, type: str = 'primary', disabled=False):
    return st.button(label=label, type=type, disabled=disabled)
