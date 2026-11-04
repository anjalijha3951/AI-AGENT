import ollama
import json
from tools import compare_skills


def run_agent(job_description, candidate_profile):

    prompt = f"""
    Extract technical skills from the text below.

    JOB DESCRIPTION:
    {job_description}

    CANDIDATE PROFILE:
    {candidate_profile}

    Return JSON with exactly these keys:
    {{
        "required_skills": [],
        "candidate_skills": []
    }}

    Include skills explicitly mentioned in each text.
    Do not return empty lists if skills are present.
    Return JSON only.
    """

    response = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        format="json"
    )

    content = response["message"]["content"]

    print("AI Response:", content)

    try:
        skills = json.loads(content)

        required = skills.get("required_skills", [])
        candidate = skills.get("candidate_skills", [])

    except (json.JSONDecodeError, AttributeError):
        required = []
        candidate = []

    # Reliable fallback if the model fails to extract skills
    known_skills = [
        "Python",
        "SQL",
        "Machine Learning",
        "Power BI",
        "Scikit-learn",
        "Java",
        "Deep Learning",
        "NLP",
        "TensorFlow",
        "PyTorch"
    ]

    if not required:
        required = [
            skill for skill in known_skills
            if skill.lower() in job_description.lower()
        ]

    if not candidate:
        candidate = [
            skill for skill in known_skills
            if skill.lower() in candidate_profile.lower()
        ]

    if not required:
        raise ValueError(
            "No skills found in the job description."
        )

    result = compare_skills(required, candidate)

    return result