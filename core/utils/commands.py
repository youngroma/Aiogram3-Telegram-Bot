#меню с командами
from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Начало роботы'
        ),
        BotCommand(
            command='help',
            description = 'Помощь'
        ),
        BotCommand(
            command='cancel',
            description = 'Назад'
        ),
        BotCommand(
            command='inline',
            description='Показать инлайн клавиатуру'
        ),
        BotCommand(
            command='pay',
            description='Купить продукт'
        ),
        BotCommand(
            command='audio',
            description='прислась аудио'
        ),
        BotCommand(
            command='document',
            description='прислась документ'
        ),
        BotCommand(
            command='mediagroup',
            description='прислать медиагруппу'
        ),
        BotCommand(
            command='photo',
            description='прислать фото'
        ),
        BotCommand(
            command='sticker',
            description='прислать стикер'
        ),
        BotCommand(
            command='video',
            description='прислать видео'
        ),
        BotCommand(
            command='video_note',
            description='прислать видеосообщениес'
        ),
        BotCommand(
            command='voice',
            description='прислать голосовое сообщение'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())