from datetime import datetime
from aiogram import BaseMiddleware
from typing import Callable, Awaitable, Dict, Any
from aiogram.types import Message

def office_hours() -> bool:
    return datetime.now().weekday() in (0, 1, 2, 3, 4, 5 , 6, 7, 8) and datetime.now().hour in ([i for i in (range(6, 24))])


class OfficeHoursMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any],
    ) -> Any:
        if office_hours():
            return await handler(event, data)

        await event.answer('BOT AVALIABLE in: \r\nmonday-friday from 6 to 23. Come during business hours')