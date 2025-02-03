from pyrogram import Client
from login_handler import login, logout
from content_handler import get_content, download_media
from config import API_ID, API_HASH, BOT_TOKEN

app = Client("telegram_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message()
async def handle_message(client, message):
    if message.text.startswith('/login'):
        await login(client, message)
    elif message.text.startswith('/logout'):
        await logout(client, message)
    elif message.text.startswith('https://t.me/'):
        await get_content(client, message)
    # Add more handlers as needed

if __name__ == '__main__':
    app.run()
