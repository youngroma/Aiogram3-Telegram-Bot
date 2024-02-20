from aiogram import Bot


async def send_message_time(bot: Bot):
    await bot.send_message(0, f'the message was sent a few seconds after the bot started') #Instead 0, you must enter your ID

async def send_message_cron(bot: Bot): #выполняеться в одно и тоже время каждый день
    await bot.send_message(0, f'message will be sent daily at a specified time') #Instead 0, you must enter your ID

async def send_message_interval(bot: Bot):
    await bot.send_message(0, f'this message will be sent at intervals of 10 minutes') #Instead 0, you must enter your ID

async def send_message_middleware(bot: Bot, chat_id: int):
    await bot.send_message(chat_id, f'This message was sent using a middleware task')
