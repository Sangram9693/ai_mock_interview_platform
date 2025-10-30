import streamlit as st
import time
from utils.NevigationUtil import nevigate_component
from constants.AppConstant import MAX_DURATION


def init_session():
    """Initialize Streamlit session state safely."""
    st.session_state.setdefault("start_time", time.time())
    st.session_state.setdefault("elapsed", 0.0)
    st.session_state.setdefault("end_time", None)
    st.session_state.setdefault("stopped", False)


def update_elapsed_time():
    """Update elapsed time or stop automatically after reaching max duration."""
    if st.session_state.end_time is None:
        st.session_state.elapsed = time.time() - st.session_state.start_time

        if st.session_state.elapsed >= MAX_DURATION:
            st.session_state.elapsed = MAX_DURATION
            st.session_state.end_time = time.time()
            return True  # Auto stop triggered
    return False


def stop_interview():
    """Stop interview manually."""
    st.session_state.stopped = True
    st.session_state.end_time = time.time()
    st.session_state.elapsed = st.session_state.end_time - st.session_state.start_time


def auto_navigate_if_stopped(navigate):
    """If interview is over, navigate and reset session."""
    if st.session_state.end_time is not None and st.session_state.elapsed >= MAX_DURATION:
        nevigate_component(navigate, 'upload')
        intialize_session_state()

def intialize_session_state():
    if "start_time" not in st.session_state:
        st.session_state.start_time = time.time()
    if "elapsed" not in st.session_state:
        st.session_state.elapsed = 0.0
    if "end_time" not in st.session_state:
        st.session_state.end_time = None