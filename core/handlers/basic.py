from aiogram import Bot
from aiogram.types import Message
import json
from core.keyboards.reply import reply_keyboard, loc_tel_poll_keyboard, get_reply_keyboard
from core.keyboards.inline import select_macbook, get_inline_keyboard
from core.utils.dbconnect import Request


async def get_inline(message: Message, bot: Bot):
    await message.answer(f"Hello, {message.from_user.first_name}. Show you inline buttons",
                         reply_markup=get_inline_keyboard())



async def get_start(message: Message, bot: Bot, counter: str, request: Request):
    await request.add_data(message.from_user.id, message.from_user.first_name)
    await message.answer(f'Message #{counter}')
    await message.answer(f' <s> Hi {message.from_user.first_name}. Welcome!</s>',
                         reply_markup=get_reply_keyboard())

async def get_location(message: Message, bot: Bot):
    await message.answer(f'you sent the location!\r\a'
                         f'{message.location.latitude}\r\n{message.location.longitude}')


async def get_photo(message: Message, bot: Bot):
    await message.answer(f'thx for the pic :3')
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, 'photo.jpg')

async def get_hello(message: Message, bot: Bot):
    await message.answer(f'Hello to you too!')
    json_str = json.dumps(message.dict(), default=str)
    print(json_str)