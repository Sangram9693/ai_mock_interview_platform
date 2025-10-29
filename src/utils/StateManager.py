import streamlit as st

def init_state():
    defaults = {
        "page": "upload",
        "job_details": {},
        "interview_data": {},
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

def reset_interview():
    st.session_state.job_details = {}
    st.session_state.interview_data = {}
