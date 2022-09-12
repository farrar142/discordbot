from MyBot.base import app
from discord.ext.commands.context import Context
from server.users.models import User

accumulated:int = 0
@app.command()
async def hello(ctx:Context):
    await ctx.send('Hello I am Bot!')
    
@app.command()
async def 야옹(ctx:Context):
    await ctx.send("야옹")

@app.command()
async def 물어(ctx:Context):
    # print(dir(app))
    # print(app.all_commands)
    await ctx.send('야옹!')
    
@app.command()
async def 사용자(ctx:Context):
    await ctx.send(f"{ctx.author.name}")
    
@app.command()
async def 호출횟수(ctx:Context):
    user:User = User.get(id=ctx.author.id)
    await ctx.send(f"{user.call}")

@app.command()
async def 종료(ctx:Context):
    await ctx.send("종료중")
    guild = ctx.guild
    if guild:
        await guild.leave()