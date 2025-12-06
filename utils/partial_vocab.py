# utils/partial_vocab.py

# Maps base JD keywords → list of alternative words/phrases
# Used to calculate Partial Match instead of marking as Missing
PARTIAL_VOCAB = {
    "communication": ["presented", "explained", "discussed", "reported", "stakeholder", "articulated", "collaborated"],
    "leadership": ["managed", "mentored", "coordinated", "supervised", "led", "organized"],
    "analytics": ["analyzed", "evaluated", "interpreted", "modeled", "optimized"],
    "sales": ["sold", "prospected", "negotiated", "closed deals", "account management"],
    "marketing": ["campaign", "promoted", "advertised", "market research", "branding"],
    "programming": ["coded", "developed", "engineered", "built", "implemented", "scripted"],
    "HR": ["hiring", "recruitment", "onboarding", "employee engagement", "training"],
    "consultancy": ["advised", "consulted", "strategized", "recommended"],
    "datascience": ["model", "prediction", "machine learning", "statistics", "AI", "data analysis"],
    "accounting": ["audited", "bookkeeping", "finance", "budgeted", "reconciled"],
    "education": ["taught", "instructed", "curriculum", "lesson planning"],
    "socialsciences": ["researched", "surveyed", "analyzed behavior", "qualitative", "quantitative"],
}
