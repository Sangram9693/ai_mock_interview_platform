import streamlit as st

def Button(label: str, type: str = 'primary'):
    return st.button(label=label, type=type)
