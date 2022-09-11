from MyBot.base import app
from discord.ext.commands.context import Context
from server.users.models import User
from server.messages.models import Message
from consts import COMMAND_PREFIX

@app.command()
async def 메모(ctx:Context,*args):
    user_id = ctx.author.id
    if len(args)==0:
        await ctx.send(f'{COMMAND_PREFIX}메모 제목 내용~~ 으로 입력해주세요')
    elif len(args)==1:
        title = args[0]
        memos = Message.my_memos_filter(user_id=user_id,title=title)
        await ctx.send(memos)
    else:
        title = args[0]
        context = '\n'.join(args[1:])
        await ctx.send(f'{title}:\n{context}')
        Message.memo(user_id=user_id,title=title,context=context)

@app.command()
async def 내메모(ctx:Context):
    memos = Message.my_memos(user_id=ctx.author.id)
    await ctx.send(memos)

@app.command()
async def 메모삭제(ctx:Context,*args):
    if len(args)==0:
        await ctx.send("메모 번호를 입력해 주세요")
    else:
        memo_id = args[0]
        if Message.delete_memo(memo_id=memo_id):
            await ctx.send(f"{memo_id}번 메모가 삭제 되었어요")
        else:
            await ctx.send(f"{memo_id}번 메모 삭제를 하지 못했어요")