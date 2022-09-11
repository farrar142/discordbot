import dotenv
import os

import discord
from discord.ext import commands

dotenv.load_dotenv()
app = commands.Bot(command_prefix='!',intents=discord.Intents.all())
app.get_context
@app.event
async def on_ready():
    print('Done')
    await app.change_presence(status=discord.Status.online, activity=None)