import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("6969577050:AAFeNsbUqhXzHMiHpB45f4DTTLWZWWDYhk8", "")

    APP_ID = int(os.environ.get("APP_ID", 10027276))

    API_HASH = os.environ.get("API_HASH", "ce5e8cd00a5bdd3c09c5f1489c4fb858")
