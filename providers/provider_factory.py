from providers.gemini_provider import GeminiProvider


class ProviderFactory:

    @staticmethod
    def get_provider(provider_name: str):

        if provider_name.lower() == "gemini":
            return GeminiProvider()

        raise ValueError(f"Provider '{provider_name}' is not supported.")