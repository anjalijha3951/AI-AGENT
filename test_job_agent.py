from agent import run_agent

job_description = """
We need an AI/ML Engineer with Python, SQL,
Machine Learning, Power BI and Scikit-learn.
"""

candidate_profile = """
I know Python, SQL and Machine Learning.
"""

result = run_agent(
    job_description,
    candidate_profile
)

print("\n===== SMART AI JOB ASSISTANT =====")
print("Matching Skills:", result["matching_skills"])
print("Missing Skills:", result["missing_skills"])
print("Skill Match:", result["match_percentage"], "%")