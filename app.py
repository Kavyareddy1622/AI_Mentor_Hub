import streamlit as st
from modules import home

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
    ],
)

# ---------------------------
# Routing
# ---------------------------

if page == "🏠 Home":
    home.show()

else:
    st.title(page)
    st.info("🚧 This module will be developed in upcoming phases.")