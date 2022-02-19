import asyncio
import logging
import os
import sys
import json
import asyncio
import time
import telegram.ext as tg

from typing import list
from telethon import TelegramClient
from telethon.sessions import MemorySession
from configparser import ConfigParser
from ptbcontrib.postgres_persistence import PostgresPersistence
from logging.config import fileConfig

StartTime = time.time()


def get_user_list(__init__, key):
    with open("{}/ichigochan/{}".format(os.getcwd(), __init__), "r") as json_file:
        return json.load(json_file)[key]
      
FORMAT = "[IchigoChan] %(message)s"
logging.basicConfig(
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
    format=FORMAT,
    datefmt="[%X]",
)

logging.getLogger('ptbcontrib.postgres_persistence.postgrespersistence').setLevel(logging.WARNING)

logs = logging.getLogger('[Ichigochan]')
logs.info("I'm ichigo! I'm starting do waitoo waitoo (~‾▿‾)~ UwU.")

if sys.version_info[0] < 3 or sys.version_info[1] < 9:
    LOGGER.error(
        "You MUST have a python version of at least 3.9! Multiple features depend on this. Bot quitting."
    )
    sys.exit(1)
    
ENV = bool(os.environ.get("ENV", False))
if ENV:
    TOKEN = os.environ.get("TOKEN", None)
    try:
        OWNER_ID = int(os.environ.get("OWNER_ID", None))
    except ValueError:
        raise Exception("Your OWNER_ID env variable is not a valid integer.")
        OWNER_USERNAME = os.environ.get("OWNER_USERNAME", None)
        BOT_USERNAME = os.environ.get("BOT_USERNAME", None)
        API_ID = os.environ.get("API_ID", None)
        API_HASH = os.environ.get("API_HASH", None)
        DB_URL = os.environ.get("DATABASE_URL")
        BOT_ID = int(os.environ.get("BOT_ID", None))
        BOT_USERNAME = os.environ.get("BOT_USERNAME", None)
        DB_URL = DB_URL.replace("postgres://", "postgresql://", 1)
        NO_LOAD = os.environ.get("NO_LOAD", "translation").split()
        LOAD = os.environ.get("LOAD", "").split()
        ALLOW_EXCL = os.environ.get("ALLOW_EXCL", False)

    else:
        from Ichigochan.config import Development as Config
    
        TOKEN = Config.TOKEN
      
try: 
   OWNER_ID = Int(Config.OWNER_ID)
except ValueError:
     raise Exception("Your OWNER_ID variable is not a valid integer.")
 
   OWNER_USERNAME = Config.OWNER_USERNAME
    
   API_ID = Config.API_ID
   API_HASH = Config.API_HASH
   DB_URL = Config.SQLALCHEMY_DATABASE_URI
   BOT_USERNAME = Config.BOT_USERNAME
   BOT_ID = Config.BOT_ID
   LOAD = Config.LOAD
   NO_LOAD = Config.NO_LOAD

from ichigochan.modules.sql import SESSION

defaults = tg.Defaults(run_async=True)
updater = tg.Updater(TOKEN, workers=WORKERS, use_context=True)
telethn = TelegramClient(MemorySession(), API_ID, API_HASH)
dispatcher = updater.dispatcher
print("[INFO]: INITIALIZING AIOHTTP SESSION")
aiohttpsession = ClientSession()

pbot = Client(
    ":memory:",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=TOKEN,
    workers=min(32, os.cpu_count() + 4),
)
apps = []
apps.append(pbot)
loop = asyncio.get_event_loop()

async def get_entity(client, entity):
    entity_client = client
    if not isinstance(entity, Chat):
        try:
            entity = int(entity)
        except ValueError:
            pass
        except TypeError:
            entity = entity.id
        try:
            entity = await client.get_chat(entity)
        except (PeerIdInvalid, ChannelInvalid):
            for kp in apps:
                if kp != client:
                    try:
                        entity = await kp.get_chat(entity)
                    except (PeerIdInvalid, ChannelInvalid):
                        pass
                    else:
                        entity_client = kp
                        break
            else:
                entity = await kp.get_chat(entity)
                entity_client = kp
    return entity, entity_client

async def eor(msg: Message, **kwargs):
    func = msg.edit_text if msg.from_user.is_self else msg.reply
    spec = getfullargspec(func.__wrapped__).args
    return await func(**{k: v for k, v in kwargs.items() if k in spec})


# Load at end to ensure all prev variables have been set
from Tanji.modules.helper_funcs.handlers import (
    CustomCommandHandler,
    CustomMessageHandler,
    CustomRegexHandler,
)

# make sure the regex handler can take extra kwargs
tg.RegexHandler = CustomRegexHandler
tg.CommandHandler = CustomCommandHandler
tg.MessageHandler = CustomMessageHandler
 
