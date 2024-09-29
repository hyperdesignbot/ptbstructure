from telegram import Update
from telegram.ext import ContextTypes


async def join_request_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("in join_request_buttons")