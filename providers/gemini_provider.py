import os

from dotenv import load_dotenv
from google import genai

from providers.base_provider import BaseProvider

load_dotenv()


class GeminiProvider(BaseProvider):
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in .env")

        self.client = genai.Client(api_key=api_key)

    async def generate_response(self, message: str) -> str:
        model = os.getenv("GEMINI_MODEL")

        if not model:
            raise ValueError("GEMINI_MODEL not found in .env")

        response = self.client.models.generate_content(
            model=model,
            contents=message,
        )

        return response.text