from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "fastapi-agentic"
    log_level: str = "INFO"


settings = Settings()
