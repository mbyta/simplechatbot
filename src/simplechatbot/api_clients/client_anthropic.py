from dotenv import load_dotenv
from api_clients.client_base import BaseClient
import os
from api_clients.api_key_names import ApiKeyName
from anthropic import Anthropic
from constants import Constants
from openai.types.chat import ChatCompletionMessageParam

load_dotenv()

class AnthropicClient(BaseClient):
    def __init__(self, selected_model: str):
        super().__init__(selected_model)
        self.api_client = Anthropic(api_key=os.getenv(ApiKeyName.ANTHROPIC))

    def get_response(self, messages: list[ChatCompletionMessageParam]) -> str:
        message = self.api_client.messages.create(
            model=self.selected_model,
            max_tokens=Constants.MAX_TOKEN,
            messages=messages,
        )
        return message.content[0].text