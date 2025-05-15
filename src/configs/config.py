import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    BOT_TOKEN: str = os.environ.get("APP_BOT_TOKEN", "")


settings = Settings()
