import os

from MyBot.base import app
from MyBot.conversations import *
from MyBot.messages.conversations import *
from MyBot.enchant.conversations import *
from MyBot.cats.conversations import *

from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("TOKEN","")
print("Run! Discord Server!")
app.run(TOKEN)