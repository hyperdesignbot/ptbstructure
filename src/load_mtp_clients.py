from telegram.ext import Application
from .bot_class import mtprotoclient
from pyrogram import idle

async def load_pyro_client(application):
    if mtprotoclient is not None:
        await mtprotoclient.start()
        me = await mtprotoclient.get_me()
        print("me")
        await mtprotoclient.send_message('hyperdesign','msg from client')
        # await idle()
