# utils/transferable_clusters.py
# Each cluster lists tools/skills considered mutually substitutable.

print("DEBUG: loading transferable_clusters.py")

TRANSFERABLE_CLUSTERS = [
    {
        "cluster": ["Tableau", "Power BI", "QlikView", "Looker", "Google Data Studio"],
        "coverage_level": "Transferable Skill",
        "explanation": "Business intelligence platforms share core workflows: data connection, modeling, dashboard building, and visualization logic."
    },
    {
        "cluster": ["AWS", "Azure", "Google Cloud Platform"],
        "coverage_level": "Transferable Skill",
        "explanation": "Cloud providers differ in naming and UI, but fundamentals such as compute, storage, IAM, networking, and deployment patterns carry over."
    },
    {
        "cluster": ["SQL", "MySQL", "PostgreSQL", "Oracle", "MariaDB"],
        "coverage_level": "Transferable Skill",
        "explanation": "All are relational ecosystems built around SQL syntax and standard schema design concepts. Switching requires minimal adaptation."
    },
    {
        "cluster": ["Git", "GitHub", "GitLab", "Bitbucket"],
        "coverage_level": "Transferable Skill",
        "explanation": "These platforms all operate on Git fundamentals (branching, merge, PRs). Knowing one strongly implies capability with others."
    },
    {
        "cluster": ["Google Analytics", "Adobe Analytics", "Mixpanel", "HubSpot", "Marketo"],
        "coverage_level": "Transferable Skill",
        "explanation": "Analytics and marketing automation systems share tracking, segmentation, attribution, and reporting foundations."
    },
    {
        "cluster": ["Photoshop", "Illustrator", "Figma", "Sketch"],
        "coverage_level": "Transferable Skill",
        "explanation": "Professional design tools share transferable concepts: vector/raster editing, layout, typography, prototyping, and component systems."
    },
    {
        "cluster": ["Jira", "Trello", "Asana", "Monday.com", "ClickUp"],
        "coverage_level": "Transferable Skill",
        "explanation": "Project management tools follow equivalent principles: task structuring, tracking, workflow management, and collaboration."
    }
]

