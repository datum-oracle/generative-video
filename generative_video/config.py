from functools import cache
from pydantic_settings import BaseSettings
from pydantic import SecretStr


class GenerativeVideoSettings(BaseSettings, env_file=".env", env_prefix="ds_"):
    GOOGLE_API_KEY: SecretStr
    PROJECT_ID: str
    LOCATION: str


@cache
def get_settings() -> GenerativeVideoSettings:
    return GenerativeVideoSettings()


settings = get_settings()
