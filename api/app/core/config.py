from pydantic_settings import BaseSettings

import secrets

class Settings(BaseSettings):
    PROJECT_NAME: str = "CredKit CRM"
    API_V1_STR: str = "/api/v1"

    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SECRET_KEY: str = secrets.token_urlsafe(32)

    DATABASE_URL: str
    REDIS_URL: str

    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()
