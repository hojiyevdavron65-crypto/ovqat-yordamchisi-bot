from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN=os.getenv("BOT_TOKEN")
ADMINS=list(map(int, os.getenv("ADMINS", "").split(",")))
GROQ_API_KEY = os.getenv("GROQ_API_KEY")