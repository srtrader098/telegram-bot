from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

BOT_TOKEN = "8306282619:AAGn7ox3ekrrhYxxlBjsUKmWEiiDUGxG5G0"  # <-- Copy-paste করো এখানে

CHANNEL_USERNAME = "@S_RTRADERTEAM_098"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    try:
        member = await context.bot.get_chat_member(CHANNEL_USERNAME, user_id)
        if member.status in ["member", "administrator", "creator"]:
            await update.message.reply_text("✅ Access Granted!\nWelcome to S_R Trader Gift Bot 🎁")
        else:
            raise Exception("Not a member")
    except:
        keyboard = [[InlineKeyboardButton("🔔 Join Channel", url=f"https://t.me/{CHANNEL_USERNAME.replace('@','')}")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("❌ Access Denied!\nJoin our channel first 👇", reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await start(update, context)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

print("Bot is running...")
app.run_polling()
