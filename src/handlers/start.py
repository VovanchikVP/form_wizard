from aiogram import (
    F,
    Router,
    types,
)
from aiogram.filters import (
    Command,
    CommandStart,
)
from aiogram.types import Message

from src.configs.config import settings
from src.handlers.services.templates.initial_template_preparation import InitialTemplatePreparation
from src.handlers.services.voice_to_text import VoiceToTextService
from src.llm_agents.giga import GIGAChatService

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


@start_router.message()
async def get_audio_messages(message: Message):
    if message.from_user.id not in settings.ALLOWED_USERS:
        if message.voice is not None:
            message_text = await VoiceToTextService.parce_voice_message(message)
            await message.answer(message_text)
        await message.answer("Я вас не понимаю. Говорите голосом.")
    else:
        if message.voice is not None:
            message_text = await VoiceToTextService.parce_voice_message(message)
            answer_llm = await GIGAChatService.request_function(message_text, message.from_user.id)
            await message.answer(answer_llm)
        elif message.content_type == types.ContentType.DOCUMENT:
            message_text = await InitialTemplatePreparation.parce_document(message)
            await message.answer(message_text)
        elif message.content_type == types.ContentType.TEXT:
            answer_llm = await GIGAChatService.request_function(message.text, message.from_user.id)
            await message.answer(answer_llm)
