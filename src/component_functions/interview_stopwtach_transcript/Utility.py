import streamlit as st
from constants.StringConstant import INTERVIEW_LABEL,TRANSCRIPT_LABEL,STOPWATCH_TIME,ROBOT_IMAGE_PATH
from datetime import timedelta
import time

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



