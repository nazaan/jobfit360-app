# utils/similarity.py
from sentence_transformers import SentenceTransformer, util
import nltk
from nltk.tokenize import sent_tokenize
import tempfile

# Use Streamlit's temp folder for nltk data
nltk_data_dir = tempfile.mkdtemp()
nltk.data.path.append(nltk_data_dir)
nltk.download('punkt', download_dir=nltk_data_dir, quiet=True)

# Load small, fast sentence-transformer model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def compute_similarity(cv_text: str, jd_text: str) -> float:
    if not cv_text or not jd_text:
        return 0.0

    cv_sents = sent_tokenize(cv_text)
    jd_sents = sent_tokenize(jd_text)

    cv_embs = model.encode(cv_sents, convert_to_tensor=True)
    jd_embs = model.encode(jd_sents, convert_to_tensor=True)

    sim_matrix = util.cos_sim(cv_embs, jd_embs)
    max_per_jd = sim_matrix.max(dim=0).values
    avg_similarity = max_per_jd.mean().item()
    return avg_similarity * 100
