import sqlite3
from datetime import datetime
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = "8837865586:AAHkt6SceG-jRWlOSjmADzuFdS6JWNAR7Y4"

# 🗄️ SQLite database
conn = sqlite3.connect("results.db", check_same_thread=False)
c = conn.cursor()

# إنشاء table اسمها results
c.execute("""
CREATE TABLE IF NOT EXISTS results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    message TEXT,
    timestamp TEXT
)
""")
conn.commit()

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text

    # 👤 username
    username = update.message.from_user.username
    if not username:
        username = "unknown"

    # 📅 time
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 💾 save into results table
    c.execute("""
        INSERT INTO results (username, message, timestamp)
        VALUES (?, ?, ?)
    """, (username, msg, timestamp))

    conn.commit()

    print("saved:", username, msg, timestamp)

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, handle_message))

app.run_polling()