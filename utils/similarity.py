# utils/similarity.py
from sentence_transformers import SentenceTransformer, util
import re

# Load small, fast model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def split_sentences(text: str):
    """Simple regex-based sentence splitter"""
    # Split on '.', '?', '!', followed by space or end of line
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    return [s for s in sentences if s]

def compute_similarity(cv_text: str, jd_text: str) -> float:
    if not cv_text or not jd_text:
        return 0.0

    cv_sents = split_sentences(cv_text)
    jd_sents = split_sentences(jd_text)

    cv_embs = model.encode(cv_sents, convert_to_tensor=True)
    jd_embs = model.encode(jd_sents, convert_to_tensor=True)

    sim_matrix = util.cos_sim(cv_embs, jd_embs)
    max_per_jd = sim_matrix.max(dim=0).values
    avg_similarity = max_per_jd.mean().item()
    return avg_similarity * 100
