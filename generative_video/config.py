from typing import Optional
from functools import lru_cache
from pydantic_settings import BaseSettings
from pydantic import SecretStr


class GenerativeVideoSettings(BaseSettings, env_file=".env", env_prefix="yt_"):
    GOOGLE_API_KEY: Optional[SecretStr] = None


@lru_cache
def get_settings() -> GenerativeVideoSettings:
    return GenerativeVideoSettings()
