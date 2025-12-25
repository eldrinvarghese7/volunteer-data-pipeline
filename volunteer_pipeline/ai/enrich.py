import json

def ai_enrich(text):
    """
    MOCK AI FUNCTION (replace with real API later)
    """
    if not isinstance(text, str) or len(text.strip()) == 0:
        return {
            "skills": [],
            "persona": "Passive",
            "confidence": 0.3
        }

    text_lower = text.lower()

    skills = []
    if "mentor" in text_lower:
        skills.append("Mentoring")
    if "electronics" in text_lower:
        skills.append("Electronics")
    if "teaching" in text_lower:
        skills.append("Teaching")

    persona = "Needs Guidance"
    if "mentor" in text_lower or "teaching" in text_lower:
        persona = "Mentor Material"

    confidence = min(0.9, 0.5 + 0.1 * len(skills))

    return {
        "skills": skills,
        "persona": persona,
        "confidence": confidence
    }
