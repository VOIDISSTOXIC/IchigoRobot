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
        BOT_USERNAME = os.environ.get("BOT_USERNAME", None)
        API_ID = os.environ.get("API_ID", None)
        API_HASH = os.environ.get("API_HASH", None)
        NO_LOAD = os.environ.get("NO_LOAD", "translation").split()
        LOAD = os.environ.get("LOAD", "").split()
        ALLOW_EXCL = os.environ.get("ALLOW_EXCL", False)

    else:
        from Ichigochan.config import Development as Config
    
        TOKEN = Config.TOKEN
      
try: 
   OWNER_ID = Int(Config.OWNER_ID)
except Value error:
     raise Exception("Your OWNER_ID variable is not a valid integer.")


 
