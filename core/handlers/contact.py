'''rom aiogram.types import Message
from aiogram import Bot

async def get_true_contact(message: Message, bot: Bot):
    await message.answer(f'Ты отправил <b>свой</b> контакт')

async def get_fake_contact(message: Message, bot: Bot):
    await message.answer(f'Ты отправил <b>не свой</b> контакт')'''