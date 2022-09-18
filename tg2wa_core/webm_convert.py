from aiofiles import tempfile
from asyncio import gather
from typing import List
from glob import glob
from .create_wastickers import create_wastickers
from .downloader import downloader
from .process import process
from .resize import resize
from .webp_maker import webp_maker


async def webm_downloader(app: object, pack: dict, count: int, webm_folder: str, webp_folder: str):
    await downloader(app, pack, count, webm_folder, "webm")
    webm = f"{webm_folder}/{count}.webm"
    webp = f"{webp_folder}/{count}.webp"
    async with tempfile.TemporaryDirectory() as png_folder:
        await process(['ffmpeg', '-c:v', 'libvpx-vp9', '-i', webm, '-r', '25', f'{png_folder}/%03d.png'])
        width, height = pack['width'], pack['height']
        if any(size != 512 for size in (width, height)):
            await gather(*[resize(png_files) for png_files in glob(f'{png_folder}/*')])
        await webp_maker(png_folder, webp)
    del width, height, webm, webp


async def webm_convert(app: object, chat_id: int, author: str, title: str, stickerpacks: List[List[dict]], wa_folder: str):
    for num, packs in enumerate(stickerpacks):
        async with tempfile.TemporaryDirectory() as webp_folder:
            async with tempfile.TemporaryDirectory() as webm_folder:
                await gather(*[webm_downloader(app, pack, count, webm_folder, webp_folder) for count, pack in enumerate(packs)])
            await create_wastickers(app, chat_id, author, title, num, webp_folder, wa_folder, len(stickerpacks))
