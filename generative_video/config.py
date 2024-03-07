from typing import Optional
from functools import cache
from pydantic_settings import BaseSettings
from pydantic import SecretStr


class GenerativeVideoSettings(BaseSettings, env_file=".env", env_prefix="ds_"):
    GOOGLE_API_KEY: Optional[SecretStr] = None


@cache
def get_settings() -> GenerativeVideoSettings:
    return GenerativeVideoSettings()


settings = get_settings()
