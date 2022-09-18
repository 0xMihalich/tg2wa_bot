from aiofiles import open as async_open


async def file_create(file_name: str, file_data: str):
    async with async_open(file_name, 'wb') as file:
        await file.write(file_data.encode("utf-8"))
