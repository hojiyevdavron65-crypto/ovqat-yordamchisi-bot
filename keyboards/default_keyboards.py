from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🥘 Retsept"), KeyboardButton(text="👨‍🍳 Tayyorlash usuli")],
            [KeyboardButton(text="📅 Kunlik menyu"), KeyboardButton(text="📆 Haftalik menyu")],
            [KeyboardButton(text="❓ Yordam")]
        ],
        resize_keyboard=True,
        input_field_placeholder="Tanlang..."
    )
    return keyboard