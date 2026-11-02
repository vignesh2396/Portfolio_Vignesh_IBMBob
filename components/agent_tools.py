"""
Agent tools — structured data retrieval functions used by the IBM Granite ReAct agent.
Each function returns a string that the agent can include in its response.
"""
from data.profile import COURSES, SKILLS, PROJECTS, EMAIL, LINKEDIN, LOCATION, NAME


def get_courses(topic: str = "") -> str:
    """Return a formatted list of courses. Filter by topic keyword if provided."""
    results = COURSES
    if topic:
        topic_lower = topic.lower()
        results = [
            c for c in COURSES
            if topic_lower in c["title"].lower()
            or any(topic_lower in t.lower() for t in c["topics"])
        ]
    if not results:
        return f"No courses found matching '{topic}'. Here are all available courses:\n" + get_courses()

    lines = []
    for c in results:
        lines.append(
            f"**{c['title']}** ({c['duration']}, {c['level']})\n"
            f"  Topics: {', '.join(c['topics'])}\n"
            f"  Audience: {c['audience']}\n"
            f"  Delivered to: {c['delivered_to']}"
        )
    return "\n\n".join(lines)


def get_skills(category: str = "") -> str:
    """Return skills optionally filtered by category."""
    results = SKILLS
    if category:
        cat_lower = category.lower()
        results = [s for s in SKILLS if cat_lower in s[1].lower()]

    if not results:
        return f"No skills found for category '{category}'."

    # Group by category
    grouped: dict[str, list] = {}
    for skill, cat, prof in results:
        grouped.setdefault(cat, []).append(f"{skill} ({prof}%)")

    lines = []
    for cat, items in grouped.items():
        lines.append(f"**{cat}**: " + " | ".join(items))
    return "\n".join(lines)


def get_contact_info() -> str:
    """Return contact information."""
    return (
        f"📧 Email: {EMAIL}\n"
        f"💼 LinkedIn: {LINKEDIN}\n"
        f"📍 Location: {LOCATION}\n\n"
        f"You can also fill in the Contact form on the Contact page of this website."
    )


def get_projects() -> str:
    """Return a formatted list of projects."""
    lines = []
    for p in PROJECTS:
        lines.append(
            f"**{p['title']}** [{p['status']}]\n"
            f"  {p['description']}\n"
            f"  Tech: {', '.join(p['tech'])}"
        )
    return "\n\n".join(lines)


# Tool registry for agent use
TOOLS = {
    "get_courses": get_courses,
    "get_skills": get_skills,
    "get_contact_info": get_contact_info,
    "get_projects": get_projects,
}

TOOL_DESCRIPTIONS = """Available tools:
- get_courses(topic="") — lists training courses, optionally filtered by topic
- get_skills(category="") — lists skills, optionally filtered by category (Agentic AI, Machine Learning, Quantum Computing, Programming)
- get_contact_info() — returns email, LinkedIn, and location
- get_projects() — lists project summaries
"""
