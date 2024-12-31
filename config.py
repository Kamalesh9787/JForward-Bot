# bot developer @mr_jisshu
from os import environ 

class Config:
    
    API_ID = environ.get("API_ID", "25599491")
    API_HASH = environ.get("API_HASH", "c8e3c0561cf148a6504f27b111fc3698")
    BOT_TOKEN = environ.get("BOT_TOKEN", "") 
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '5983189506').split()]
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 

    PICS = (environ.get('PICS', 'https://dl.kpsbots.workers.dev/dl/66d3f8b1210c4d7ce3030600'))
    
    DATABASE_URI = environ.get("DATABASE_URI", "")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
    
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002037384930'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "") # FORCE SUB channel link 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "False")  # FORCE SUB ON - OFF


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
