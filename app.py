import streamlit as st
from modules import (
    home,
    ai_chat,
    resume,
    interview,
    study,
    career,
    linkedin,
    dashboard,
    rag_chat
    
)

# ---------------------------
# Page Configuration
# ---------------------------
print("Imported from:", home.__file__)
print("Contents:", dir(home))

st.set_page_config(
    page_title="AI Mentor Hub",
    page_icon="🤖",
    layout="wide",
)

# ---------------------------
# Load CSS
# ---------------------------

with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------------------------
# Sidebar
# ---------------------------

st.sidebar.title("🤖 AI Mentor Hub")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "💬 AI Chat",
        "📄 Resume Analyzer",
        "🎤 Interview Coach",
        "📚 Study Mentor",
        "🚀 Career Advisor",
        "✍ LinkedIn Generator",
        "📊 Student Dashboard",
        "📚 Document Chat (RAG)"
    ],
)

# ---------------------------
# Routing
# ---------------------------
# ---------------------------
# Routing
# ---------------------------

if page == "🏠 Home":
    home.show()

elif page == "💬 AI Chat":
    ai_chat.show()
elif page == "📄 Resume Analyzer":
    resume.show()
elif page == "🎤 Interview Coach":
    interview.show()
elif page == "📚 Study Mentor":
    study.show()
elif page == "🚀 Career Advisor":
    career.show()
elif page == "✍ LinkedIn Generator":
    linkedin.show()
elif page == "📊 Student Dashboard":
    dashboard.show()
elif page == "📚 Document Chat (RAG)":
    rag_chat.show()
elif page == "📄 Resume Analyzer":
    st.title("📄 Resume Analyzer")
    st.info("🚧 Coming Soon")

elif page == "🎤 Interview Coach":
    st.title("🎤 Interview Coach")
    st.info("🚧 Coming Soon")

elif page == "📚 Study Mentor":
    st.title("📚 Study Mentor")
    st.info("🚧 Coming Soon")

elif page == "🚀 Career Advisor":
    st.title("🚀 Career Advisor")
    st.info("🚧 Coming Soon")

elif page == "✍ LinkedIn Generator":
    st.title("✍ LinkedIn Generator")
    st.info("🚧 Coming Soon")

elif page == "📊 Student Dashboard":
    st.title("📊 Student Dashboard")
    st.info("🚧 Coming Soon")
