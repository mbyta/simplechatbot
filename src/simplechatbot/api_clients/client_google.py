from dotenv import load_dotenv
from api_clients.client_base import BaseClient
import os
from api_clients.api_key_names import ApiKeyName
import google.generativeai as genai
from constants import Constants
from openai.types.chat import ChatCompletionMessageParam
from google.generativeai.types.content_types import ContentDict
from api_clients.llm_roles import LlmRole

load_dotenv()

class GoogleClient(BaseClient):
    def __init__(self, selected_model: str):
        super().__init__(selected_model)
        genai.configure(api_key=os.getenv(ApiKeyName.GOOGLE))
        self.api_client = genai.GenerativeModel(
                model_name=f"models/{self.selected_model}",
                generation_config=genai.types.GenerationConfig(max_output_tokens=Constants.MAX_TOKEN))

    def get_response(self, messages: list[ChatCompletionMessageParam]) -> str:
        api_response = self.api_client.generate_content(contents=self.map_to_gemini_messages_format(messages))
        return api_response.text
    
    def map_to_gemini_messages_format(self, messages: list[ChatCompletionMessageParam]) -> list[ContentDict]:
        mapped_messages = []

        for msg in messages:
            gemini_role = LlmRole.MODEL if msg["role"] == LlmRole.ASSISTANT else msg["role"]
            mapped_messages.append(ContentDict(role=gemini_role, parts=[msg["content"]]))

        return mapped_messages