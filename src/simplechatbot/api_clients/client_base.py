from abc import ABC, abstractmethod
from instructor import Instructor
from openai.types.chat import ChatCompletionMessageParam

class BaseClient(ABC):
    def __init__(self, selected_model: str):
        self.api_client: Instructor = None
        self.selected_model = selected_model

    @abstractmethod
    def get_response(self, messages: list[ChatCompletionMessageParam]) -> str:
        pass