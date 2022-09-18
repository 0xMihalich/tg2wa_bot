from pyrogram import filters
from .get_links import get_links
from .get_pack import get_pack
from .convert import convert
from .session import app


async def get_json_pack(app: object, chat_id: int, set_name: str):
    stickerpack = await get_pack(set_name)
    if not stickerpack:
        await app.send_message(chat_id, f"can't get pack {set_name}")
        return False
    elif not stickerpack['ok']:
        await app.send_message(chat_id, f"fail to get pack {set_name}")
        return False
    await convert(app, chat_id, stickerpack['result'])


@app.on_message(filters.sticker & filters.private)
async def reply_from_sticker(client, message):
    if not message.sticker.set_name:
        await message.reply("sorry, can't get pack for this sticker")
        return False
    await get_json_pack(client, message.chat.id, message.sticker.set_name)


@app.on_message(filters.text & filters.private)
async def reply_from_text(client, message):
    find_packs = await get_links(message)
    if find_packs:
        [await get_json_pack(client, message.chat.id, pack.replace("https://t.me/addstickers/", "")) for pack in find_packs]
        return True
    await message.reply('''Send me any sticker and I convert all his sickerpack to whatsapp arhive.
Downloading stickers is simple — you just need to have the latest WhatsApp version and follow the instruction:
-Download file from bot with your sticker pack
-Download the Sticker Maker app. Go to <a href="https://play.google.com/store/apps/details?id=com.marsvard.stickermakerforwhatsapp">Google Play (Android)</a> \
or <a href="https://apps.apple.com/us/app/sticker-maker-studio/id1443326857">App store (iOS)</a> and download the app
-Open the file with the Sticker Maker app. Tap "Add to library" and then "Add to WhatsApp". Confirm the action
-Open a conversation on WhatsApp, access the sticker icon and choose some of the installed stickers
-All done. Now you can send stickers from stickerpack''')
