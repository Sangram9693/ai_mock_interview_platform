import streamlit as st

def init_state():
    defaults = {
        "page": "upload",
        "interview_data": {},
        "user": {"name": "Sangram", "role": "developer"},
        "theme": "light"
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

def reset_interview():
    st.session_state.interview_data = {}
