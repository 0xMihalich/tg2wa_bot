from os.path import getsize
from asyncio import get_running_loop, sleep
from functools import partial
from .compress import compress
from .resize import resize


async def downloader(app: object, pack: dict, count: int, folder: str, file_type: str="webp"):
    width, height, file_id = pack['width'], pack['height'], pack['file_id']
    file_name = f"{folder}/{count}.{file_type}"
    for tryes in range(10):
        try:
            await app.download_media(message=file_id, file_name=file_name)
            break
        except TimeoutError:
            await sleep(5)
    if file_type == "webp":
        if any(size != 512 for size in (width, height)):
            await resize(file_name, "WEBP")
        size = await get_running_loop().run_in_executor(None, partial(getsize, file_name))
        if size > 100000:
            await compress(file_name)
    del width, height, file_id
