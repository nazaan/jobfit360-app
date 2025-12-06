import streamlit as st

# Test imports
try:
    from utils.file_loader import load_file
    from utils.similarity import compute_similarity
    from utils.transferable_clusters import TRANSFERRABLE_CLUSTERS
    st.write("✅ All imports work")
except Exception as e:
    st.error(f"Import error: {e}")

st.title("JobFit360 Minimal Test")
st.write("If you see this, Streamlit runs and imports succeed.")
