from dotenv import load_dotenv
from api_clients.client_base import BaseClient
import os
import instructor
from api_clients.api_key_names import ApiKeyName
import google.generativeai as genai
from api_clients.response_models import GenericFormatResponseModel
from constants import Constants
from openai.types.chat import ChatCompletionMessageParam

load_dotenv()

class GoogleClient(BaseClient):
    def __init__(self):
        genai.configure(api_key=os.getenv(ApiKeyName.GOOGLE))
        self.api_client = instructor.from_gemini(client=genai.GenerativeModel(), mode=instructor.Mode.GEMINI_JSON)

    def get_response(self, messages: list[ChatCompletionMessageParam], selected_model: str) -> str:
        self.api_client.client = genai.GenerativeModel(
            model_name=f"models/{selected_model}-latest",
            generation_config=genai.types.GenerationConfig(max_output_tokens=Constants.MAX_TOKEN))

        api_response = self.api_client.messages.create(
            #stream=True,
            response_model=GenericFormatResponseModel,
            messages=messages,
        )

        return api_response.response