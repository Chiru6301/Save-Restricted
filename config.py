# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "28817205"))
API_HASH = getenv("API_HASH", "f319d02866bf7b83e4de31002f6ba8a3")
BOT_TOKEN = getenv("BOT_TOKEN", "7737490454:AAE5VVCe8R6xnvy6yFPp320i1JH_dZSDOqk")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7935947598").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://chiruedizz:WmzSiQlS35fLDImn@cluster0.4o4zl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002468082777")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002262582661"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "5"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "5000"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
