import pandas as pd

def load_csv(uploaded_file):
    """Load a CSV file uploaded through Streamlit."""
    try:
        df = pd.read_csv(uploaded_file)
        return df
    except Exception as e:
        raise ValueError(f"Could not read CSV: {e}")
