import streamlit as st
from services.gemini_service import GeminiService


def show():

    st.title("📚 AI Study Mentor")

    st.write("Your personal AI tutor powered by Google Gemini.")

    ai = GeminiService()

    topic = st.text_input(
        "Enter a topic",
        placeholder="Example: Prompt Engineering"
    )

    task = st.selectbox(
        "Choose what you need",
        [
            "Explain Concept",
            "Generate Notes",
            "Create Quiz",
            "Study Plan",
            "Flashcards"
        ]
    )

    if st.button("Generate"):

        if not topic:
            st.warning("Please enter a topic.")
            return

        prompt = f"""
You are an expert educator.

Topic:
{topic}

Task:
{task}

Instructions:

- Explain clearly.
- Use simple language.
- Use bullet points.
- Add examples wherever possible.
- Format the response using Markdown.
"""

        with st.spinner("Generating..."):

            response = ai.generate_response(prompt)

        st.markdown(response)