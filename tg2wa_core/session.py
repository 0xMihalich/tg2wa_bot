from os.path import exists
from pyrogram import Client
from .bot_token import bot_token
from .exceptions import tg_to_wa_error


if not exists("tg2wa.session"):
    print("Bot don't have auth. Please, input your data below:")
    try:
        api_id = int(input("Your api_id: "))
        api_hash = input("Your api_hash: ")
        if not bot_token:
            bot_token=input("Your bot_token: ")
        app = Client("tg2wa", api_id=api_id, api_hash=api_hash, bot_token=bot_token)
        with open("bot_token", 'wb') as _token:
            _token.write(bot_token.encode("utf-8"))
    except Exception:
        raise tg_to_wa_error("Auth error. Check your input and try again")
else:
    app = Client("tg2wa")
