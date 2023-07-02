from os import getenv

from dotenv import load_dotenv

load_dotenv()

admins = {}

SESSION_NAME = getenv("SESSION_NAME", "")

BOT_TOKEN = getenv("BOT_TOKEN", "")
API_ID = int(getenv("API_ID", "22839370"))
API_HASH = getenv("API_HASH", "7fb99db07ddecec3e7a1f02da9730c33")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "LovelyXSupport")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "LovelyXAssociation")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1929914544").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1929914544").split()))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "12"))

IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/31e9ecee16a46575267a4.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/d744707634106cf76627a.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/d8f8fc1de9110b93ca94c.jpg")
YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL", "https://te.legra.ph/file/bc5556476395a0c8e109b.jpg"
)
