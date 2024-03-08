from pydantic import BaseModel, field_validator


class PromptResponseModel(BaseModel):
    prompt_type: str
    func_input_kwargs: dict
    prompt_used: str
    generate_content_response: str


class ProjectRequest(BaseModel):
    project_name: str
    initial_idea: str
    target_audience_persona: list[str]

    @field_validator("project_name")
    @classmethod
    def project_name_must_be_unique(cls, v: str) -> str:
        return v.replace(" ", "_").lower()
