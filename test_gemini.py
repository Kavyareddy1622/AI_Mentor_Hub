from google import genai
from google.genai.errors import APIError
from config.settings import GEMINI_API_KEY
import time


class GeminiService:

    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def generate_response(self, prompt):

        for attempt in range(3):  # Retry up to 3 times

            try:

                response = self.client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt,
                )

                return response.text

            except APIError as e:

                if "503" in str(e):
                    time.sleep(5)  # Wait 5 seconds before retrying
                    continue

                return f"❌ Gemini API Error:\n\n{e}"

            except Exception as e:
                return f"❌ Unexpected Error:\n\n{e}"

        return "⚠️ Gemini is currently experiencing high demand. Please try again in a few minutes."