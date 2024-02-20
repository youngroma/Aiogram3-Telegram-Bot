from aiogram.filters.callback_data import CallbackData

class MacInfo(CallbackData, prefix='Mac'):
    model: str
    size: int
    chip: str
    year: int