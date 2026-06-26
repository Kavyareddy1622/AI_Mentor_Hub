import streamlit as st

from services.gemini_service import GeminiService
from utils.pdf_reader import extract_text


def show():

    st.title("📄 AI Resume Analyzer")

    st.write(
        "Upload your resume in PDF format to receive AI-powered feedback."
    )

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["pdf"]
    )

    if uploaded_file:

        st.success("Resume uploaded successfully.")

        if st.button("Analyze Resume"):

            with st.spinner("Analyzing resume..."):

                resume_text = extract_text(uploaded_file)

                prompt = f"""
You are an experienced ATS recruiter.

Analyze the following resume.

Return:

1. ATS Score (0-100)

2. Strengths

3. Weaknesses

4. Missing Skills

5. Suggestions for Improvement

Resume:

{resume_text}
"""

                ai = GeminiService()

                response = ai.generate_response(prompt)

                st.markdown(response)