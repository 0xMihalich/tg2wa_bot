from os.path import exists


bot_token = None
if exists("bot_token"):
    with open("bot_token", 'r') as _token:
        bot_token = _token.read()
