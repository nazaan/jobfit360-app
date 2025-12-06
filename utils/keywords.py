# utils/keywords.py
# Master lists and proxy dictionaries for CV↔JD matching.

print("DEBUG: loading keywords.py")


SKILLS = [
    "Python","R","SQL","Tableau","Power BI","QlikView","Looker",
    "AWS","Azure","Google Cloud Platform","Photoshop","Illustrator",
    "Figma","Sketch","Google Analytics","Adobe Analytics",
    "HubSpot","Marketo","Git","GitHub","GitLab","Bitbucket",
    "MySQL","PostgreSQL","Oracle","MariaDB","Excel","SPSS",
    "Jira","Trello","Asana","Monday.com","ClickUp"
]

RESPONSIBILITIES = [
    "led","managed","supervised","mentored","coordinated",
    "collaborated","presented","reported","delivered","designed",
    "developed","implemented","analyzed","optimized","negotiated",
    "trained","supported","communicated","organized","planned",
    "executed","facilitated","documented","reviewed","monitored"
]

EDUCATION = [
    "bachelor","master","phd","mba","bsc","msc",
    "diploma","certification","pmp","cpa","cfa",
    "high school","associate","degree"
]

# -------------------------
# Proxy terms per category
# Lowercase tokens used for simple deterministic matching
# -------------------------
PROXIES = {
    "communication": [
        "present","presentation","explain","stakeholder","report","documentation",
        "negotiate","workshop","briefing","articulate","speak","write","written"
    ],
    "teamwork": [
        "collaborate","cross-functional","partner","coordinate","support","joint","liaison"
    ],
    "project_management": [
        "timeline","milestone","deliverable","roadmap","sprint","backlog","planning",
        "prioritization","workflow","dependency","scope","execution"
    ],
    "data_analysis": [
        "analysis","insight","insights","reporting","visualization","statistics",
        "modeling","hypothesis","experiment","metric","evaluate","investigate","interpret"
    ],
    "python": ["pandas","numpy","scikit","jupyter","script","scripting","automation","api","backend"],
    "sql": ["query","join","schema","stored procedure","etl","warehouse","relational","table"],
    "cloud": ["deploy","deployment","container","kubernetes","serverless","compute","storage","iam","pipeline","cluster"],
    "design_tools": ["illustrator","photoshop","figma","sketch","wireframe","vector","layout","typography"],
    "marketing": ["campaign","funnel","segmentation","targeting","branding","seo","content","conversion","ab test","a/b test"],
    "sales": ["pipeline","prospecting","crm","closing","negotiation","account management","lead generation","quota"],
    "programming": ["algorithm","codebase","debug","debugging","architecture","refactor","refactoring","api design","testing"],
    "hr": ["recruit","recruiting","onboarding","training","performance review","employee relations","workforce planning"],
    "consultancy": ["client engagement","requirements gathering","workshop facilitation","stakeholder advisory","proposal","diagnosis","deliverable"],
    "data_science": ["modeling","ml","machine learning","prediction","features","training","validation","deployment","experiment","data pipeline"],
    "accounting": ["ledger","reconciliation","audit","financial statement","budget","variance","compliance","accrual"],
    "education": ["curriculum","teaching","instruction","assessment","learning outcomes","mentoring","tutor","tutoring"],
    "social_sciences": ["qualitative","quantitative","survey design","behavioral","fieldwork","interview","coding scheme","protocol"]
}

# utils/education_map.py

EDU_SYNONYMS = {
    "bachelor": ["bachelor", "b.sc", "b.s", "b.s.", "bsc", "bs"],
    "master": ["master", "m.sc", "m.s", "m.s.", "msc", "ms", "mba"],
    "phd": ["phd", "doctorate", "d.phil", "d.phil."],
    "associate": ["associate", "aas", "aa", "associate degree"],
    "high school": ["high school", "secondary school"],
}


# Normalization helper lists (lowercase)
SKILLS_LC = [s.lower() for s in SKILLS]
RESPONSIBILITIES_LC = [r.lower() for r in RESPONSIBILITIES]
EDUCATION_LC = [e.lower() for e in EDUCATION]

