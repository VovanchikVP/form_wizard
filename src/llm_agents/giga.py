import asyncio
import datetime

import aiohttp
from gigachat import GigaChat

from src.configs.config import settings
from src.configs.log_config import logger


class OauthGIGAChat:
    """Авторизация в giga чате"""

    PAYLOAD = {"scope": settings.GIGA_SCOPE}
    HEADERS = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
        "RqUID": "c398d696-7588-4a2e-817c-e06c0ec3eeb8",
        "Authorization": f"Basic {settings.GIGA_AUTHORIZATION_KEY}",
    }
    ACCESS_TOKEN = None

    def __init__(self):
        self.last_refresh_token = None

    async def run(self):
        """Запуск сервиса контроля токена доступа"""
        async with aiohttp.ClientSession() as session:
            while True:
                try:
                    if not await self.condition_refresh_token():
                        await asyncio.sleep(10)
                        continue
                    async with session.post(
                        settings.GIGA_OAUTH_URL, headers=self.HEADERS, data=self.PAYLOAD, ssl=False
                    ) as resp:
                        result = await resp.json()
                        if isinstance(result, dict):
                            self.ACCESS_TOKEN = result.get("access_token")
                            self.last_refresh_token = datetime.datetime.now()
                        logger.info(resp.status)
                        logger.info(result)
                except Exception as err:
                    logger.error(err)

    async def condition_refresh_token(self) -> bool:
        """Определяем нужно ли обновлять токен или нет"""
        if self.last_refresh_token is None:
            return True
        if (datetime.datetime.now() - self.last_refresh_token).seconds > settings.GIGA_REFRESH_TOKEN:
            return True
        return False


class GIGAChat:
    """Взаимодействие с GIGA чатом"""

    @classmethod
    async def giga_chat(cls) -> GigaChat:
        """Взаимодействие с моделью GigaChat"""
        return GigaChat(credentials=OauthGIGAChat.ACCESS_TOKEN, model="GigaChat")

    @classmethod
    async def giga_chat_pro(cls) -> GigaChat:
        """Взаимодействие с моделью GigaChat-Pro"""
        return GigaChat(credentials=OauthGIGAChat.ACCESS_TOKEN, model="GigaChat-Pro")

    @classmethod
    async def giga_chat_max(cls) -> GigaChat:
        """Взаимодействие с моделью GigaChat-Max"""
        return GigaChat(credentials=OauthGIGAChat.ACCESS_TOKEN, model="GigaChat-Max")
