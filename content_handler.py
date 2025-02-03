from pyrogram import Client

async def login(client: Client, message):
    phone_number = message.text.split()[1]
    await client.send_code(phone_number)
    code = await get_user_input("Enter the code you received:")
    await client.sign_in(phone_number, code)
    session_string = await client.export_session_string()
    # Store session_string securely

async def logout(client: Client, message):
    await client.log_out()
