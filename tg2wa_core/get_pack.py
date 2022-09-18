from aiohttp import ClientSession
from typing import Optional
from .bot_token import bot_token


async def get_pack(set_name: str) -> Optional[dict]:
    async with ClientSession() as session:
        try:
            resp = await session.get(f"https://api.telegram.org/bot{bot_token}/getStickerSet?name={set_name}")
            return await resp.json()
        except Exception:
            return None
