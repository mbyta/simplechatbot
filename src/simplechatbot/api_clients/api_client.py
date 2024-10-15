from api_clients.llm_models import LlmModels
from api_clients.client_base import BaseClient
from api_clients.client_openai import OpenAiClient
from api_clients.client_anthropic import AnthropicClient
from api_clients.client_google import GoogleClient

class ApiClient():
    def get_response(self, user_query: str, selected_model: str) -> str:
        api_client: BaseClient = None
        llm_models = LlmModels()

        if selected_model in llm_models.get_list_of_openai_models():
            api_client = OpenAiClient()
        elif selected_model in llm_models.get_list_of_anthropic_models():
            api_client = AnthropicClient()
        elif selected_model in llm_models.get_list_of_google_models():
            api_client = GoogleClient()
        else:
            raise ValueError("Unknown model")

        return api_client.get_response(user_query, selected_model)