import streamlit as st
import time
from elements.Button import Button
from utils.NevigationUtil import nevigate_component
from constants.StringConstant import INTERVIEW_END_BUTTON,INTERVIEW_ENDED, GO_BACK
from component_functions.interview_stopwtach_transcript.Utility import (
    voiceagent_conatiner,
    transcript_conatiner,
    format_time,
)
from utils.StateManager import (
    init_session,
    update_elapsed_time,
    stop_interview,
    auto_navigate_if_stopped,
)

st.set_page_config(layout="wide")


def render(navigate):
    init_session()  # initialize all session vars

    with st.container():
        vaCol, endCol, transCol = st.columns(3, vertical_alignment="center", width="stretch")

        # Update time and handle auto-stop
        auto_stopped = update_elapsed_time()
        if auto_stopped:
            auto_navigate_if_stopped(navigate)

        # Stopwatch + voice agent
        with vaCol:
            voiceagent_conatiner()

        # End/Go Back section
        with endCol:
            st.write("")
            left, center, right = st.columns([1, 2, 1])
            with center:
                st.markdown(f"### ⏰ {format_time(st.session_state.elapsed)}")
                if not st.session_state.stopped:
                    if st.button(INTERVIEW_END_BUTTON,use_container_width=True):
                        stop_interview()
                        st.rerun()
                else:
                    st.success(INTERVIEW_ENDED)
                    if Button(GO_BACK):
                        nevigate_component(navigate, 'upload')

        # Transcript section
        with transCol:
            transcript_conatiner()

        # Refresh every second if still running
        if st.session_state.end_time is None:
            time.sleep(1)
            st.rerun()
