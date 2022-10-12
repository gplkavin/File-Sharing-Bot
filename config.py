import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5646531776:AAFpvsrih7VqvTV-FeEtt2VynZUXOVGlFGM")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "7206698"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "bedabcb3509638b2ff0fedf2492dcb08")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001159368239"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1174794359"))

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://kavinkumar:kavinkumar@cluster0.vipysuo.mongodb.net/?retryWrites=true&w=majority")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001509652119"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Vanakkam Da Maapla,{first}\n\nI LOVE to store private files Machi.Files ah send pannitu Neenga yen kitta irunthu link eduthukalaam.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1337528464").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "{first}\n\n<b>Machi, You need to join in my Channel/Group to use me\n\nVanthu Join pannu</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "😕 Message send panrathukku naan unnoda Lover illa, Files ah Send pannu Machi!"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
