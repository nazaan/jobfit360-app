# utils/similarity.py

from sentence_transformers import SentenceTransformer, util
import nltk
from nltk.tokenize import sent_tokenize

# Download punkt tokenizer once
nltk.download('punkt')

# Load a small, fast model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def compute_similarity(cv_text: str, jd_text: str) -> float:
    """
    Computes CV–JD similarity as a percentage (0–100).
    Uses sentence-level embeddings for precise semantic matching.
    """
    if not cv_text or not jd_text:
        return 0.0

    # Split texts into sentences
    cv_sents = sent_tokenize(cv_text)
    jd_sents = sent_tokenize(jd_text)

    # Encode sentences
    cv_embs = model.encode(cv_sents, convert_to_tensor=True)
    jd_embs = model.encode(jd_sents, convert_to_tensor=True)

    # Cosine similarity matrix
    sim_matrix = util.cos_sim(cv_embs, jd_embs)

    # For each JD sentence, take max similarity to any CV sentence
    max_per_jd = sim_matrix.max(dim=0).values

    # Average similarity across all JD sentences
    avg_similarity = max_per_jd.mean().item()

    return avg_similarity * 100  # as percentage
