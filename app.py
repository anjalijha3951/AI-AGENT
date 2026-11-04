
import streamlit as st
from agent import run_agent

st.set_page_config(
    page_title="Smart AI Job Assistant",
    page_icon="🤖"
)

st.title("🤖 Smart AI Job Assistant")
st.write("AI-powered Job Skill Matching System")

job_description = st.text_area(
    "Enter Job Description"
)

candidate_profile = st.text_area(
    "Enter Your Skills"
)

if st.button("Analyze My Skills"):

    if not job_description.strip() or not candidate_profile.strip():
        st.warning("Please enter both fields.")

    else:
        try:
            with st.spinner("AI is analyzing your skills..."):
                result = run_agent(
                    job_description,
                    candidate_profile
                )

            st.success("Analysis Completed!")

            st.subheader("📊 Skill Analysis Report")

            st.metric(
                "Skill Match Percentage",
                f"{result['match_percentage']}%"
            )

            st.progress(
                min(100, max(0, result["match_percentage"] / 100))
            )

            st.subheader("✅ Matching Skills")
            st.write(result["matching_skills"])

            st.subheader("❌ Missing Skills")
            st.write(result["missing_skills"])

        except Exception as e:
            st.error(f"Error: {e}")
