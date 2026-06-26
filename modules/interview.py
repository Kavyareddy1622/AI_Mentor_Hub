import streamlit as st
from services.gemini_service import GeminiService


def show():

    st.title("🎤 AI Interview Coach")

    st.write("Practice technical interviews with AI.")

    ai = GeminiService()

    domain = st.selectbox(
        "Choose Interview Domain",
        [
            "Python",
            "Data Science",
            "Machine Learning",
            "Deep Learning",
            "GenAI",
            "SQL",
            "Web Development"
        ]
    )

    difficulty = st.selectbox(
        "Difficulty",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    number = st.slider(
        "Number of Questions",
        1,
        10,
        5
    )

    if st.button("Generate Interview Questions"):

        prompt = f"""
You are a senior technical interviewer.

Generate {number} {difficulty}-level interview questions on {domain}.

For each question provide:

Question

Ideal Answer

Interview Tip

Format using Markdown headings.
"""

        with st.spinner("Generating questions..."):

            response = ai.generate_response(prompt)

        st.markdown(response)