from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from data.config import ADMINS
from database.users import get_users_count, get_today_users_count, get_all_users, ban_user, unban_user
from loader import bot

admin_router = Router()


def is_admin(message: Message) -> bool:
    return message.from_user.id in ADMINS


@admin_router.message(Command("admin"))
async def admin_panel(message: Message):
    if not is_admin(message):
        await message.answer("❌ Sizda ruxsat yo'q!")
        return

    await message.answer(
        "👨‍💼 <b>Admin Panel</b>\n\n"
        "📊 /statistika — Foydalanuvchilar statistikasi\n"
        "📢 /broadcast — Barcha foydalanuvchilarga xabar\n"
        "👥 /foydalanuvchilar — Foydalanuvchilar ro'yxati\n"
        "🚫 /ban [user_id] — Foydalanuvchini bloklash\n"
        "✅ /unban [user_id] — Foydalanuvchini blokdan chiqarish",
        parse_mode="HTML"
    )


@admin_router.message(Command("statistika"))
async def statistika_handler(message: Message):
    if not is_admin(message):
        await message.answer("❌ Sizda ruxsat yo'q!")
        return

    jami = await get_users_count()
    bugun = await get_today_users_count()

    await message.answer(
        "📊 <b>Statistika</b>\n\n"
        f"👥 Jami foydalanuvchilar: <b>{jami}</b>\n"
        f"📅 Bugun qo'shilganlar: <b>{bugun}</b>",
        parse_mode="HTML"
    )


@admin_router.message(Command("foydalanuvchilar"))
async def users_list_handler(message: Message):
    if not is_admin(message):
        await message.answer("❌ Sizda ruxsat yo'q!")
        return

    users = await get_all_users()
    if not users:
        await message.answer("👥 Hozircha foydalanuvchilar yo'q.")
        return

    text = "👥 <b>Foydalanuvchilar ro'yxati:</b>\n\n"
    for user in users:
        user_id, full_name, username, joined_date, is_ban = user
        ban_status = "🚫" if is_ban else "✅"
        text += f"{ban_status} <b>{full_name}</b> | @{username} | <code>{user_id}</code>\n"

    await message.answer(text, parse_mode="HTML")


@admin_router.message(Command("broadcast"))
async def broadcast_handler(message: Message):
    if not is_admin(message):
        await message.answer("❌ Sizda ruxsat yo'q!")
        return

    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await message.answer(
            "❌ Xabar matni kiritilmadi!\n"
            "<i>Masalan: /broadcast Salom hammaga!</i>",
            parse_mode="HTML"
        )
        return

    xabar = args[1]
    users = await get_all_users()

    yuborildi = 0
    xato = 0

    await message.answer("⏳ Xabar yuborilmoqda...")

    for user in users:
        user_id = user[0]
        is_ban = user[4]
        if is_ban:
            continue
        try:
            await bot.send_message(user_id, xabar)
            yuborildi += 1
        except Exception:
            xato += 1

    await message.answer(
        f"✅ <b>Broadcast tugadi!</b>\n\n"
        f"📨 Yuborildi: <b>{yuborildi}</b>\n"
        f"❌ Xato: <b>{xato}</b>",
        parse_mode="HTML"
    )


@admin_router.message(Command("ban"))
async def ban_handler(message: Message):
    if not is_admin(message):
        await message.answer("❌ Sizda ruxsat yo'q!")
        return

    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await message.answer("❌ User ID kiritilmadi!\n<i>Masalan: /ban 123456789</i>", parse_mode="HTML")
        return

    try:
        user_id = int(args[1])
        await ban_user(user_id)
        await message.answer(f"🚫 Foydalanuvchi <code>{user_id}</code> bloklandi!", parse_mode="HTML")
    except ValueError:
        await message.answer("❌ User ID noto'g'ri!")


@admin_router.message(Command("unban"))
async def unban_handler(message: Message):
    if not is_admin(message):
        await message.answer("❌ Sizda ruxsat yo'q!")
        return

    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await message.answer("❌ User ID kiritilmadi!\n<i>Masalan: /unban 123456789</i>", parse_mode="HTML")
        return

    try:
        user_id = int(args[1])
        await unban_user(user_id)
        await message.answer(f"✅ Foydalanuvchi <code>{user_id}</code> blokdan chiqarildi!", parse_mode="HTML")
    except ValueError:
        await message.answer("❌ User ID noto'g'ri!")