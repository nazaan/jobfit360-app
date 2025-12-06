# utils/similarity.py

from sentence_transformers import SentenceTransformer, util
import nltk
from nltk.tokenize import sent_tokenize
import os

# Force NLTK to use a local directory inside Streamlit Cloud
nltk_data_dir = os.path.join(os.getcwd(), "nltk_data")
os.makedirs(nltk_data_dir, exist_ok=True)
nltk.data.path.append(nltk_data_dir)

# Download punkt tokenizer if not already present
nltk.download('punkt', download_dir=nltk_data_dir, quiet=True)

# Load small sentence transformer model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def compute_similarity(cv_text: str, jd_text: str) -> float:
    if not cv_text or not jd_text:
        return 0.0

    # Split texts into sentences
    cv_sents = sent_tokenize(cv_text)
    jd_sents = sent_tokenize(jd_text)

    # Encode sentences
    cv_embs = model.encode(cv_sents, convert_to_tensor=True)
    jd_embs = model.encode(jd_sents, convert_to_tensor=True)

    # Cosine similarity
    sim_matrix = util.cos_sim(cv_embs, jd_embs)

    # For each JD sentence, take max similarity to any CV sentence
    max_per_jd = sim_matrix.max(dim=0).values

    # Average similarity across JD sentences
    avg_similarity = max_per_jd.mean().item()

    return avg_similarity * 100
