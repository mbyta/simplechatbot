from abc import ABC, abstractmethod
from instructor import Instructor
from openai.types.chat import ChatCompletionMessageParam

class BaseClient(ABC):
    def __init__(self):
        self.api_client: Instructor = None

    @abstractmethod
    def get_response(self, messages: list[ChatCompletionMessageParam], selected_model: str) -> str:
        pass