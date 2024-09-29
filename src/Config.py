from os import getenv, remove, listdir

__import__("dotenv").load_dotenv()

OWNER_USER_ID = int(getenv("OWNER_USER_ID") or 0)

TOKEN = getenv("TOKEN")
API_ID, API_HASH = getenv("API_ID"), getenv("API_HASH")

