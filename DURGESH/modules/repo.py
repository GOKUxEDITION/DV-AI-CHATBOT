from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DURGESH import app

@app.on_message(filters.command("repo"))
async def start(_, msg):
    await msg.reply_photo(
        photo="https://i.postimg.cc/qvR8PTty/20241128-220025.png",
        caption="""Hey there, I'm Edition Server, your AI chatbot. ♥︎

If you want my bot repo, click below to get the source code.

Powered by @net_pro_max ✨""",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/II_Masti_Ki_Pathshala_II"),
             InlineKeyboardButton("ʀᴇᴘᴏ", url="https://t.me/II_Masti_Ki_Pathshala_II")]
        ])
    )
