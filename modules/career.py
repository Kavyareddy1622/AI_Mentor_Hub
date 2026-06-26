import streamlit as st
from services.gemini_service import GeminiService


def show():

    st.title("🚀 AI Career Advisor")

    st.write("Get personalized career guidance powered by Google Gemini.")

    ai = GeminiService()

    name = st.text_input("Your Name")

    education = st.selectbox(
        "Education",
        [
            "Diploma",
            "B.Tech",
            "M.Tech",
            "MBA",
            "Other"
        ]
    )

    interests = st.multiselect(
        "Select Your Interests",
        [
            "Python",
            "Data Science",
            "Machine Learning",
            "Deep Learning",
            "GenAI",
            "Prompt Engineering",
            "Web Development",
            "Cloud",
            "Cyber Security",
            "Data Analytics"
        ]
    )

    goal = st.text_input(
        "Career Goal",
        placeholder="Example: Become a GenAI Engineer"
    )

    if st.button("Generate Career Roadmap"):

        if not goal:
            st.warning("Please enter your career goal.")
            return

        prompt = f"""
Role:
You are a Senior AI Career Mentor.

Student Information:
Name: {name}
Education: {education}
Interests: {', '.join(interests)}
Goal: {goal}

Generate:

1. Suitable Career Paths
2. Skills to Learn
3. Recommended Certifications
4. Portfolio Projects
5. Interview Preparation Tips
6. 30-Day Learning Plan
7. 60-Day Learning Plan
8. 90-Day Learning Plan

Format the output using Markdown.
"""

        with st.spinner("Creating your personalized roadmap..."):

            response = ai.generate_response(prompt)

        st.markdown(response)