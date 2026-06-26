print("✅ home.py loaded")
import streamlit as st


def show():
    # ===========================
    # PAGE TITLE
    # ===========================
    st.title("🤖 AI Mentor Hub")
    st.subheader("Your Personal GenAI Career & Learning Platform")

    st.write(
        """
Welcome to **AI Mentor Hub**!

This application combines multiple AI-powered tools into one platform to help students:
- 📄 Improve resumes
- 🎤 Prepare for interviews
- 📚 Learn new concepts
- 🚀 Plan careers
- ✍️ Generate LinkedIn posts
- 📊 Track academic performance

**Powered by Python + Google Gemini**
"""
    )

    st.divider()

    # ===========================
    # DASHBOARD METRICS
    # ===========================
    st.header("📊 Dashboard Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Modules", "8")

    with col2:
        st.metric("AI Model", "Gemini")

    with col3:
        st.metric("Prompt Templates", "20+")

    with col4:
        st.metric("Status", "Active")

    st.divider()

    # ===========================
    # FEATURES
    # ===========================
    st.header("✨ Available Modules")

    col1, col2 = st.columns(2)

    with col1:
        st.success("💬 AI Chat Assistant")
        st.success("📄 Resume Analyzer")
        st.success("🎤 Interview Coach")
        st.success("📚 Study Mentor")

    with col2:
        st.success("🚀 Career Advisor")
        st.success("✍️ LinkedIn Post Generator")
        st.success("📊 Student Dashboard")
        st.success("📑 Research Assistant (Coming Soon)")

    st.divider()

    # ===========================
    # TECHNOLOGIES
    # ===========================
    st.header("🛠 Technology Stack")

    tech1, tech2, tech3 = st.columns(3)

    with tech1:
        st.info("🐍 Python")
        st.info("🎨 Streamlit")

    with tech2:
        st.info("🤖 Google Gemini")
        st.info("🧠 Prompt Engineering")

    with tech3:
        st.info("🗄 SQLite")
        st.info("📂 Git & GitHub")

    st.divider()

    # ===========================
    # ROADMAP
    # ===========================
    st.header("📌 Development Roadmap")

    roadmap = [
        "✅ Project Setup",
        "✅ Dashboard UI",
        "⬜ Gemini Integration",
        "⬜ AI Chat Assistant",
        "⬜ Resume Analyzer",
        "⬜ Interview Coach",
        "⬜ Study Mentor",
        "⬜ Career Advisor",
        "⬜ LinkedIn Generator",
        "⬜ Student Dashboard",
        "⬜ Research Assistant (RAG)",
        "⬜ Deployment"
    ]

    for item in roadmap:
        st.write(item)

    st.divider()

    # ===========================
    # FOOTER
    # ===========================
    st.caption(
        "AI Mentor Hub • Built using Python, Streamlit, Google Gemini, and Prompt Engineering"
    )