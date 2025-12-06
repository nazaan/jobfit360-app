# utils/matcher.py

import re
from collections import defaultdict
from .transferable_clusters import TRANSFERABLE_CLUSTERS
from .partial_vocab import PARTIAL_VOCAB
from .base_vocab import SKILLS, RESPONSIBILITIES, EDUCATION

# ----------------------------
#   Basic Normalization
# ----------------------------

def normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9+.# ]", " ", text)
    return text


def tokenize(text: str):
    return normalize(text).split()


# ----------------------------
#   Extraction
# ----------------------------

def extract_category_terms(text: str):
    tokens = tokenize(text)

    extracted = {
        "skills": [],
        "responsibilities": [],
        "education": []
    }

    for token in tokens:
        if token in [s.lower() for s in SKILLS]:
            extracted["skills"].append(token)
        if token in [r.lower() for r in RESPONSIBILITIES]:
            extracted["responsibilities"].append(token)
        if token in [e.lower() for e in EDUCATION]:
            extracted["education"].append(token)

    return extracted


# ----------------------------
#   Transferable Lookup
# ----------------------------

def check_transferable(jd_item, cv_items):
    jd_item_low = jd_item.lower()
    cv_items_low = [c.lower() for c in cv_items]

    for cluster in TRANSFERABLE_CLUSTERS:
        cluster_low = [x.lower() for x in cluster["cluster"]]

        if jd_item_low in cluster_low:
            # direct transferable match inside cluster
            for cv_item in cv_items_low:
                if cv_item in cluster_low:
                    return True
    return False


# ----------------------------
#   Partial Match Lookup
# ----------------------------

def check_partial(jd_item, cv_text):
    jd_item_low = jd_item.lower()

    if jd_item_low not in PARTIAL_VOCAB:
        return False

    synonyms = PARTIAL_VOCAB[jd_item_low]

    cv_tokens = tokenize(cv_text)

    for syn in synonyms:
        if syn.lower() in cv_tokens:
            return True

    return False


# ----------------------------
#   Match Classification
# ----------------------------

def classify_item(jd_item, cv_items, cv_text):
    jd_item_low = jd_item.lower()
    cv_items_low = [c.lower() for c in cv_items]

    # Strong
    if jd_item_low in cv_items_low:
        return "Strong Match", 1.0

    # Transferable
    if check_transferable(jd_item, cv_items):
        return "Transferable Skill", 0.8

    # Partial
    if check_partial(jd_item, cv_text):
        return "Partial Match", 0.5

    # Missing
    return "Missing", 0.0


# ----------------------------
#   Full Matching Process
# ----------------------------

def match_cv_to_jd(jd_text: str, cv_text: str):
    jd_ex = extract_category_terms(jd_text)
    cv_ex = extract_category_terms(cv_text)

    results = {
        "skills": [],
        "responsibilities": [],
        "education": [],
        "scores": {
            "skills": 0,
            "responsibilities": 0,
            "education": 0
        }
    }

    # For each category, compute matches
    for category in ["skills", "responsibilities", "education"]:
        jd_items = list(set(jd_ex[category]))  # unique
        cv_items = list(set(cv_ex[category]))

        if len(jd_items) == 0:
            continue

        total_points = 0
        max_points = len(jd_items) * 1.0  # strong = 1 point

        for item in jd_items:
            match_type, score = classify_item(item, cv_items, cv_text)
            total_points += score

            results[category].append({
                "item": item,
                "match_type": match_type,
                "score": score
            })

        results["scores"][category] = round(total_points / max_points, 3)

    return results

