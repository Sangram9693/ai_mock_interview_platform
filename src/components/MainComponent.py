import components.UploadResumeJd as uploadResumeJd
import components.Interview as interview
import streamlit as st

st.set_page_config(layout="wide")

PAGES = {
  "interview": interview.render,
  "upload": uploadResumeJd.render,
}