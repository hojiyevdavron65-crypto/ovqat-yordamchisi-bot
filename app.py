import asyncio
import logging
from loader import dp, bot
from data.config import ADMINS
from handlers import setup_handlers
from database.db import create_table
from middlewares.register import RegisterMiddleware
from aiogram.types import BotCommand, BotCommandScopeDefault, BotCommandScopeChat

async def set_commands(bot):
    # Oddiy foydalanuvchilar uchun
    user_commands = [
        BotCommand(command="start", description="🏠 Bosh menyu"),
        BotCommand(command="help", description="❓ Yordam"),
        BotCommand(command="retsept", description="🥘 Retsept olish"),
        BotCommand(command="kunlik_menyu", description="📅 Kunlik menyu"),
        BotCommand(command="haftalik_menyu", description="📆 Haftalik menyu"),
    ]
    await bot.set_my_commands(user_commands, scope=BotCommandScopeDefault())

    # Adminlar uchun
    admin_commands = [
        BotCommand(command="start", description="🏠 Bosh menyu"),
        BotCommand(command="help", description="❓ Yordam"),
        BotCommand(command="admin", description="👨‍💼 Admin panel"),
        BotCommand(command="statistika", description="📊 Statistika"),
        BotCommand(command="broadcast", description="📢 Xabar yuborish"),
        BotCommand(command="foydalanuvchilar", description="👥 Foydalanuvchilar"),
        BotCommand(command="ban", description="🚫 Ban"),
        BotCommand(command="unban", description="✅ Unban"),
    ]
    for admin_id in ADMINS:
        try:
            await bot.set_my_commands(admin_commands, scope=BotCommandScopeChat(chat_id=admin_id))
        except Exception:
            pass

async def main() -> None:
    await create_table()

    # Middleware ulash
    dp.message.middleware(RegisterMiddleware())
    main_router = setup_handlers()
    dp.include_router(main_router)

    logging.info("Bot ishlamoqda")
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())