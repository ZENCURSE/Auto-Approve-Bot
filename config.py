import os
from typing import List

API_ID = os.environ.get("API_ID", "")
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
ADMIN = int(os.environ.get("ADMIN", "6426143861"))
PICS = (os.environ.get("PICS", "https://i.ibb.co/GQs3pkNb/9ac5043ae499.jpg https://i.ibb.co/NgDPVg0z/8cc6914ebc13.jpg")).split()
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1004450199083"))
NEW_REQ_MODE = os.environ.get("NEW_REQ_MODE", "True").lower() == "true"
DB_URI = os.environ.get("DB_URI", "")
DB_NAME = os.environ.get("DB_NAME", "approve")
IS_FSUB = os.environ.get("IS_FSUB", "False").lower() == "true"  # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNELS", "-1003766203099").split())) # Add Multiple channel ids
AUTH_REQ_CHANNELS = list(map(int, os.environ.get("AUTH_REQ_CHANNELS", "").split())) # Add Multiple channel ids
FSUB_EXPIRE = int(os.environ.get("FSUB_EXPIRE", 2))  # minutes, 0 = no expiry
PING_URL = os.environ.get("PING_URL", "") # Service URL for Keep-Alive
VERSION = os.environ.get("VERSION", "3.0")
SOURCE_CODE = os.environ.get("SOURCE_CODE", "https://graph.org/Nigga-09-13-4")
