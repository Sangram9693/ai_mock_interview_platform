import streamlit as st


def init_state():
    """Initialize core app states."""
    defaults = {
        "page": "upload",
        "job_details": {},
        "interview_data": {},
    }
    for key, value in defaults.items():
        st.session_state.setdefault(key, value)

