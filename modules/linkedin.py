import streamlit as st
from services.gemini_service import GeminiService


def show():

    st.title("✍️ AI LinkedIn Post Generator")

    st.write("Generate professional LinkedIn posts using Google Gemini.")

    ai = GeminiService()

    post_type = st.selectbox(
        "Post Type",
        [
            "Project",
            "Internship",
            "Certification",
            "Achievement",
            "Learning Journey",
            "Hackathon"
        ]
    )

    title = st.text_input(
        "Title",
        placeholder="Example: AI Mentor Hub"
    )

    description = st.text_area(
        "Describe your work",
        placeholder="Explain what you built or achieved..."
    )

    tone = st.selectbox(
        "Writing Style",
        [
            "Professional",
            "Storytelling",
            "Excited",
            "Minimal"
        ]
    )

    if st.button("Generate LinkedIn Post"):

        if not title or not description:
            st.warning("Please complete all fields.")
            return

        prompt = f"""
Role:
You are a professional LinkedIn content writer.

Create a LinkedIn post.

Post Type:
{post_type}

Title:
{title}

Description:
{description}

Tone:
{tone}

Requirements:

- Professional opening
- Explain the achievement
- Mention key technologies
- Mention learning outcomes
- End with appreciation
- Add 10 relevant hashtags

Return only the LinkedIn post.
"""

        with st.spinner("Generating..."):

            response = ai.generate_response(prompt)

        st.markdown("## Generated Post")

        st.write(response)