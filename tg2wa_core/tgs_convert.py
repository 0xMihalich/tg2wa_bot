from aiofiles import tempfile
from asyncio import gather
from typing import List
from .create_wastickers import create_wastickers
from .downloader import downloader
from .process import process
from .webp_maker import webp_maker


async def tgs_downloader(app: object, pack: dict, count: int, tgs_folder: str, webp_folder: str):
    await downloader(app, pack, count, tgs_folder, "tgs")
    tgs = f"{tgs_folder}/{count}.tgs"
    webp = f"{webp_folder}/{count}.webp"
    async with tempfile.TemporaryDirectory() as png_folder:
        await process(["./tgs_to_png", "--width", "512", "--height", "512", "--fps", "25", "--output", png_folder, tgs])
        await webp_maker(png_folder, webp)
    del tgs, webp


async def tgs_convert(app: object, chat_id: int, author: str, title: str, stickerpacks: List[List[dict]], wa_folder: str):
    for num, packs in enumerate(stickerpacks):
        async with tempfile.TemporaryDirectory() as webp_folder:
            async with tempfile.TemporaryDirectory() as tgs_folder:
                await gather(*[tgs_downloader(app, pack, count, tgs_folder, webp_folder) for count, pack in enumerate(packs)])
            await create_wastickers(app, chat_id, author, title, num, webp_folder, wa_folder, len(stickerpacks))
