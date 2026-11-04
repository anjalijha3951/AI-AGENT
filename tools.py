def compare_skills(required_skills, candidate_skills):
    required = {
        skill.strip().lower()
        for skill in required_skills
    }

    candidate = {
        skill.strip().lower()
        for skill in candidate_skills
    }

    matching = sorted(required & candidate)
    missing = sorted(required - candidate)

    if required:
        percentage = round(
            len(matching) / len(required) * 100, 2
        )
    else:
        percentage = 0

    return {
        "matching_skills": matching,
        "missing_skills": missing,
        "match_percentage": percentage
    }