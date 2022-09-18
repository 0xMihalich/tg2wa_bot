class tg_to_wa_error(Exception):
    def __init__(self, text: str="error"):
        self.text = text
