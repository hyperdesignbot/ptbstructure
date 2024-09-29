from src.Config import API_ID, API_HASH, TOKEN
from pyrogram import Client as MPTProtoClient, idle
from src import WORK_DIR

mtprotoclient = MPTProtoClient(name="bot",
                               api_id=API_ID,
                               api_hash=API_HASH,
                               bot_token=TOKEN,
                               plugins={"root": r'src/mtp_plugins'},
                               workdir=WORK_DIR,
                            )



