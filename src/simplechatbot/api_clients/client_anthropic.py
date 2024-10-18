from dotenv import load_dotenv
from api_clients.client_base import BaseClient
import os
import instructor
from api_clients.api_key_names import ApiKeyName
from anthropic import Anthropic
from api_clients.response_models import GenericFormatResponseModel
from constants import Constants
from openai.types.chat import ChatCompletionMessageParam

load_dotenv()

class AnthropicClient(BaseClient):
    def __init__(self, selected_model: str):
        super().__init__(selected_model)
        self.api_client = instructor.from_anthropic(Anthropic(api_key=os.getenv(ApiKeyName.ANTHROPIC)))

    def get_response(self, messages: list[ChatCompletionMessageParam]) -> str:
        api_response = self.api_client.messages.create(
            model=self.selected_model,
            max_tokens=Constants.MAX_TOKEN,
            response_model=GenericFormatResponseModel,
            messages=messages,
        )
        return api_response.response