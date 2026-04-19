from openai import AsyncOpenAI
from data.config import GROQ_API_KEY

client = AsyncOpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

MODEL = "llama-3.3-70b-versatile"

async def ai_sorash(savol: str) -> str:
    try:
        response = await client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "Sen o'zbek tilida javob beradigan ovqat yordamchisisisan. Har doim faqat o'zbek tilida javob ber."},
                {"role": "user", "content": savol}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Xatolik yuz berdi: {e}"

async def retsept_olish(mahsulotlar: str) -> str:
    prompt = f"""
    Sen professional oshpaz yordamchisisiz.
    Foydalanuvchida quyidagi mahsulotlar bor: {mahsulotlar}
    Shu mahsulotlar bilan tayyorlanishi mumkin bo'lgan 2-3 ta retsept tavsiya qil.
    Har bir retsept uchun:
    - Ovqat nomi
    - Kerakli mahsulotlar
    - Tayyorlash bosqichlari
    O'zbek tilida javob ber.
    """
    return await ai_sorash(prompt)

async def kunlik_menyu_olish(talab: str) -> str:
    prompt = f"""
    Sen professional dietolog yordamchisisiz.
    Foydalanuvchi talabi: {talab}
    Bugungi kun uchun to'liq ovqat menyusini tuz:
    - Nonushta
    - Tushlik
    - Kechki ovqat
    - Oraliq sneklar
    O'zbek tilida javob ber.
    """
    return await ai_sorash(prompt)

async def haftalik_menyu_olish(talab: str) -> str:
    prompt = f"""
    Sen professional dietolog yordamchisisiz.
    Foydalanuvchi talabi: {talab}
    Bir hafta (7 kun) uchun to'liq ovqat menyusini tuz.
    Har bir kun uchun:
    - Nonushta
    - Tushlik
    - Kechki ovqat
    O'zbek tilida javob ber.
    """
    return await ai_sorash(prompt)


async def mahsulotlar_royxati_olish(retsept: str) -> str:
    prompt = f"""
    Quyidagi retsept uchun xarid qilish ro'yxatini tuz:
    {retsept}

    Faqat mahsulotlar ro'yxatini chiqar, miqdori bilan.
    Masalan:
    - 2 ta tuxum
    - 1 kg un
    - 500g pomidor
    O'zbek tilida javob ber.
    """
    return await ai_sorash(prompt)

async def tayyorlash_usuli_olish(ovqat: str) -> str:
    prompt = f"""
    Sen professional oshpaz yordamchisisisan.
    Foydalanuvchi "{ovqat}" tayyorlamoqchi.
    Quyidagilarni batafsil yoz:
    - Kerakli mahsulotlar va miqdori
    - Tayyorlash bosqichlari
    - Tayyorlash vaqti
    - Qo'shimcha maslahatlar
    O'zbek tilida javob ber.
    """
    return await ai_sorash(prompt)