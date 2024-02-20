from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from core.utils.callbackdata import MacInfo

select_macbook = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Macbook Air 13 M2',
            callback_data='apple_air_13_m2_2020',
        )
    ],
    [
        InlineKeyboardButton(
            text='Macbook Pro 14 M1',
            callback_data='apple_pro_14_m1_2020'
        )
    ],
    [
        InlineKeyboardButton(
            text='Macbook Pro 16',
            callback_data='apple_pro_16_m1_2021'
        )
    ],
    [
        InlineKeyboardButton(
            text='Link',
            url='https://www.apple.com'
        )
    ],
    [
        InlineKeyboardButton(
            text='Profile',
            url='tg://user?id=YOUR_ID' #YOUR_ID - enter Your user ID
        )
    ]
])


def get_inline_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Macbook Air 13 M2', callback_data=MacInfo(model='air', size=13, chip='m2', year=2020 ))
    keyboard_builder.button(text='Macbook Pro 14 M1', callback_data=MacInfo(model='pro', size=14, chip='m1', year=2020 ))
    keyboard_builder.button(text='Macbook Pro 16', callback_data=MacInfo(model='pro', size=16, chip='m1', year=2021 ))
    keyboard_builder.button(text='Link', url='https://www.apple.com')
    keyboard_builder.button(text='Profile', url='tg://user?id=YOUR_ID') ##YOUR_ID - enter Your user ID

    keyboard_builder.adjust(3)
    return keyboard_builder.as_markup()


