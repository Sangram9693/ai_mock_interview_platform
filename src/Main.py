import streamlit as st
from elements.Button import Button
from components.MainComponent import PAGES
from utils.StateManager import init_state

init_state()

# Function to switch page
def navigate(page_name: str):
    st.session_state.page = page_name

# Render appropriet componets
PAGES[st.session_state.page](navigate)
