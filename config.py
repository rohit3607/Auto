#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7520786912:AAHCCKb-HrJ1sd3TfKY-PY7kmMrFIS4BBMw")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "25839862"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "ef417c527eae44d9ddb662743fbbedcc")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002008354608"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "7328629001"))

#Port
PORT = os.environ.get("PORT", "8007")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://nsdh77ygz5:b0zdFJkd9frHADgT@cluster0.vvof2.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "1800")) # auto delete in seconds

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002215102799"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002001392051"))


TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#Time in seconds for message delete, put 0 to never delete
TIME = int(os.environ.get("TIME", "600"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>Hello {first} ✨\n\n I am a file store bot Powered by @Javpostr ⚡️</b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>Hello {first} ✨\n\n Please Join Our Update Channels To Continue Watching Your Favourite Javs ⚡️</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption

CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>  </b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = None

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
