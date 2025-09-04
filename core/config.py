from __future__ import annotations

import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str

    class Config:
        # .env 파일이 있으면 읽고, 없으면 OS 환경변수 사용
        env_file = ".env"
        env_file_encoding = "utf-8"

# .env 파일이 없을 수도 있으니 예외처리
settings = Settings()