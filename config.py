import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("6995888962:AAHA4ozq8jiip9V358b8k0zJSLMmC6GoPqg", "")

    APP_ID = int(os.environ.get("APP_ID", 21786461))

    API_HASH = os.environ.get("API_HASH", "bda65e7c142dd5841fd6843d0ded941f")
