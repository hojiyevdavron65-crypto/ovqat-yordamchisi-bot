from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def yana_tugma(tur: str):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔄 Yana", callback_data=f"yana_{tur}")],
            [InlineKeyboardButton(text="🏠 Bosh menyu", callback_data="bosh_menyu")]
        ]
    )
    return keyboard

def retsept_tugmalari():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🛒 Mahsulotlar ro'yxati", callback_data="mahsulotlar_royxati")]
        ]
    )
    return keyboard