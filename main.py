import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text = update.message.text

    if user and text:
        username = user.username or "Без username"
        full_name = f"{user.first_name or ''} {user.last_name or ''}".strip()
        user_id = user.id

        message_to_admin = (
            f"📩 Новое сообщение:\n\n{text}\n\n"
            f"👤 Отправитель:\n"
            f"ID: {user_id}\nUsername: @{username}\nИмя: {full_name}"
        )

        await context.bot.send_message(chat_id=ADMIN_ID, text=message_to_admin)
        await update.message.reply_text("✅ Сообщение отправлено.")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Бот запущен.")
    app.run_polling()
