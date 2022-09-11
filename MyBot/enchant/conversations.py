from MyBot.base import app
from discord.ext.commands.context import Context
from MyBot.enchant import Enchant

@app.command()
async def 인챈트(ctx:Context,name:str):
    await ctx.send(Enchant.search(name))
