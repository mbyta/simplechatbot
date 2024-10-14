from enum import StrEnum

class OpenAiModel(StrEnum):
    GPT_4O_MINI_LATEST = "gpt-4o-mini-2024-07-18"

class AnthropicModel(StrEnum):
    CLAUDE_3_HAIKU_LATEST = "claude-3-haiku-20240307"

class GoogleModel(StrEnum):
    GEMINI_1_5_FLASH_LATEST = "gemini-1.5-flash-latest"

def get_list_of_all_models() -> list[str]:
    model_1 = [model.value for model in OpenAiModel]
    model_2 = [model.value for model in AnthropicModel]
    model_3 = [model.value for model in GoogleModel]

    return model_1 + model_2 + model_3

def get_list_of_openai_models() -> list[str]:
    return [model.value for model in OpenAiModel]

def get_list_of_anthropic_models() -> list[str]:
    return [model.value for model in AnthropicModel]

def get_list_of_google_models() -> list[str]:
    return [model.value for model in GoogleModel]