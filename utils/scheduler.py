from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from database.users import get_all_users
from utils.ai import kunlik_menyu_olish
from loader import bot

scheduler = AsyncIOScheduler()


async def kunlik_menyu_yuborish():
    users = await get_all_users()
    javob = await kunlik_menyu_olish("oddiy va to'yimli")

    for user in users:
        user_id = user[0]
        is_ban = user[4]
        if is_ban:
            continue
        try:
            await bot.send_message(
                user_id,
                f"🌅 <b>Bugungi kunlik menyu!</b>\n\n{javob}",
                parse_mode="HTML"
            )
        except Exception:
            pass


def setup_scheduler():
    scheduler.add_job(
        kunlik_menyu_yuborish,
        CronTrigger(hour=18, minute=0),  # har kuni 8:00 da
        timezone="Asia/Tashkent"
    )
    scheduler.start()