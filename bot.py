import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Token aur Data
TOKEN = "8974809627:AAHyW5oMd7F-XCGlLFirJNwF_Udt-iTLKLU" # Apna token yahan update kar lena agar change kiya ho

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Join Channel 1", url="https://t.me/ThePhantomOFC"), InlineKeyboardButton("Join Channel 2", url="https://t.me/+_YUQcKpkFUIxMDc1")],
        [InlineKeyboardButton("Join Channel 3", url="https://t.me/+lAslisnneegyYTI1"), InlineKeyboardButton("Join Channel 4", url="https://t.me/+ZkUmhOPwtIdhNzE1")],
        [InlineKeyboardButton("Join Channel 5", url="https://t.me/+hoN6botionUxNzRl")],
        [InlineKeyboardButton("✅ Verify Now", callback_data="verify")]
    ]
    await update.message.reply_text("👋 Welcome! Please join all channels first:", reply_markup=InlineKeyboardMarkup(keyboard))

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "verify":
        keyboard = [
            [InlineKeyboardButton("1 • Username and password", callback_data="hack_data")],
            [InlineKeyboardButton("2 • CONFIG FILES", url="https://t.me/+VdVcZZgxIqllOWFl")],
            [InlineKeyboardButton("3 • PAID PRODUCTS", url="https://t.me/cheatz_exe")]
        ]
        await query.edit_message_text("✅ Verified! Choose an option:", reply_markup=InlineKeyboardMarkup(keyboard))
    elif query.data == "hack_data":
        await query.edit_message_text("🔐 Username: `TR-TRIAL`\nPassword: `3439`")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("Bot is running...")
    app.run_polling()
