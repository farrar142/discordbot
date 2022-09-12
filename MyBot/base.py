import discord
from .mybot import MyBot

from consts import COMMAND_PREFIX

app = MyBot(command_prefix=COMMAND_PREFIX,intents=discord.Intents.all())

@app.event
async def on_ready():
    print('Done')
    if not app.increase_hungry.is_running():
        app.increase_hungry.start()
    await app.change_presence(status=discord.Status.online, activity=None)
