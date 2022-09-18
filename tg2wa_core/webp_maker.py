from os.path import getsize
from asyncio import get_running_loop
from functools import partial
from typing import List, Optional
from .process import process


def webp_command(png_folder: str, webp_file: str, fps: int) -> List[str]:
    return ['ffmpeg', '-r', '25', '-i', f'{png_folder}/%03d.png', '-r', str(fps), '-vcodec', 'webp', '-loop', '0', '-pix_fmt', 'yuva420p', '-y', '-f', 'webp', webp_file]


async def make_webp(png_folder: str, webp_file: str, fps: int) -> List[str]:
    return await get_running_loop().run_in_executor(None, partial(webp_command, png_folder, webp_file, fps))


def get_fps(webp_file: str) -> Optional[int]:
    size = getsize(webp_file)
    if size > 500000:
        if size > 2300000:
            fps=4
        elif 1900000 < size < 2300000:
            fps=5
        elif 1600000 < size < 1900000:
            fps=6
        elif 1400000 < size < 1600000:
            fps=7
        elif 1200000 < size < 1400000:
            fps=8
        elif 960000 < size < 1200000:
            fps=9
        elif 700000 < size < 960000:
            fps=10
        elif 638000 < size < 700000:
            fps=12
        elif size < 638000:
            fps=15
        return fps
    return None


async def current_fps(webp_file: str) -> Optional[int]:
    return await get_running_loop().run_in_executor(None, partial(get_fps, webp_file))


async def fps_fix(png_folder: str, webp_file: str, fps: int):
    size = await get_running_loop().run_in_executor(None, partial(getsize, webp_file))
    if size > 500000:
        await process(await make_webp(png_folder, webp_file, (fps//3)*2))


async def webp_maker(png_folder: str, webp_file: str):
    await process(await make_webp(png_folder, webp_file, 25))
    fps = await current_fps(webp_file)
    if fps:
        await process(await make_webp(png_folder, webp_file, fps))
        await fps_fix(png_folder, webp_file, fps)
    del fps
