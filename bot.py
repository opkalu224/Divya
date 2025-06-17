from pyrogram import Client, filters
from pyrogram.types import Message
from config import API_ID, API_HASH, BOT_TOKEN

app = Client("divya_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.new_chat_members)
async def welcome_new_member(client, message):
    for user in message.new_chat_members:
        name = user.first_name or "Member"
        username = f"@{user.username}" if user.username else "No username"
        user_id = user.id

        caption = f"""
👋 Welcome to our family 😍✨ Kya haal chaal?

🌸 Name: {name}
🔖 Username: {username}
🆔 ID: {user_id}

📜 Group Rules:
1. Be respectful
2. No spam
3. No NSFW
        """

        await message.reply_photo("welcome.jpg", caption=caption)

# Auto-delete join/leave system messages
@app.on_message(filters.status_update)
async def delete_system_messages(client, message):
    await message.delete()

app.run()
