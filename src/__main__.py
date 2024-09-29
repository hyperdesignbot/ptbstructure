from .plugins.start import start
from .load_mtp_clients import load_pyro_client
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler
from .plugins.get_user_text import input_text
from .Config import TOKEN
from .plugins.join_channel import join_request_buttons
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from telegram import Update, WebAppInfo #upm package(python-telegram-bot)
from telegram.ext import Application, MessageHandler, filters, CommandHandler #upm package(python-telegram-bot)

load_dotenv()

# routes = [
#     Mount("/static", StaticFiles(directory="static"), name="static"),
# ]

app = FastAPI()
@app.get("/")
async def web_html(request: Request):
    return {'status': 'Fast APi Works!'}



def main():
    tg_app = Application.builder().token(TOKEN).arbitrary_callback_data(True).post_init(load_pyro_client).build()
    tg_app.add_handler(CommandHandler("start", start))
    tg_app.add_handler(MessageHandler(filters.TEXT & filters.ALL, input_text))
    tg_app.add_handler(CallbackQueryHandler(join_request_buttons, pattern="^JOIN"))

    tg_app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
