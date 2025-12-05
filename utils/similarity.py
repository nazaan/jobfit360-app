from sentence_transformers import SentenceTransformer, util

# Load model once (small model for speed)
model = SentenceTransformer('all-MiniLM-L6-v2')

def compute_similarity(text1: str, text2: str) -> float:
    """
    Compute cosine similarity between two texts.
    Returns a percentage (0-100).
    """
    if not text1 or not text2:
        return 0.0

    embeddings1 = model.encode(text1, convert_to_tensor=True)
    embeddings2 = model.encode(text2, convert_to_tensor=True)

    cosine_score = util.cos_sim(embeddings1, embeddings2)
    return float(cosine_score[0][0] * 100)

