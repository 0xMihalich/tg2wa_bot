from aiofiles import tempfile
from funcy import chunks
from .tgs_convert import tgs_convert
from .webm_convert import webm_convert
from .webp_convert import webp_convert


async def convert(app: object, chat_id: int, stickerpack: dict):
    async with tempfile.TemporaryDirectory() as wa_folder:
        author, title = stickerpack['name'], stickerpack['title']
        stickerpacks = list(chunks(30, stickerpack['stickers']))
        await app.send_message(chat_id, f"create whatsapp arhive for stickerpack {author} started. total stickers: {len(stickerpack['stickers'])}. total whatsapp arhives: {len(stickerpacks)}")
        try:
            if stickerpack['is_animated']: #tgs
                await tgs_convert(app, chat_id, author, title, stickerpacks, wa_folder)
            elif stickerpack['is_video']: #webm
                await webm_convert(app, chat_id, author, title, stickerpacks, wa_folder)
            else: #webp
                await webp_convert(app, chat_id, author, title, stickerpacks, wa_folder)
        except FileNotFoundError:
            await app.send_message(chat_id, f"create whatsapp arhive for stickerpack {author} fail. please, try again later")
            return False
    await app.send_message(chat_id, f"create whatsapp arhive for stickerpack {author} done. thanx for use this bot")
    del author, title, stickerpacks
