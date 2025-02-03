async def get_content(client, message):
    chat_id = message.text.split('/')[-1]
    posts = await client.get_messages(chat_id, range(100, 120))
    for post in posts:
        await client.copy_message(message.chat.id, post.chat.id, post.id)

async def download_media(client, message):
    media = await client.download_media(message)
    # Handle media (e.g., save to storage)
