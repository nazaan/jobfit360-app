import streamlit as st
from utils.file_loader import load_file
from utils.similarity import compute_similarity
from utils.transferable_clusters import TRANSFERABLE_CLUSTERS

# ------------------------
# Helpers
# ------------------------
def get_transferable_explanation(item):
    """Return explanation if item is in any transferable cluster"""
    for cluster in TRANSFERABLE_CLUSTERS:
        if item.lower() in [x.lower() for x in cluster["cluster"]]:
            return cluster["explanation"]
    return ""

# ------------------------
# Page setup
# ------------------------
st.set_page_config(page_title="JobFit360", layout="wide")
st.title("💼 JobFit360: CV & JD Analyzer")

# ------------------------
# Sidebar - file upload
# ------------------------
st.sidebar.header("Upload Files")
cv_file = st.sidebar.file_uploader("Candidate CV (PDF or TXT)", type=["pdf", "txt"])
jd_file = st.sidebar.file_uploader("Job Description (PDF or TXT)", type=["pdf", "txt"])

cv_text = load_file(cv_file) if cv_file else ""
jd_text = load_file(jd_file) if jd_file else ""

# ------------------------
# Preview uploaded text
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
# Analysis
# ------------------------
if st.button("Analyze"):
    if not cv_text or not jd_text:
        st.error("Please upload both CV and JD before analyzing.")
    else:
        results = compute_similarity(cv_text, jd_text)

        # Display per-category score
        st.subheader("Category Scores")
        for cat in ["skills", "responsibilities", "education"]:
            score = results[f"{cat}_score"]
            st.write(f"**{cat.capitalize()}**: {score*100:.1f}%" if score is not None else "N/A")

        # Display coverage tables with explanations
        st.subheader("Coverage Table with Explanations")
        for cat in ["skills", "responsibilities", "education"]:
            st.write(f"**{cat.capitalize()}**")
            coverage = results[cat]
            table_lines = []
            for item, level in coverage.items():
                symbol = {
                    "Strong Match": "✅",
                    "Transferable Skill": "🔄",
                    "Partial Match": "⚠",
                    "Missing": "❌"
                }[level]

                explanation = get_transferable_explanation(item) if level == "Transferable Skill" else ""
                line = f"{symbol} {item}"
                if explanation:
                    line += f" → {explanation}"
                table_lines.append(line)

            st.text_area(f"{cat.capitalize()} Coverage", "\n".join(table_lines), height=250)
