from ..bot_class import mtprotoclient
from pyrogram import filters, Client
from pyrogram.types import Message, CallbackQuery

@mtprotoclient.on_message(filters.regex('^hello'))
async def hello(bot: Client, msg:Message):
    await msg.reply_text('reply from pyro client')