from telegram import Update, MessageEntity, InlineKeyboardMarkup, InlineKeyboardButton

from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, CallbackQueryHandler, \
    InvalidCallbackData, ApplicationHandlerStop, TypeHandler

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.effective_message.reply_text(
        "Welcome to the bot!\nYou can start downloading videos by simply sending the link(s)")
