# streamlit_app.py

import streamlit as st
from utils.file_loader import load_file
from utils.similarity import compute_similarity

st.set_page_config(page_title="JobFit360", layout="wide")
st.title("💼 JobFit360 – CV vs JD Analyzer")

# ------------------------
# Sidebar - file upload
# ------------------------
st.sidebar.header("Upload Files")
cv_file = st.sidebar.file_uploader("Upload Candidate CV (PDF or TXT)", type=["pdf", "txt"])
jd_file = st.sidebar.file_uploader("Upload Job Description (PDF or TXT)", type=["pdf", "txt"])

# ------------------------
# Load text from files
# ------------------------
cv_text = load_file(cv_file) if cv_file else ""
jd_text = load_file(jd_file) if jd_file else ""

# ------------------------
# Display uploaded text
# ------------------------
st.header("Uploaded Documents Preview")
if cv_file:
    st.subheader("Candidate CV")
    st.text_area("CV Text", cv_text, height=200)
else:
    st.info("Upload a Candidate CV to preview text.")

if jd_file:
    st.subheader("Job Description")
    st.text_area("JD Text", jd_text, height=200)
else:
    st.info("Upload a Job Description to preview text.")

# ------------------------
# Compute similarity
# ------------------------
st.header("Analysis")
if st.button("Analyze"):
    if not cv_text or not jd_text:
        st.error("Please upload both CV and JD before analyzing.")
    else:
        results = compute_similarity(cv_text, jd_text)

        # Display scores per category
        for category in ["skills", "responsibilities", "education"]:
            st.subheader(f"{category.capitalize()} Coverage")
            coverage = results[category]
            score = results[f"{category}_score"]
            st.write(f"**Score:** {score:.2f} / 1.00")
            
            # Create table
            table_data = []
            for item, level in coverage.items():
                table_data.append([item, level])
            
            st.table(table_data)

        # Overall score (average of categories)
        valid_scores = [results[f"{c}_score"] for c in ["skills","responsibilities","education"] if results[f"{c}_score"] is not None]
        if valid_scores:
            overall_score = sum(valid_scores) / len(valid_scores)
            st.subheader("Overall Match Score")
            st.write(f"**{overall_score:.2f} / 1.00**")
