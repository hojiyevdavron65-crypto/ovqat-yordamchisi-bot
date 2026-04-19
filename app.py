import asyncio
import logging
from loader import dp,bot
from handlers import setup_handlers


async def main()->None:
    #Barcha routerlarni ulash
    main_router=setup_handlers()
    dp.include_router(main_router)

    logging.info("Bot ishlamoqda")
    await dp.start_polling(bot)


if __name__=="__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())