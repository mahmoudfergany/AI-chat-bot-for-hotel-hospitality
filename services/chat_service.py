import os

from dotenv import load_dotenv

from providers.provider_factory import ProviderFactory

load_dotenv()


class ChatService:

    def __init__(self):
        provider_name = os.getenv("DEFAULT_PROVIDER", "gemini")
        self.provider = ProviderFactory.get_provider(provider_name)

    async def chat(self, message: str):
        return await self.provider.generate_response(message)