
class LlmModels:
    def __init__(self):
        self.openai_models = {
            "gpt-4o-mini": "GPT-4o mini"
        }

        self.anthropic_models = {
            "claude-3-haiku-20240307": "Claude 3 Haiku"
        }

        self.google_models = {
            "gemini-1.5-flash-latest": "Gemini 1.5 Flash"
        }

    def get_all_models(self) -> dict[str, str]:
        return { **self.openai_models, **self.anthropic_models, **self.google_models }

    def get_list_of_openai_models(self) -> list[str]:
        return list(self.openai_models.keys())

    def get_list_of_anthropic_models(self) -> list[str]:
        return list(self.anthropic_models.keys())

    def get_list_of_google_models(self) -> list[str]:
        return list(self.google_models.keys())