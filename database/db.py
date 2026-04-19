import aiosqlite

DB_PATH = "database/users.db"

async def create_table():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                full_name TEXT,
                username TEXT,
                joined_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                is_ban INTEGER DEFAULT 0
            )
        """)
        await db.commit()