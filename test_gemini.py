from services.gemini_service import GeminiService

ai = GeminiService()

response = ai.generate_response(
    "Introduce yourself in 50 words."
)

print(response)