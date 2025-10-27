import streamlit as st
from elements.Button import Button
from utils.NevigationUtil import nevigate_component

def render(navigate):
    st.title("Upload Page")
    print(st.session_state.get("user")['name'])

    if Button("Start Interview"):
        nevigate_component(navigate, "interview")
