
from datetime import datetime
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# === Налаштування ===
BOT_TOKEN = "8491835130:AAGqqPYtS2LqJjRx4Hz04DsyO8RWBDATtaQ"
START_DATETIME = datetime(2025, 9, 25, 9, 34)
ALLOWED_USER_ID = 7292634641  # Твій Telegram ID

# === Команди ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привіт! Напиши /admins, щоб побачити скільки ти вже на адмінці 💪")

async def admins(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    if user_id != ALLOWED_USER_ID:
        await update.message.reply_text("❌ Тобі заборонено використовувати цю команду.")
        return

    now = datetime.now()
    diff = now - START_DATETIME
    days = diff.days
    hours = diff.seconds // 3600
    minutes = (diff.seconds % 3600) // 60

    current_date = now.strftime("%d.%m.%Y %H:%M")
    start_date_str = START_DATETIME.strftime("%d.%m.%Y %H:%M")

    message = (
        "🏆 Grand Mobile | Адмінка 🏆\n"
        f"📅 Початок адмінки: {start_date_str}\n"
        f"📆 Поточна дата: {current_date}\n"
        f"🕓 Ти вже {days} днів, {hours} годин і {minutes} хвилин на адмінці!\n\n"
        "💪 Продовжуй у тому ж дусі!"
    )

    await update.message.reply_text(message)

# === Запуск бота ===
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("admins", admins))

app.run_polling()
