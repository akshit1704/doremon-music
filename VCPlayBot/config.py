import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "phoenix_music_new")
BG_IMAGE = getenv("BG_IMAGE","https://telegra.ph/file/ffb0effc64003f4c3936d.jpg")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Doremon assistant")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "phoenix_music_suportt")
PROJECT_NAME = getenv("PROJECT_NAME", "Dormeon music")
SOURCE_CODE = getenv("SOURCE_CODE", "https://github.com/akshit1704/doremon-music")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "797768146").split()))
