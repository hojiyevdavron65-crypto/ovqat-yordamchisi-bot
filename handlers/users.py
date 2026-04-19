from aiogram import Router,types
from aiogram.filters import Command


user_router=Router()

@user_router.message(Command('start'))
async def start_message(message: types.Message):
    await message.reply("Hello, World!")
