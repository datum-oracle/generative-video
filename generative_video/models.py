from pydantic import BaseModel


class PromptResponseModel(BaseModel):
    prompt_type: str
    func_input_kwargs: dict
    prompt_used: str
    generate_content_response: str
