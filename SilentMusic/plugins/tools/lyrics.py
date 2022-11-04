import random
import re
import string
import aiohttp

import lyricsgenius as lg
from pyrogram import filters
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)

from config import BANNED_USERS, lyrical
from strings import get_command
from SilentMusic import app
from SilentMusic.utils.decorators.language import language

###Commands
LYRICS_COMMAND = get_command("LYRICS_COMMAND")

@app.on_message(
    filters.command(LYRICS_COMMAND) & ~filters.edited & ~BANNED_USERS
)
@language
async def lrsearch(client, message: Message, _):
    if len(message.command) < 2:
        return await message.reply_text(_["lyrics_1"])
    title = message.text.split(None, 1)[1]
    m = await message.reply_text(_["lyrics_2"])

    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://techzbotsapi.herokuapp.com/lyrics?query={title}") as resp:
            if resp.status == 200:
                lyrics = await resp.json()
                lyrics = lyrics["lyrics"]
            else:
                lyrics = None

    if lyrics is None:
        return await m.edit(_["lyrics_3"].format(title))
    return await m.edit(lyrics)
