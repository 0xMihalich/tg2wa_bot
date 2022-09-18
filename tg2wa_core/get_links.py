import re


# Поиск стикерпаков в теле сообщения
async def get_links(message):
    message = str(message).lower().replace("tg://", "https://t.me/").replace("?set=", "/").replace("\\n", "\n").replace("\r", "").replace("\n", "")
    return re.findall(r'(https://t.me/addstickers/\S+[0-9a-z])', message)
