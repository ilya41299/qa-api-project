from pathlib import Path
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict

Language_codes = Literal["en", "ru"]

ROOT_DIR = Path(__file__).parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(ROOT_DIR / ".env"),
        env_file_encoding="utf-8",
        extra="ignore",
        env_nested_delimiter="__",
    )

    base_url: str


settings = Settings()
