from aiogram import Router
from .users import user_router
from .admins import admin_router




def setup_handlers():
    main_router=Router()
    main_router.include_router(user_router)
    main_router.include_router(admin_router)


    return main_router