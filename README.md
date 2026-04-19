# 🍽️ Ovqat Yordamchisi Bot

AI yordamida ovqat retseptlari, kunlik va haftalik menyu tavsiya qiluvchi Telegram bot.

## 🚀 Imkoniyatlar

- 🥘 **Retsept** — Mahsulotlar asosida retsept tavsiya qilish
- 👨‍🍳 **Tayyorlash usuli** — Ovqat tayyorlash bosqichlari
- 📅 **Kunlik menyu** — Kunlik ovqat menyusi
- 📆 **Haftalik menyu** — Haftalik ovqat menyusi
- 🛒 **Xarid ro'yxati** — Retsept asosida mahsulotlar ro'yxati
- 👨‍💼 **Admin panel** — Foydalanuvchilar boshqaruvi

## 🛠️ Texnologiyalar

- Python 3.11+
- Aiogram 3.x
- Groq API (LLaMA 3.3 70B)
- SQLite + aiosqlite

## ⚙️ O'rnatish

1. Reponi klonlash:
```bash
git clone https://github.com/hojiyevdavron65-crypto/ovqat-yordamchisi-bot.git
cd ovqat-yordamchisi-bot
```

2. Virtual muhit yaratish:
```bash
python -m venv venv
venv\Scripts\activate
```

3. Kerakli paketlarni o'rnatish:
```bash
pip install -r requirements.txt
```

4. `.env` fayl yaratish:
```env
BOT_TOKEN=your_bot_token
GROQ_API_KEY=your_groq_api_key
ADMIN_IDS=your_telegram_id
```

5. Botni ishga tushirish:
```bash
python app.py
```

## 📁 Loyiha strukturasi
├── data/
│   └── config.py
├── database/
│   ├── db.py
│   └── users.py
├── handlers/
│   ├── users.py
│   └── admins.py
├── keyboards/
│   ├── default/
│   │   └── main_menu.py
│   └── inline/
│       └── actions.py
├── middlewares/
│   └── register.py
├── states/
│   └── states.py
├── utils/
│   ├── ai.py
│   └── typing.py
├── loader.py
├── app.py
└── .env

## 👨‍💻 Muallif

- Telegram: @xojiyevdavron