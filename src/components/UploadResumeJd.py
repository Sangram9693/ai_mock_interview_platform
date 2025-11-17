import streamlit as st
from elements.Button import Button
from utils.NevigationUtil import nevigate_component
from component_functions.upload_resume_jd.Utility import jd_conatiner, resume_conatiner
from llms.combine import generate_interview_questions
import streamlit as st

st.set_page_config(layout="wide")

def render(navigate):
    with st.container():
        jdCol, resumeCol = st.columns(2, vertical_alignment="center", width="stretch")

        with jdCol:
            jd_conatiner()

        with resumeCol:
            resume_conatiner()
    
    with st.container(horizontal=True, horizontal_alignment="right"):
        job_details = st.session_state.get("job_details", {})
        is_job_details_complete = all(
            job_details.get(field, "").strip()
            for field in ["job_title", "job_description", "resume_content"]
        )

        is_disable = not is_job_details_complete

        if Button("Start Interview", disabled=is_disable):
            with st.spinner("Starting Your Interview... Please Wait..."):
                result = generate_interview_questions(str(st.session_state.get("job_details")))
                st.session_state.interview_data = result
                nevigate_component(navigate, "interview")
            



        
