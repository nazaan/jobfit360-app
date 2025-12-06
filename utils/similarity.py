# utils/similarity.py

from utils.keywords import SKILLS_LC, RESPONSIBILITIES_LC, EDUCATION_LC, PROXIES, EDU_SYNONYMS
from utils.transferable_clusters import TRANSFERABLE_CLUSTERS
import re

COVERAGE_WEIGHTS = {
    "Strong Match": 1,
    "Transferable Skill": 0.8,
    "Partial Match": 0.5,
    "Missing": 0
}


def match_transferable(item):
    """Return coverage_level if item is in any transferable cluster"""
    item_lower = item.lower()
    for cluster in TRANSFERABLE_CLUSTERS:
        if item_lower in [x.lower() for x in cluster["cluster"]]:
            return cluster["coverage_level"]
    return None


def match_partial(item, cv_tokens):
    """
    Check if any proxy term matches tokens in CV.
    Return True if partial match found.
    """
    item_lower = item.lower()
    if item_lower in PROXIES:
        proxies = PROXIES[item_lower]
        for p in proxies:
            if any(p in t for t in cv_tokens):
                return True
    return False


def compute_category_score(jd_items, cv_tokens, category=None):
    coverage = {}
    total_score = 0
    matched_edu = False  # track if we already matched an education

    for item in jd_items:
        item_lower = item.lower()

        if category == "education":
            if not matched_edu:
                # check synonyms
                matched = False
                if item_lower in EDU_SYNONYMS:
                    for syn in EDU_SYNONYMS[item_lower]:
                        if any(syn in t for t in cv_tokens):
                            matched = True
                            break
                if matched:
                    level = "Strong Match"
                    matched_edu = True  # prevent further "Missing" on other items
                elif match_partial(item_lower, cv_tokens):
                    level = "Partial Match"
                else:
                    level = "Missing"
            else:
                # already matched one edu item → mark others as ignored or skip
                level = "Strong Match"  # or None if you prefer
        else:
            if item_lower in cv_tokens:
                level = "Strong Match"
            elif match_transferable(item_lower):
                level = "Transferable Skill"
            elif match_partial(item_lower, cv_tokens):
                level = "Partial Match"
            else:
                level = "Missing"

        coverage[item] = level
        total_score += COVERAGE_WEIGHTS.get(level, 0)

    category_score = total_score / len(jd_items) if jd_items else None
    return coverage, category_score



def compute_similarity(cv_text, jd_text):
    """
    Compute coverage and score per category.
    Returns dictionary:
    {
        "skills": {item: coverage_level, ...},
        "skills_score": float,
        "responsibilities": {item: coverage_level, ...},
        "responsibilities_score": float,
        "education": {item: coverage_level, ...},
        "education_score": float
    }
    """
    # Simple tokenization (lowercase, alphanumeric)
    cv_tokens = re.findall(r'\w+', cv_text.lower())
    jd_tokens = re.findall(r'\w+', jd_text.lower())

    # Filter JD tokens per category
    jd_skills = [t for t in jd_tokens if t in SKILLS_LC]
    jd_responsibilities = [t for t in jd_tokens if t in RESPONSIBILITIES_LC]
    jd_education = [t for t in jd_tokens if t in EDUCATION_LC]

    results = {}

    results["skills"], results["skills_score"] = compute_category_score(jd_skills, cv_tokens)
    results["responsibilities"], results["responsibilities_score"] = compute_category_score(jd_responsibilities, cv_tokens)
    results["education"], results["education_score"] = compute_category_score(jd_education, cv_tokens, category="education")

    return results
