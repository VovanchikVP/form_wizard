import asyncio

from handlers.start import start_router
from src.tg_bot.main import (
    bot,
    dp,
)


async def main():
    dp.include_router(start_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
