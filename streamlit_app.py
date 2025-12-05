import streamlit as st
import pandas as pd

from utils.data_loader import load_csv

st.set_page_config(page_title="JobFit360 UI", layout="wide")

st.title("🧪 JobFit360 Dashboard (Starter Version)")

st.write(
    """
    This is your starter interface for running ML experiments.
    As you build more features, you will add:
    - Model training UI
    - Metrics visualization
    - Experiment comparison
    - Model saving/loading
    - Hyperparameter settings
    """
)

# ============================
# 1. Upload Dataset
# ============================
st.header("📁 1. Upload Dataset")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = load_csv(uploaded_file)
    st.success("File loaded successfully.")
    st.dataframe(df.head())

    # Show shape
    st.write(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

    # Select target column
    st.header("🎯 2. Select Target Column")
    target_col = st.selectbox("Choose target variable:", df.columns)

    if target_col:
        st.info(f"Selected target: {target_col}")

# ============================
# Footer
# ============================
st.write("---")
st.caption("Starter JobFit360 UI • Built with Streamlit")
