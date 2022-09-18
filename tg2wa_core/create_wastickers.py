from shutil import make_archive
from asyncio import gather, get_running_loop
from functools import partial
from .file_create import file_create
from .make_tray import make_tray


async def create_arhive(wa_arhive: str, webp_folder: str):
    await get_running_loop().run_in_executor(None, partial(make_archive, wa_arhive, 'zip', webp_folder))


async def create_wastickers(app: object, chat_id: int, author: str, title: str, num: int, webp_folder: str, wa_folder: str, total: int):
    await gather(*[file_create(f"{webp_folder}/author.txt", author), file_create(f"{webp_folder}/title.txt", title), make_tray(webp_folder)])
    wa_arhive = f"{wa_folder}/{author}_{num}"
    await create_arhive(wa_arhive, webp_folder)
    if total == 1:
        file_name = f"{author}.wastickers"
    else:
        file_name = f"{author}_{num}.wastickers"
    await app.send_document(chat_id, document=f"{wa_arhive}.zip", file_name=file_name)
