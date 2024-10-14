from api_clients.llm_models import get_list_of_openai_models, get_list_of_anthropic_models, get_list_of_google_models
from api_clients.openai_api_client import get_openai_api_response
from api_clients.anthropic_api_client import get_anthropic_api_response
from api_clients.google_api_client import get_google_api_response

def get_api_response(user_query: str, selected_model: str) -> str:
    if selected_model in get_list_of_openai_models():
        return get_openai_api_response(user_query, selected_model)
    elif selected_model in get_list_of_anthropic_models():
        return get_anthropic_api_response(user_query, selected_model)
    elif selected_model in get_list_of_google_models():
        return get_google_api_response(user_query, selected_model)
    else:
        raise ValueError("Unknown model")