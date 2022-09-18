from PIL import Image
from asyncio import gather, get_running_loop
from functools import partial


def tray_maker(webp_folder: str):
    img = Image.open(f"{webp_folder}/0.webp")
    img.thumbnail((96, 96))
    img.save(f"{webp_folder}/tray.png", "PNG")
    del img


async def make_tray(webp_folder: str):
    await get_running_loop().run_in_executor(None, partial(tray_maker, webp_folder))
