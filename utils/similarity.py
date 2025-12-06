# utils/similarity.py
from utils.keywords import SKILLS_LC, RESPONSIBILITIES_LC, EDUCATION_LC, PROXIES
from utils.transferable_clusters import TRANSFERABLE_CLUSTERS

COVERAGE_WEIGHTS = {
    "Strong Match": 1,
    "Transferable Skill": 0.8,
    "Partial Match": 0.5,
    "Missing": 0
}

def match_transferable(item):
    """Return coverage_level if item is in any transferable cluster"""
    for cluster in TRANSFERABLE_CLUSTERS:
        if item in [x.lower() for x in cluster["cluster"]]:
            return cluster["coverage_level"]
    return None

def match_partial(item, cv_tokens):
    """
    Check if any proxy term matches tokens in CV
    Return True if partial match found
    """
    item_lower = item.lower()
    if item_lower in PROXIES:
        proxies = PROXIES[item_lower]
        for p in proxies:
            if any(p in t for t in cv_tokens):
                return True
    return False

def compute_category_score(jd_items, cv_tokens):
    coverage = {}
    total_score = 0

    for item in jd_items:
        item_lower = item.lower()
        if item_lower in cv_tokens:
            level = "Strong Match"
        elif match_transferable(item_lower):
            level = "Transferable Skill"
        elif match_partial(item_lower, cv_tokens):
            level = "Partial Match"
        else:
            level = "Missing"

        coverage[item] = level
        total_score += COVERAGE_WEIGHTS[level]

    if jd_items:
        category_score = total_score / len(jd_items)
    else:
        category_score = None
    return coverage, category_score

def compute_similarity(cv_text, jd_text):
    """
    Compute coverage and score per category.
    Returns dictionary:
    {
        "skills": {"coverage": {...}, "score": ...},
        "responsibilities": {"coverage": {...}, "score": ...},
        "education": {"coverage": {...}, "score": ...}
    }
    """
    cv_tokens = [t.lower() for t in cv_text.split()]
    jd_tokens = [t.lower() for t in jd_text.split()]

    results = {}

    results["skills"], results["skills_score"] = compute_category_score(SKILLS_LC, cv_tokens)
    results["responsibilities"], results["responsibilities_score"] = compute_category_score(RESPONSIBILITIES_LC, cv_tokens)
    results["education"], results["education_score"] = compute_category_score(EDUCATION_LC, cv_tokens)

    return results
