import os
import streamlit as st

try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass

GEMINI_API_KEY = st.secrets.get(
    "GEMINI_API_KEY",
    os.getenv("GEMINI_API_KEY")
)