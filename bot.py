import random
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from telegram import Update

# Токен Telegram-бота
TOKEN = "7549308934:AAFIEqvdqttyKOVVs625GkUr6ScSgCdwMYk"

# Ключевые слова и наборы случайных ответов
TRIGGERS = {
    "привет": ["Здарова!", "Приветик!", "Йоу!", "Добрый день!"],
    "бот": ["Я тут!", "Что случилось?", "Готов ответить.", "Зову?"],
    "авито": ["Авито — это сила!", "Работал там, знаю.", "Интересно..."],
}

# Обработчик входящих сообщений
async def respond(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text.lower()

    for keyword, replies in TRIGGERS.items():
        if keyword in message:
            response = random.choice(replies)
            await update.message.reply_text(response)
            break  # отвечаем на первое совпавшее ключевое слово

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), respond))

    print("Бот запущен и слушает сообщения...")
    app.run_polling()
