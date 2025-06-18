from pyrogram import Client, filters 
from pyrogram.types import Message

API_ID = 26281694
API_HASH = "cd4c1812820a28047602f16e953b8a19"
BOT_TOKEN = "7641297559:AAE9j6biwpwY4DXUA8tkHXP65FrjytSCn7c"

app = Client("divya_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.new_chat_members)
async def welcome(client, message: Message):
    for member in message.new_chat_members:
        try:
            await message.reply_photo(
                photo="anime_banner.jpg",  # Your welcome image here
                caption=(
                    "✨ **Welcome to our family 🔥 Kya haal chaal❓**\n\n"
                    f"✦ **Name** ⇾ {member.first_name}\n"
                    f"✦ **Username** ⇾ @{member.username or 'N/A'}\n"
                    f"✦ **User ID** ⇾ `{member.id}`\n\n"
                    "🙏 **Pay attention to the Rules:**\n"
                    "╔════════════════════╗\n"
                    "║ 1 ➤ Be kind to all\n"
                    "║ 2 ➤ No abuse allowed\n"
                    "║ 3 ➤ No spam or links\n"
                    "║ 4 ➤ Avoid 18+ content 🚫\n"
                    "║ 5 ➤ Respect everyone ✨\n"
                    "╚════════════════════╝\n"
                    "🤍 **Enjoy karo!**"
                ),
                parse_mode="markdown"
            )
            await message.delete()
        except Exception as e:
            print("Error in welcome:", e)

@app.on_message(filters.command("start") & filters.private)
async def start_cmd(client, message):
    await message.reply("Hi! I'm Divya 👧 — your friendly group assistant 💫")

app.run()
