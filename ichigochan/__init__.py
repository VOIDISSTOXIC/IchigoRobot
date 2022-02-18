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

logs.info("I'm ichigo! I'm starting do waitoo waitoo (~‾▿‾)~ UwU.")
