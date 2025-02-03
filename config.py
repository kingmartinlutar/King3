import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("25444644")
API_HASH = os.getenv("bff60a5f566d9a54c175b0001ba9615b")
BOT_TOKEN = os.getenv("8056263089:AAHMI88zp5GyHzeaQS82BKNzGFzEI_5DAPs")
ADMINS = [int(admin) for admin in os.getenv("ADMINS").split("5969730414,")]
