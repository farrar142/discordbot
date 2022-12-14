import dotenv,subprocess
from typing import Dict, TypedDict,Union
import discord
from discord.ext import commands,tasks
from discord.ext.commands.context import Context
from MyBot.formatter.Formatter import Formatter
from MyBot.interfaces import CTX
from server import User
from server.history.models import History
from server.attachments.models import Attachment
from server.cats.models import Cat

dotenv.load_dotenv()

class MyBot(commands.Bot):
    process:Union[None,subprocess.Popen] = None
    formatter=Formatter()

    def runDevServer(self):
        if self.process:
            print("kill discord server")
            self.process.terminate()
        self.process = subprocess.Popen('python3 exec.py'.split(' '))

    def get_context(self,*args,**kwargs):
        cmd = super().get_context(*args,**kwargs)
        msg:CTX = args[0]
        user = msg.author
        User.update_call(id=user.id,name=user.name)
        for attach in msg.attachments:
            print(f"{attach=}")
            Attachment._create(id=attach.id,user_id=user.id,filename=attach.filename,url=attach.url)
        if msg.guild:
            Cat.cat_factory(msg.guild.id)
            History.create(guild_id=msg.guild.id,user_id=user.id,text=msg.content)
        return cmd
    
    def get_author(self,ctx:Context):
        return ctx.author
    
    @tasks.loop(seconds=60.0)
    async def increase_hungry(self):
        cats = Cat.call_all()
        for cat in cats:
            cat.increase_hungry()
           