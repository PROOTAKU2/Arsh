from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from VILLAIN_MUSIC import app

MUST_JOIN = -1002710057429  # Private channel ID
JOIN_LINK_1 = "https://t.me/+f9CCUJiRK6E1YzJh"
JOIN_LINK_2 = "https://t.me/+6lt8_5E86UcyNGYx"

@app.on_message(filters.private & filters.incoming, group=-1)
async def must_join_channel(client: Client, message: Message):
    try:
        try:
            await client.get_chat_member(MUST_JOIN, message.from_user.id)
            # ✅ User is in the channel, do nothing
        except UserNotParticipant:
            # ❌ User not in channel, show join message
            await message.reply_photo(
                photo="https://files.catbox.moe/bm6nx8.jpg",
                caption=(
                    "❌ ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ ᴊᴏɪɴᴇᴅ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ ʏᴇᴛ!\n\n"
                    f"📢 [ᴊᴏɪɴ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ ʜᴇʀᴇ]({JOIN_LINK_1}) & [ᴇxᴛʀᴀ ᴄʜᴀɴɴᴇʟ]({JOIN_LINK_2})\n\n"
                    "ᴛʜᴇɴ sᴇɴᴅ /start ᴀɢᴀɪɴ ✅"
                ),
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("• ᴊᴏɪɴ 1 •", url=JOIN_LINK_1)],
                    [InlineKeyboardButton("• ᴊᴏɪɴ 2 •", url=JOIN_LINK_2)]
                ])
            )
            await message.stop_propagation()
    except ChatAdminRequired:
        print(f"⚠️ Bot needs admin rights in channel ID: {MUST_JOIN}")
    except ChatWriteForbidden:
        pass
