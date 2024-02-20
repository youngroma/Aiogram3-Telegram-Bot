from aiogram import Bot
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery, InlineKeyboardButton,  InlineKeyboardMarkup, ShippingOption, ShippingQuery



keyboards =InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='pay',
            pay=True
        )
    ],
    [
        InlineKeyboardButton(
            text='Link',
            url='apple.com'
        )
    ]
])


PL_SHIPPING = ShippingOption(
    id='PL',
    title='deliver to Poland',
    prices=[
        LabeledPrice(
            label='Poczta Polska',
            amount=700
        )
    ]
)

CZ_SHIPPING = ShippingOption(
    id='CZ',
    title='deliver to Czech',
    prices=[
        LabeledPrice(
            label='CZ POCZTA',
            amount=900
        )
    ]
)

UA_SHIPPING = ShippingOption(
    id='UA',
    title='deliver to Ukraine',
    prices=[
        LabeledPrice(
            label='Nova Post',
            amount=500
        )
    ]
)

CITTIES_SHIPING = ShippingOption(
    id='capitals',
    title='Fast delivery',
    prices=[
        LabeledPrice(
            label='courier',
            amount=2000
        )
    ]
)


async def shipping_check(shipping_query: ShippingQuery, bot: Bot):
    shiping_options = []
    countries = ['PL', 'CZ', 'UA']
    if shipping_query.shipping_address.country_code not in countries:
        return await bot.answer_shipping_query(shipping_query.id, ok=False,
                                               error_message='Not delivery in your Country')

    if shipping_query.shipping_address.country_code == 'PL':
        shiping_options.append(PL_SHIPPING)
    if shipping_query.shipping_address.country_code == 'CZ':
        shiping_options.append(CZ_SHIPPING)
    if shipping_query.shipping_address.country_code == 'UA':
        shiping_options.append(UA_SHIPPING)

    cities = ['Warsaw', 'Praha', 'Kyiv']
    if shipping_query.shipping_address.city in cities:
        shiping_options.append(CITTIES_SHIPING)

    await bot.answer_shipping_query(shipping_query.id, ok=True, shipping_options=shiping_options)

async def order(message: Message, bot: Bot):
    await bot.send_invoice(
        chat_id=message.chat.id,
        title='Purchase through TG Bot',
        description='Learn to accept payments via telegram bot',
        payload='Payment through a bot',
        provider_token='410694247:TEST:14c0c650-8fa1-403c-87b6-4f10d5cd8ec6',
        currency='usd',
        prices=[
            LabeledPrice(
                label='access to classified information',
                amount=99000
            ),
            LabeledPrice(
                label='VAT',
                amount=20000
            ),
            LabeledPrice(
                label='discount',
                amount=20000
            ),
            LabeledPrice(
                label='Bonus',
                amount=-40000
            )
        ],
        max_tip_amount=5000,
        suggested_tip_amounts=[1000,2000,3000,4000],
        start_parameter='Roma',
        provider_data=None,
        photo_url='https://www.apple.com/v/iphone-14/i/images/key-features/features/size/size_yellow__dnv9794q7loy_large.jpg',
        photo_size=100,
        photo_width=800,
        photo_height=450,
        need_name=False,
        need_phone_number=False,
        need_email=False,
        need_shipping_address=False,
        send_phone_number_to_provider=False,
        send_email_to_provider=False,
        is_flexible=True,
        disable_notification=False,
        protect_content=False,
        reply_to_message_id=None,
        allow_sending_without_reply=True,
        reply_markup=keyboards,
        request_timeout=15
    )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment(message: Message):
    msg = f'Thank you for paying {message.successful_payment.total_amount // 100} {message.successful_payment.currency}.'\
          f'\r\nOur manager got the application and is already typing your phone number.' \
          f'\r\nGood luck ;3'
    await message.answer(msg)
