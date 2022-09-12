from MyBot.base import app
from discord.ext.commands.context import Context
from server.users.models import Intimacy, User
from server.messages.models import Message
from server.cats.models import Cat,CatSerializer
from consts import COMMAND_PREFIX
from MyBot.cats.functions import Interaction


@app.command()
async def 넌누구니(ctx:Context):
    cat = Cat.get_default_cat()
    msg = f"자기 이름은 {cat.name}(이)라고 하는 것 같다"
    _msg = app.formatter.single_block(app.formatter.italic(msg))
    await ctx.send(f"야옹? \n{_msg})")    

@app.command()
async def 내츄르(ctx:Context):
    user:User = User.get_user_from_ctx(ctx)
    await ctx.send(f"가지고 있는 츄르: {user.call}개")
    
@app.command()
async def 츄르주기(ctx:Context):
    interaction = Interaction(ctx)
    result = interaction.give_churr(amount=1)
    if result.get('result'):
        name = app.formatter.bold(result.get('cat').name)
        msg = app.formatter.single_block(f"{name}(이)가 츄르를 맛있게 먹었다\n공복도 : {result.get('hungry')}\n친밀도 + 1")
        await ctx.send(f"에에에에옹!")
        await ctx.send(msg)
    else:
        await ctx.send("애옹?   ")

@app.command()
async def 친밀도(ctx:Context):
    interaction = Interaction(ctx)
    await ctx.send(f"{app.formatter.bold(interaction.cat.name)}와(과)의 친밀도")
    await ctx.send(app.formatter.single_block(f"{interaction.intimacy.intimacy}"))
    
@app.command()
async def 배고프니(ctx:Context):
    interaction = Interaction(ctx)
    hungry= app.formatter(f"배고픔 : {interaction.cat.hungry}").new_line()
    intimacy = app.formatter(f"친밀도 : {interaction.intimacy.intimacy}").new_line()
    if interaction.cat.is_hungry:
        speak = (app.formatter(f"야옹!").bold().italic().new_line()
                 .single_block(f"{interaction.cat.name}은(는) 배고파보인다").new_line())
    else:
        speak = (app.formatter.bold(f"애옹?")
                 .italic().new_line()
                 .single_block(f"{interaction.cat.name}은(는) 배고파보이지 않는다").new_line())
    await ctx.send(speak+hungry+intimacy)