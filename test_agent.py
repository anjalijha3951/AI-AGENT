from tools import compare_skills

required_skills = [
    "Python",
    "SQL",
    "Machine Learning",
    "Power BI",
    "Scikit-learn"
]

candidate_skills = [
    "Python",
    "SQL",
    "Machine Learning"
]

result = compare_skills(
    required_skills,
    candidate_skills
)

print("AI JOB ASSISTANT REPORT")
print("-----------------------")
print("Matching Skills:", result["matching_skills"])
print("Missing Skills:", result["missing_skills"])
print("Skill Match:", result["match_percentage"], "%")