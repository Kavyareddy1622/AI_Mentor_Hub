import os
import streamlit as st

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Try Streamlit Secrets first, then .env
GEMINI_API_KEY = st.secrets.get("GEMINI_API_KEY", os.getenv("GEMINI_API_KEY"))

if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found. Add it to Streamlit Secrets or .env"
    )