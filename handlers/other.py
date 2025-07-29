from aiogram import Router
from aiogram.types import Message

oter_router = Router()

@oter_router.message()
async def sen_echo(message: Message):
    return message.answer(f'Это эхо! {message.text}')