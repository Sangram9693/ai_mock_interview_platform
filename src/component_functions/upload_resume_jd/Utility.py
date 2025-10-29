import streamlit as st
from constants.StringConstant import JOB_TITLE_PLACEHOLDER, JOB_DESCRIPTION_PLACEHOLDER, JOB_LABEL, JOB_DESCRIPTION_LABEL, RESUME_LABEL, RESUME_UPLOAD_MESSAGE
from pypdf import PdfReader

def jd_conatiner():
    with st.container(border=True, vertical_alignment="center", horizontal_alignment="center", height=400):
        job_input = st.text_input(label=JOB_LABEL, placeholder=JOB_TITLE_PLACEHOLDER)
        job_dec = st.text_area(label=JOB_DESCRIPTION_LABEL, placeholder=JOB_DESCRIPTION_PLACEHOLDER)
       
        st.session_state.job_details["job_title"] = job_input
        st.session_state.job_details["job_description"] = job_dec
        


def resume_conatiner():
    with st.container(border=True, vertical_alignment="center", horizontal_alignment="center", height=400):
        resume = st.file_uploader(label=RESUME_LABEL, type=["pdf"], accept_multiple_files=False, width="stretch")
        if resume is not None:
            reader = PdfReader(resume)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            st.success(RESUME_UPLOAD_MESSAGE)
            st.session_state.job_details["resume_content"] = text