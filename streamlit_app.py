import streamlit as st
from utils.file_loader import load_file 
import os 
from utils.ai_feedback import generate_feedback

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
# Compute similarity
# ------------------------
from utils.similarity import compute_similarity

st.header("Analysis")
if st.button("Analyze"):
    if cv_file and jd_file:
        st.info("Running analysis...")

        # Compute similarity %
        similarity = compute_similarity(cv_text, jd_text)
        st.success(f"🔹 CV ↔ JD Similarity: {similarity:.2f}%")

        # Placeholder for AI feedback (next step)
        st.info("AI-generated feedback will appear here soon.")
    else:
        st.warning("Please upload both CV and JD to run analysis.") 

# Retrieve API key from Streamlit secrets or environment
api_key = st.secrets.get("OPENAI_API_KEY", None)
if api_key is None:
    st.error("OpenAI API key not set. Add it in Streamlit Secrets.")
else:
    with st.spinner("Generating AI feedback..."):
        feedback = generate_feedback(cv_text, jd_text, api_key)
        st.subheader("💡 AI Feedback")
        st.text_area("Feedback", feedback, height=250)


