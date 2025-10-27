import streamlit as st
from elements.Button import Button
from utils.NevigationUtil import nevigate_component

def render(navigate):
    st.title("Interview Page")

    if Button("Go Back"):
        nevigate_component(navigate, 'upload')
