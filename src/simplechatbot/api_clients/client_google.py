from dotenv import load_dotenv
from api_clients.client_base import BaseClient
import os
import instructor
from api_clients.api_key_names import ApiKeyName
import google.generativeai as genai
from api_clients.response_models import GenericFormatResponseModel

load_dotenv()

class GoogleClient(BaseClient):
    def __init__(self):
        genai.configure(api_key=os.getenv(ApiKeyName.GOOGLE))
        self.api_client = instructor.from_gemini(client=genai.GenerativeModel(), mode=instructor.Mode.GEMINI_JSON)

    def get_response(self, user_query: str, selected_model: str) -> str:
        self.api_client.client = genai.GenerativeModel(model_name=f"models/{selected_model}-latest")

        api_response = self.api_client.messages.create(
            messages=[{"role": "user", "content": user_query}],
            response_model=GenericFormatResponseModel,
        )

        return api_response.response