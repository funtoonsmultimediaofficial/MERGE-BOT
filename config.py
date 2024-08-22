import os


class Config(object):
    API_HASH = os.environ.get("429c3423fba4cac53c02b8da777e93a8")
    BOT_TOKEN = os.environ.get("6659796121:AAE8cSoiKhqucrEnq8zY5KLl6PBWTLx31t8")
    TELEGRAM_API = os.environ["13786499"]
    OWNER = os.environ.get("7113960085")
    OWNER_USERNAME = os.environ.get("mrindianlekhak")
    PASSWORD = os.environ.get("FTM")
    DATABASE_URL = os.environ.get("mongodb+srv://ftmserver:ftm@cluster0.fneio.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    LOGCHANNEL = os.environ.get("-1002199200593")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID","root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle","extract-streams"]
