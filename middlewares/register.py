from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import Message
from database.users import add_user, is_banned


class RegisterMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        user = event.from_user

        # Foydalanuvchini bazaga saqlash
        await add_user(
            user_id=user.id,
            full_name=user.full_name,
            username=user.username or ""
        )

        # Banlangan foydalanuvchini bloklash
        if await is_banned(user.id):
            await event.answer("🚫 Siz bloklangansiz!")
            return

        return await handler(event, data)