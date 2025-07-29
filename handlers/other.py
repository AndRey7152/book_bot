from aiogram import Router
from aiogram.types import Message

other_router = Router()

@other_router.message()
async def sen_echo(message: Message):
    return message.answer(f'Это эхо! {message.text}')