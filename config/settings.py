import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found. Please check your .env file."
    )
    MODEL_NAME = "gemini-2.5-flash"
    response = self.client.models.generate_content(
    model=MODEL_NAME,
    contents=prompt,
)