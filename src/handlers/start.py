from aiogram import (
    F,
    Router,
)
from aiogram.filters import (
    Command,
    CommandStart,
)
from aiogram.types import Message

from src.audio_converter.converter import Converter
from src.configs.log_config import logger
from src.tg_bot.main import bot

start_router = Router()


@start_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Запуск сообщения по команде /start")


@start_router.message(Command("start_2"))
async def cmd_start_2(message: Message):
    await message.answer("Запуск сообщения по команде /start_2 используя фильтр Command()")


@start_router.message(F.text == "/start_3")
async def cmd_start_3(message: Message):
    await message.answer("Запуск сообщения по команде /start_3 используя магический фильтр F.text!")


@start_router.message(F.voice is not None)
async def get_audio_messages(message: Message):
    file_id = message.voice.file_id
    file_info = await bot.get_file(file_id)
    downloaded_file = await bot.download_file(file_info.file_path)
    file_name = f"{message.message_id}.ogg"
    name = message.chat.first_name if message.chat.first_name else "No_name"
    logger.info(f"Chat {name} (ID: {message.chat.id}) download file {file_name}")

    with open(file_name, "wb") as new_file:
        new_file.write(downloaded_file.read())

    converter = Converter(file_name)
    message_text = converter.audio_to_text()
    del converter
    await message.answer(message_text)
