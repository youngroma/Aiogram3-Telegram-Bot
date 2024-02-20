from aiogram import Bot, Dispatcher
from core.handlers.basic import get_start, get_photo, get_hello
import asyncio
import logging
from core.settings import settings
#from core.filters.iscontact import IsTrueContact
#from core.handlers.contact import get_true_contact, get_fake_contact
from aiogram import F
from aiogram.filters import Command
from core.utils.commands import set_commands
from core.handlers.basic import get_location
from core.handlers.basic import get_inline
from core.handlers.callback import select_macbook
from core.utils.callbackdata import MacInfo
from core.handlers.pay import order, pre_checkout_query, successful_payment, shipping_check
from core.middlewares.countermiddleware import CounterMiddleware
from core.middlewares.officehours import OfficeHoursMiddleware
from core.middlewares.dbmiddleware import DbSession
from core.middlewares.apschedulermiddleware import SchedulerMiddleware
import psycopg_pool
from core.handlers import form
from core.utils.statesform import StepsForm
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from core.handlers import apsched
from datetime import datetime, timedelta
from core.handlers import send_media
from aiogram.utils.chat_action import ChatActionMiddleware
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())



bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')

async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text='Bot is start working')

async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Bot is stop working')


def create_pool():
    return psycopg_pool.AsyncConnectionPool(f"host=127.0.0.1 port=5432 dbname=users user=postgres password=4Uwachi "
                                            f"connect_timeout=60")

async def start():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - [%(levelname)s] - %(name)s -'
                                '(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s'
                        )
    pool_connect = create_pool()
    dp = Dispatcher()
    scheduler = AsyncIOScheduler(timezone="Europe/Warsaw")
    scheduler.add_job(apsched.send_message_time, trigger='date', run_date=datetime.now() + timedelta(seconds=10),
                      kwargs={'bot': bot}) #add tasks
    scheduler.add_job(apsched.send_message_cron, trigger='cron', hour=datetime.now().hour,
                      minute=datetime.now().minute + 1, start_date=datetime.now(), kwargs={'bot': bot})
    scheduler.add_job(apsched.send_message_interval, trigger='interval', seconds=600, kwargs={'bot': bot})
    scheduler.start()
    dp.update.middleware.register((DbSession(pool_connect)))
    dp.message.middleware.register(CounterMiddleware())
    dp.message.middleware.register((OfficeHoursMiddleware()))
    dp.update.middleware.register(SchedulerMiddleware(scheduler))
    dp.message.middleware.register(ChatActionMiddleware())
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.message.register(send_media.get_audio, Command(commands='audio'))
    dp.message.register(send_media.get_document, Command(commands='document'))
    dp.message.register(send_media.get_photo, Command(commands='photo'))
    dp.message.register(send_media.get_video, Command(commands='video'))
    dp.message.register(send_media.get_meadia_group, Command(commands='mediagroup'))
    dp.message.register(send_media.get_sticker, Command(commands='sticker'))
    dp.message.register(send_media.get_video_note, Command(commands='video_note'))
    dp.message.register(send_media.get_voice, Command(commands='voice'))

    dp.message.register(form.get_form, Command(commands='form'))
    dp.message.register(form.get_name, StepsForm.GET_NAME)
    dp.message.register(form.get_last_name, StepsForm.GET_LAST_NAME)
    dp.message.register(form.get_age, StepsForm.GET_AGE)
    dp.message.register(order, Command(commands='pay'))
    dp.pre_checkout_query.register(pre_checkout_query)
    dp.message.register(successful_payment, F.successful_payment)
    dp.shipping_query.register(shipping_check)
    dp.message.register(get_inline, Command(commands='inline'))
    dp.callback_query.register(select_macbook, MacInfo.filter(F.model == 'pro')) #button click only on the model pro MacInfo.filter(F.model == 'pro')
    dp.message.register(get_location, F.from_user.location)
    dp.message.register(get_hello, F.text == 'Hello')
    #dp.message.register(get_true_contact, F.from_user.id, IsTrueContact())
    #dp.message.register(get_fake_contact, F.from_user.id)
    dp.message.register(get_photo, F.photo)
    dp.message.register(get_start, Command(commands=['start', 'run']))
    await dp.start_polling(bot)


if __name__ == '__main__':
        asyncio.run(start())
