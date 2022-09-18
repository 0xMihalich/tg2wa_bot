from PIL import Image
from asyncio import get_running_loop
from functools import partial


def compressor(frame: str):
    img = Image.open(frame)
    img.save(frame, "WEBP", optimize=True, quality=60)
    del img


async def compress(frame: str):
    await get_running_loop().run_in_executor(None, partial(compressor, frame))
