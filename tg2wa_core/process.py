from asyncio import get_running_loop, sleep
from functools import partial
from subprocess import PIPE, Popen
from typing import List, Optional


'''
Асинхронный метод вызова стороннего приложения.
Возможно делаю грязь, но добиться правильной работы встроенной в asyncio функции у меня не получилось.
'''
async def process(cmd: List[str], data: bytes=None) -> Optional[bytes]:
    for tryes in range(10):
        try:
            process_obj = await get_running_loop().run_in_executor(None, partial(Popen, cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE, bufsize=-1))
            return process_obj.communicate(data)
        except FileNotFoundError:
            await sleep(5)
