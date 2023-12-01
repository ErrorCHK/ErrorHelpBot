
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = "25183104" # integer value, dont use ""
    API_HASH = "e26e3936f8bd637f2724c728ea50c6af"
    TOKEN = "6770677388:AAE0JX4paT0vVza1h-uYjMGt3bssOyx5pjI"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 6181269269 # If you dont know, run the bot and do /id in your private chat with it, also an integer
    
    SUPPORT_CHAT = "https://t.me/+i_cCG3Gwh9U1MmE1"  # Your own group for support, do not add the @
    START_IMG = "https://telegra.ph/file/8226139581c9711fe8a07.jpg"
    EVENT_LOGS = (-4012114975)  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    MONGO_DB_URI= "mongodb+srv://errorkamoto:iRXGNBZeqYizjUZR@cluster0.fxcbbcj.mongodb.net/?retryWrites=true&w=majority"
    # RECOMMENDED
    DATABASE_URL = "postgres://kkaazmgz:GKwmsZow2Lrww098Cw3rh-7FRsCqVEn1@hansken.db.elephantsql.com/kkaazmgz"  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        "Z7PV8COX8N3C1HST"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "HYOHUKE9BAAB"
    # Get your API key from https://timezonedb.com/api

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
