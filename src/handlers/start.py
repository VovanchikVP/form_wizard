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

from src.handlers.services.initial_template_preparation import InitialTemplatePreparation
from src.handlers.services.voice_to_text import VoiceToTextService

# User(id=442054550, is_bot=False, first_name='Владимир', last_name=None, username='kapitonov_vp', language_code='ru', is_premium=None, added_to_attachment_menu=None, can_join_groups=None, can_read_all_group_messages=None, supports_inline_queries=None, can_connect_to_business=None, has_main_web_app=None)

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
    if message.voice is not None:
        message_text = await VoiceToTextService.parce_voice_message(message)
        await message.answer(message_text)
    elif message.content_type == types.ContentType.DOCUMENT:
        message_text = await InitialTemplatePreparation.parce_document(message)
        await message.answer(message_text)
