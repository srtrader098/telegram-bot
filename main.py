import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_USERNAME = "@S_RTRADERTEAM_098"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    try:
        member = await context.bot.get_chat_member(CHANNEL_USERNAME, user_id)
        if member.status in ["member", "administrator", "creator"]:
            await update.message.reply_text(
                "✅ Access Granted!\n\nWelcome to S_R Trader Gift Bot 🎁"
            )
        else:
            raise Exception("Not a member")
    except:
        keyboard = [
            [InlineKeyboardButton("🔔 Join Channel", url="https://t.me/S_RTRADERTEAM_098")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text(
            "❌ Access Denied!\n\nবট ব্যবহার করতে হলে আমাদের চ্যানেলে JOIN থাকতে হবে 👇",
            reply_markup=reply_markup
        )


app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot is running...")
app.run_polling()