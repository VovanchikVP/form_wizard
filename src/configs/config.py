import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    BOT_TOKEN: str = os.environ.get("APP_BOT_TOKEN", "")
    GIGA_CLIENT_ID: str = os.environ.get("APP_GIGA_CLIENT_ID", "")
    GIGA_SCOPE: str = os.environ.get("APP_GIGA_SCOPE", "")
    GIGA_AUTHORIZATION_KEY: str = os.environ.get("APP_GIGA_AUTHORIZATION_KEY", "")
    GIGA_OAUTH_URL: str = os.environ.get("APP_GIGA_OAUTH_URL", "")
    GIGA_REFRESH_TOKEN: int = os.environ.get("APP_GIGA_REFRESH_TOKEN", 1600)
    ALLOWED_USERS: list[int] = os.environ.get("APP_ALLOWED_USERS").split(";")


settings = Settings()
