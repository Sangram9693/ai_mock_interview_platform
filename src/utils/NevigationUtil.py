import streamlit as st

def nevigate_component(navigate, component: str):
    navigate(component)
    st.rerun()