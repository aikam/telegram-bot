import random
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from telegram import Update
import os

# Триггеры и ответы
TRIGGERS = {
    "привет": ["Здарова!", "Приветик!", "Йоу!", "Добрый день!"],
    "бот": ["Я тут!", "Что случилось?", "Готов ответить."],
    "авито": ["Авито — сила!", "Был там — знаю."]
}

async def respond(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text.lower()

    for word, replies in TRIGGERS.items():
        if word in message:
            await update.message.reply_text(random.choice(replies))
            break

if __name__ == "__main__":
    TOKEN = os.environ.get("BOT_TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), respond))
    print("Бот запущен...")
    app.run_polling()
