import streamlit as st
from elements.Button import Button
from constants.StringConstant import TITLE
from components.MainComponent import PAGES
from utils.StateManager import init_state

# # Initialize page state if not already set
# if "page" not in st.session_state:
#     st.session_state.page = "upload"   # default page

init_state()

# Function to switch page
def navigate(page_name: str):
    st.session_state.page = page_name

# Render appropriet componets
PAGES[st.session_state.page](navigate)
