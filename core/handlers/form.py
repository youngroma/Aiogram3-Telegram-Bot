from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from core.utils.statesform import StepsForm
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from core.handlers.apsched import send_message_middleware
from datetime import datetime, timedelta
from aiogram import Bot

async def get_form(message: Message, state: FSMContext):
    await message.answer(f'{message.from_user.first_name}, start filling out the form. Enter your name')
    await state.set_state(StepsForm.GET_NAME)

async def get_name(message: Message, state: FSMContext):
    await message.answer(f'Your name: \r\n{message.text}\r\nNow enter the surname')
    await state.update_data(name=message.text) #SAVE ENTERED DATA (USER NAME WRITTEN)
    await state.set_state(StepsForm.GET_LAST_NAME)

async def get_last_name(message: Message, state: FSMContext):
    await message.answer(f'Your surname: \r\n{message.text}\r\nenter age')
    await state.update_data(last_name=message.text)
    await state.set_state(StepsForm.GET_AGE)

async def get_age(message: Message, bot: Bot, state: FSMContext, apscheduler: AsyncIOScheduler):
    await message.answer(f'Your age: \r\n{message.text}\r\n')
    context_data = await state.get_data()
    await message.answer(f'Saved data in the state machine: \r\n{str(context_data)}\r\n')
    name = context_data.get('name')
    last_name = context_data.get('last_name')
    data_user = f'Here’s your details\r\n' \
                f'Name {name}\r\n' \
                f'Surname {last_name}\r\n' \
                f'Age {message.text}'
    await message.answer(data_user)
    await state.clear()
    apscheduler.add_job(send_message_middleware, trigger='date', run_date=datetime.now() + timedelta(seconds=10),
                        kwargs={'bot': bot, 'chat_id': message.from_user.id})