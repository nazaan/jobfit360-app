import streamlit as st
from utils.file_loader import load_file

st.set_page_config(page_title="JobFit360", layout="wide")

st.title("💼 JobFit360: CV & JD Analyzer")

# ------------------------
# Sidebar - file upload
# ------------------------
st.sidebar.header("Upload Files")
cv_file = st.sidebar.file_uploader("Upload Candidate CV (PDF or TXT)", type=["pdf", "txt"])
jd_file = st.sidebar.file_uploader("Upload Job Description (PDF or TXT)", type=["pdf", "txt"])

# ------------------------
# Display uploaded text
# ------------------------
st.header("Uploaded Documents Preview")
if cv_file:
    cv_text = load_file(cv_file)
    st.subheader("Candidate CV")
    st.text_area("CV Text", cv_text, height=200)
else:
    st.info("Upload a Candidate CV to preview text.")

if jd_file:
    jd_text = load_file(jd_file)
    st.subheader("Job Description")
    st.text_area("JD Text", jd_text, height=200)
else:
    st.info("Upload a Job Description to preview text.")

# ------------------------
# Placeholder for analysis
# ------------------------
st.header("Analysis")
if st.button("Analyze"):
    if cv_file and jd_file:
        st.info("Analysis will run here soon (similarity + AI feedback).")
    else:
        st.warning("Please upload both CV and JD to run analysis.")
