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

# ============================
# 3. Train Model (Simple)
# ============================
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

if st.button("Train Logistic Regression"):
    if uploaded_file and target_col:
        st.info("Training model...")
        
        X = df.drop(columns=[target_col])
        y = df[target_col]
        
        # Only numeric columns for now
        X = X.select_dtypes(include="number")
        
        if X.shape[1] == 0:
            st.error("No numeric features available for training.")
        else:
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
            
            model = LogisticRegression(max_iter=1000)
            model.fit(X_train, y_train)
            
            preds = model.predict(X_test)
            acc = accuracy_score(y_test, preds)
            
            st.success(f"Training complete! Accuracy: {acc:.2f}")
            st.text("Classification Report:")
            st.text(classification_report(y_test, preds))
    else:
        st.warning("Please upload a dataset and select a target column first.")

