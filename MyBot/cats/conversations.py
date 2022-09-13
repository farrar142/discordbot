from MyBot.base import app
from discord.ext.commands.context import Context
from server.users.models import Intimacy, User
from server.messages.models import Message
from server.cats.models import Cat,CatSerializer
from consts import COMMAND_PREFIX
from MyBot.cats.functions import Interaction
from MyBot.interfaces import CTX


@app.command()
async def 넌누구니(ctx:Context):
    cat = Cat.get_cat_from_ctx(ctx)
    msg = f"자기 이름은 {cat.name}(이)라고 하는 것 같다"
    _msg = app.formatter.single_block(app.formatter.italic(msg))
    await ctx.send(f"야옹? \n{_msg})")
    
@app.command()
async def 너의이름은(ctx:CTX,name:str):
    interaction = Interaction(ctx)
    name_before = f"{interaction.cat.name}"
    interaction.너의이름은(name)
    name_after = f"{interaction.cat.name}"
    await ctx.send(
        f"안녕 {app.formatter(name_before).bold().new_line()}"+
        f"이제부터 너의 이름은 {app.formatter(name_after).bold()}(이)란다."
    )
    await ctx.send(interaction.meow.enthusiastic())

@app.command()
async def 내츄르(ctx:CTX):
    user:User = User.get_user_from_ctx(ctx)
    await ctx.send(f"가지고 있는 츄르: {user.call}개")
    
@app.command()
async def 츄르주기(ctx:CTX,args:int=1):
    amount = 1 if not args else args
    interaction = Interaction(ctx)
    if interaction.user.call <amount:
        await ctx.send(f"츄르가 {amount-interaction.user.call}개 모잘라요!")
        return
    result = interaction.give_churr(amount=amount)
    if result.get('result'):
        msg = (app.formatter(f"{result.get('cat').name}").bold()
               .append(f"(이)가 츄르를 맛있게 먹었다\n공복도 : {result.get('hungry')}\n친밀도 + {amount}")).single_block()
        await ctx.send(f"에에에에옹!")
        await ctx.send(msg)
    else:
        await ctx.send("애옹?   ")

@app.command()
async def 친밀도(ctx:CTX):
    interaction = Interaction(ctx)
    await ctx.send(f"{app.formatter.bold(f'{interaction.cat.name}')}와(과)의 친밀도")
    await ctx.send(app.formatter.single_block(f"{interaction.intimacy.intimacy}"))
    
@app.command()
async def 배고프니(ctx:CTX):
    interaction = Interaction(ctx)
    hungry= app.formatter(f"배고픔 : {interaction.cat.hungry}").new_line().append(f"친밀도 : {interaction.intimacy.intimacy}").new_line()
    if interaction.cat.is_hungry:
        speak = interaction.meow.enthusiastic()
        speak += app.formatter.single_block(f"{app.formatter(f'{interaction.cat.name}').bold()}은(는) 배고파보인다").new_line()
    else:
        speak = interaction.meow.curious()
        speak += app.formatter.single_block(f"{interaction.cat.name}은(는) 배고파보이지 않는다").new_line()
    await ctx.send(speak+hungry)
