from aiofiles import tempfile
from asyncio import gather
from typing import List
from .create_wastickers import create_wastickers
from .downloader import downloader


async def webp_convert(app: object, chat_id: int, author: str, title: str, stickerpacks: List[List[dict]], wa_folder: str):
    for num, packs in enumerate(stickerpacks):
        async with tempfile.TemporaryDirectory() as webp_folder:
            await gather(*[downloader(app, pack, count, webp_folder) for count, pack in enumerate(packs)])
            await create_wastickers(app, chat_id, author, title, num, webp_folder, wa_folder, len(stickerpacks))
