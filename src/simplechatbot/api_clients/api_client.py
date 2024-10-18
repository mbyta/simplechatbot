from api_clients.llm_models import LlmModels
from api_clients.client_base import BaseClient
from api_clients.client_openai import OpenAiClient
from api_clients.client_anthropic import AnthropicClient
from api_clients.client_google import GoogleClient
from openai.types.chat import ChatCompletionMessageParam

class ApiClient():
    def get_response(self, messages: list[ChatCompletionMessageParam], selected_model: str):
        api_client: BaseClient = None
        llm_models = LlmModels()

        if selected_model in llm_models.get_list_of_openai_models():
            api_client = OpenAiClient(selected_model=selected_model)
        elif selected_model in llm_models.get_list_of_anthropic_models():
            api_client = AnthropicClient(selected_model=selected_model)
        elif selected_model in llm_models.get_list_of_google_models():
            api_client = GoogleClient(selected_model=selected_model)
        else:
            raise ValueError("Unknown model")

        return api_client.get_response(messages)