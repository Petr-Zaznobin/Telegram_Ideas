import asyncio
import time
import numpy as np
import emoji
from pyrogram import Client, filters

api_id = 1234567890
api_hash = "ur_hash"


async def main():
    async with Client("my_account", api_id, api_hash) as app:
        await app.send_message("me", "Greetings from **Pyrogram**!")

app = Client("my_account", api_id, api_hash)

@app.on_message(filters.text & filters.private)
async def edit(client, message):
    message_id = message.id
    chat_id = "me"
    times = 0.3
    print(id)
    print(message.text)
    res = ""
    sym = '|'
    for char in message.text:
        res = res + char+sym
        await app.edit_message_text(chat_id, message_id, res, disable_web_page_preview=True)
        time.sleep(0.03)
        res = res[:-1]
        await app.edit_message_text(chat_id, message_id, res, disable_web_page_preview=True)
        time.sleep(0.03)

@app.on_message(filters.text & filters.private)
async def emojik(client, message):
    message_id = message.id
    chat_id = "me"
    times = 0.6
    print(id)
    print(message.text)
    emjs = np.array(("🥰", "😍", "😘", "🤩", "😜", "🥵", "😎"))
    while(True):
        for ems in emjs:
            res = ems
            await app.edit_message_text(chat_id, message_id, res, disable_web_page_preview=True)
            time.sleep(times)

app.run()
