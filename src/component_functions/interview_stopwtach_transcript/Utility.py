import streamlit as st
import time
from constants.StringConstant import INTERVIEW_LABEL,TRANSCRIPT_LABEL,STOPWATCH_TIME,ROBOT_IMAGE_PATH
from datetime import timedelta
from utils.NevigationUtil import nevigate_component
from constants.AppConstant import MAX_DURATION

def voiceagent_conatiner():
    st.title(INTERVIEW_LABEL)
    with st.container(border=True, vertical_alignment="center", horizontal_alignment="center", height=600):
        try:
            st.image(ROBOT_IMAGE_PATH, width=600)
        except Exception:
            st.write("Avatar image not found.")

def transcript_conatiner():
    st.title(TRANSCRIPT_LABEL)
    with st.container(border=True, vertical_alignment="center", horizontal_alignment="center", height=600):
        st.write("Transcript will appear here...")

def end_conatiner():
    st.markdown(f"### ⏰ {format_time(st.session_state.elapsed)}")
    with st.container(border=False, vertical_alignment="center", horizontal_alignment="center", height=600):
        st.button("End Interview")

def format_time(seconds: float) -> str:
    """Format seconds to HH:MM:SS"""
    return str(timedelta(seconds=int(seconds)))


def reset_interview():
    """Reset interview and timing data."""
    st.session_state.job_details = {}
    st.session_state.interview_data = {}
    st.session_state.start_time = time.time()
    st.session_state.elapsed = 0.0
    st.session_state.end_time = None
    st.session_state.stopped = False


def init_session():
    """Initialize Streamlit session state safely."""
    st.session_state.setdefault("start_time", time.time())
    st.session_state.setdefault("elapsed", 0.0)
    st.session_state.setdefault("end_time", None)
    st.session_state.setdefault("stopped", False)


def update_elapsed_time():
    """Update elapsed time or stop automatically after reaching max duration."""
    if not st.session_state.stopped and st.session_state.end_time is None:
        st.session_state.elapsed = time.time() - st.session_state.start_time

        if st.session_state.elapsed >= MAX_DURATION:
            st.session_state.elapsed = MAX_DURATION
            st.session_state.end_time = time.time()
            st.session_state.stopped = True
            return True  # Auto stop triggered
    return False


def stop_interview():
    """Stop interview manually."""
    st.session_state.stopped = True
    st.session_state.end_time = time.time()
    st.session_state.elapsed = st.session_state.end_time - st.session_state.start_time


def auto_navigate_if_stopped(navigate):
    """If interview is stopped or max time reached, navigate back."""
    if st.session_state.stopped or (
        st.session_state.end_time is not None and st.session_state.elapsed >= MAX_DURATION
    ):
        nevigate_component(navigate, "upload")
        reset_interview()