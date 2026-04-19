from aiogram import Router,F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from keyboards.default_keyboards import main_menu
from keyboards.inline_keyboards import yana_tugma,retsept_tugmalari
from aiogram.types import CallbackQuery
from utils.ai import retsept_olish, kunlik_menyu_olish, haftalik_menyu_olish,mahsulotlar_royxati_olish,tayyorlash_usuli_olish
from states.states import RetseptState, KunlikMenyuState, HaftalikMenyuState,TayyorlashState
from aiogram.enums import ChatAction
user_router = Router()

@user_router.message(CommandStart())
async def start_handler(message: Message,state: FSMContext):
    await state.clear()
    await message.answer(
        f"Salom, {message.from_user.full_name}! 👋\n\n"
        "🍽️ <b>Ovqat Yordamchisi</b> ga xush kelibsiz!\n\n"
        "Men sizga quyidagilarda yordam bera olaman:\n"
        "🥘 /retsept — Retsept tavsiya\n"
        "🔥 /haftalik_menyu — Haftalik ovqat menyu\n"
        "📅 /menyu — Kunlik ovqat menyu\n"
        "❓ /help — Yordam",
        reply_markup=main_menu(),
        parse_mode="HTML"
    )

@user_router.message(Command("help"))
async def help_handler(message: Message):
    await message.answer(
        "❓ <b>Yordam</b>\n\n"
        "🥘 /retsept — Mahsulot yozing, retsept tavsiya qilaman\n"
        "🔥 /haftalik_menyu — Haftalik ovqat menyusini tuzib beraman\n"
        "📅 /menyu — Kunlik ovqat menyusini tuzib beraman\n\n"
        "Biron bir muammo bo'lsa @xojiyevdavron ga murojaat qiling! 🙂",
        parse_mode="HTML"
    )

@user_router.message(Command("retsept"))
async def retsept_handler(message: Message):
    await message.answer(
        "🥘 Qanday mahsulotlar bor? Yozing, retsept tavsiya qilaman!\n\n"
        "<i>Masalan: tuxum, pomidor, piyoz</i>",
        parse_mode="HTML"
    )

@user_router.message(Command("haftalik_menyu"))
async def haftalik_menyu_handler(message: Message):
    await message.answer(
        "📆 Haftalik menyu tuzib beraman!\n\n"
        "Qanday ovqatlanishni xohlaysiz?\n"
        "<i>Masalan: kamkaloriyali, to'yimli, vegetarian</i>",
        parse_mode="HTML"
    )

@user_router.message(Command("menyu"))
async def menyu_handler(message: Message):
    await message.answer(
        "📅 Kunlik menyu tuzib beraman!\n\n"
        "Qanday ovqatlanishni xohlaysiz?\n"
        "<i>Masalan: kamkaloriyali, to'yimli, vegetarian</i>",
        parse_mode="HTML"
    )

@user_router.message(F.text == "🥘 Retsept")
async def retsept_tugma_handler(message: Message,state:FSMContext):
    await state.set_state(RetseptState.mahsulot_kutish)
    await message.answer(
        "🥘 Qanday mahsulotlar bor? Yozing, retsept tavsiya qilaman!\n\n"
        "<i>Masalan: tuxum, pomidor, piyoz</i>",
        reply_markup=yana_tugma("retsept"),
        parse_mode="HTML"
    )

@user_router.message(RetseptState.mahsulot_kutish)
async def retsept_javob_handler(message: Message, state: FSMContext):
    await message.bot.send_chat_action(message.chat.id, ChatAction.TYPING)
    await message.answer("⏳ Retsept tayyorlanmoqda...")
    javob = await retsept_olish(message.text)
    await state.update_data(retsept=javob)
    await state.clear()
    await message.answer(javob, reply_markup=retsept_tugmalari())

@user_router.message(F.text == "📅 Kunlik menyu")
async def kunlik_menyu_tugma_handler(message: Message, state: FSMContext):
    await state.set_state(KunlikMenyuState.talab_kutish)
    await message.answer(
        "📅 Kunlik menyu tuzib beraman!\n\n"
        "Qanday ovqatlanishni xohlaysiz?\n"
        "<i>Masalan: kamkaloriyali, to'yimli, vegetarian</i>",
        reply_markup=yana_tugma("kunlik"),
        parse_mode="HTML"
    )
@user_router.message(KunlikMenyuState.talab_kutish)
async def kunlik_menyu_javob_handler(message: Message, state: FSMContext):
    await message.bot.send_chat_action(message.chat.id, ChatAction.TYPING)
    await message.answer("⏳ Kunlik menyu tayyorlanmoqda...")
    javob = await kunlik_menyu_olish(message.text)
    await state.clear()
    await message.answer(javob, reply_markup=main_menu())

@user_router.message(F.text == "📆 Haftalik menyu")
async def haftalik_menyu_tugma_handler(message: Message, state: FSMContext):
    await state.set_state(HaftalikMenyuState.talab_kutish)
    await message.answer(
        "📆 Haftalik menyu tuzib beraman!\n\n"
        "Qanday ovqatlanishni xohlaysiz?\n"
        "<i>Masalan: kamkaloriyali, to'yimli, vegetarian</i>",
        reply_markup=yana_tugma("haftalik"),
        parse_mode="HTML"
    )
@user_router.message(HaftalikMenyuState.talab_kutish)
async def haftalik_menyu_javob_handler(message: Message, state: FSMContext):
    await message.bot.send_chat_action(message.chat.id, ChatAction.TYPING)
    await message.answer("⏳ Haftalik menyu tayyorlanmoqda...")
    javob = await haftalik_menyu_olish(message.text)
    await state.clear()
    await message.answer(javob, reply_markup=main_menu())


@user_router.message(F.text == "❓ Yordam")
async def yordam_tugma_handler(message: Message):
    await message.answer(
        "❓ <b>Yordam</b>\n\n"
        "🥘 /retsept — Mahsulot yozing, retsept tavsiya qilaman\n"
        "🔥 /haftalik_menyu — Haftalik ovqat menyusini tuzib beraman\n"
        "📅 /menyu — Kunlik ovqat menyusini tuzib beraman\n\n"
        "Biron bir muammo bo'lsa @xojiyevdavron ga murojaat qiling! 🙂",
        parse_mode="HTML"
    )


@user_router.callback_query(F.data.startswith("yana_"))
async def yana_callback(callback: CallbackQuery):
    tur = callback.data.split("_")[1]
    if tur == "retsept":
        await callback.message.answer("🥘 Yana mahsulot yozing!", reply_markup=yana_tugma("retsept"), parse_mode="HTML")
    elif tur == "kunlik":
        await callback.message.answer("📅 Yana kunlik menyu uchun yozing!", reply_markup=yana_tugma("kunlik"), parse_mode="HTML")
    elif tur == "haftalik":
        await callback.message.answer("📆 Yana haftalik menyu uchun yozing!", reply_markup=yana_tugma("haftalik"), parse_mode="HTML")
    await callback.answer()

@user_router.callback_query(F.data == "bosh_menyu")
async def bosh_menyu_callback(callback: CallbackQuery):
    await callback.message.answer("🏠 Bosh menyu:", reply_markup=main_menu(), parse_mode="HTML")
    await callback.answer()


@user_router.callback_query(F.data == "mahsulotlar_royxati")
async def mahsulotlar_royxati_callback(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer("⏳ Mahsulotlar ro'yxati tayyorlanmoqda...")

    # Retsept matnini olish
    retsept = callback.message.text
    javob = await mahsulotlar_royxati_olish(retsept)
    await callback.message.answer(f"🛒 <b>Xarid ro'yxati:</b>\n\n{javob}", reply_markup=main_menu())

@user_router.message(F.text == "👨‍🍳 Tayyorlash usuli")
async def tayyorlash_tugma_handler(message: Message, state: FSMContext):
    await state.set_state(TayyorlashState.ovqat_kutish)
    await message.answer(
        "👨‍🍳 Qaysi ovqatni tayyorlamoqchisiz?\n\n"
        "<i>Masalan: osh, manti, lag'mon</i>",
        parse_mode="HTML"
    )

@user_router.message(TayyorlashState.ovqat_kutish)
async def tayyorlash_javob_handler(message: Message, state: FSMContext):
    await message.bot.send_chat_action(message.chat.id, ChatAction.TYPING)
    await message.answer("⏳ Tayyorlash usuli yuklanmoqda...")
    javob = await tayyorlash_usuli_olish(message.text)
    await state.clear()
    await message.answer(javob, reply_markup=retsept_tugmalari())