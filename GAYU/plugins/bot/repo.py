from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from GAYU import app
from config import BOT_USERNAME
from GAYU.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
✰ 𝗪ᴇʟᴄᴏᴍᴇ ᴛᴏ ʙᴜɢɢᴜ  𝗥ᴇᴘᴏs ✰
 
✰ 𝗥ᴇᴘᴏ ᴛᴏ 𝗡ʜɪ 𝗠ɪʟᴇɢᴀ 𝗬ʜᴀ
 
✰ 🦚Radhe Radhe🦚

✰ || @Buggu_Music_Bot ||
 
✰ 𝗥ᴜɴ 24x7 𝗟ᴀɢ 𝗙ʀᴇᴇ 𝗪ɪᴛʜᴏᴜᴛ 𝗦ᴛᴏᴘ
 
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔ᴅᴅ ᴍᴇ 𝗠ᴀʙʏ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝗛ᴇʟᴘ", url="https://t.me/FRIENDS_ZONE_CHATTING_GROUP"),
          InlineKeyboardButton("Legend", url="https://t.me/FRIENDS_ZONE_CHATTING_GROUP"),
          ],
               [
                InlineKeyboardButton("BᵤGGᵤ", url=f"https://t.me/FRIENDS_ZONE_CHATTING_GROUP"),
],
[
InlineKeyboardButton("𝗠ᴀɪɴ 𝗕ᴏᴛ", url=f"https://t.me/FRIENDS_ZONE_CHATTING_GROUP"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://graph.org/file/995db5cff091efade4df4-ba501da80714fc0c7b.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
