from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8974063060:AAGPR-u7cgD4hBSSgQ75rJHN5ssBGwy_9gI"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(
                "📢 کانال رسمی بازینو",
                url="https://t.me/channelbazino"
            )
        ],
        [
            InlineKeyboardButton(
                "💬 گروه پشتیبانی",
                url="https://t.me/poshtibanibazino"
            )
        ],
        [
            InlineKeyboardButton(
                "📞 ارتباط با پشتیبانی",
                url="https://t.me/bazino2026"
            )
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🎮 به ربات رسمی بازینو خوش آمدید.\n\nیکی از گزینه‌های زیر را انتخاب کنید:",
        reply_markup=reply_markup
    )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("BAZINO Bot is Running...")
app.run_polling()
