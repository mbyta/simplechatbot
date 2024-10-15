from abc import ABC, abstractmethod
from instructor import Instructor

class BaseClient(ABC):
    def __init__(self):
        self.api_client: Instructor = None

    @abstractmethod
    def get_response(self, user_query: str, selected_model: str) -> str:
        pass