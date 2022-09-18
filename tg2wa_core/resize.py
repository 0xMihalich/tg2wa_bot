from PIL import Image
from asyncio import get_running_loop
from functools import partial
from .fix_size import fix_size


def resizer(frame: str, fmt: str="PNG"):
    img = Image.open(frame)
    img_resized = Image.new(mode="RGBA", size=(512, 512))
    img_resized.paste(img, fix_size(img.size))
    img_resized.save(frame, fmt)
    del img, img_resized


async def resize(frame: str, fmt: str="PNG"):
    await get_running_loop().run_in_executor(None, partial(resizer, frame, fmt))
