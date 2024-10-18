from dotenv import load_dotenv
from api_clients.client_base import BaseClient
import os
from api_clients.api_key_names import ApiKeyName
from openai import OpenAI
from constants import Constants
from openai.types.chat import ChatCompletionMessageParam

load_dotenv()

class OpenAiClient(BaseClient):
    def __init__(self, selected_model: str):
        super().__init__(selected_model)
        self.api_client = OpenAI(api_key=os.getenv(ApiKeyName.OPENAI))

    def get_response(self, messages: list[ChatCompletionMessageParam]) -> str:
        completion = self.api_client.chat.completions.create(
            model=self.selected_model,
            max_tokens=Constants.MAX_TOKEN,
            messages=messages,
        )
        return completion.choices[0].message.content