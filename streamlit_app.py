import streamlit as st
from utils.file_loader import load_file
from utils.similarity import compute_similarity
from utils.ai_feedback import generate_feedback

# ------------------------
# Streamlit page config
# ------------------------
st.set_page_config(page_title="JobFit360", layout="wide")
st.title("💼 JobFit360: CV & JD Analyzer")

# ------------------------
# Sidebar - file upload
# ------------------------
st.sidebar.header("Upload Files")
cv_file = st.sidebar.file_uploader("Upload Candidate CV (PDF or TXT)", type=["pdf", "txt"])
jd_file = st.sidebar.file_uploader("Upload Job Description (PDF or TXT)", type=["pdf", "txt"])

# ------------------------
# Load file content
# ------------------------
cv_text = ""
jd_text = ""

if cv_file:
    cv_text = load_file(cv_file)
if jd_file:
    jd_text = load_file(jd_file)

# ------------------------
# Display uploaded text
# ------------------------
st.header("Uploaded Documents Preview")
if cv_text:
    st.subheader("Candidate CV")
    st.text_area("CV Text", cv_text, height=200)
else:
    st.info("Upload a Candidate CV to preview text.")

if jd_text:
    st.subheader("Job Description")
    st.text_area("JD Text", jd_text, height=200)
else:
    st.info("Upload a Job Description to preview text.")

# ------------------------
# Analyze button
# ------------------------
st.header("Analysis")
if st.button("Analyze"):
    if not cv_text or not jd_text:
        st.error("Please upload both CV and JD before analyzing.")
    else:
        # Compute similarity
        similarity = compute_similarity(cv_text, jd_text)
        st.subheader("CV–JD Similarity")
        st.write(f"{similarity:.2f}%")

        # AI feedback (Hugging Face or fallback)
        st.subheader("AI Feedback")
        with st.spinner("Generating AI feedback..."):
            feedback = generate_feedback(cv_text, jd_text)
        st.text_area("Feedback", feedback, height=250)
