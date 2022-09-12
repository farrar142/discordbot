import dotenv,subprocess
import discord
from typing import Dict, TypedDict,Union
from discord.ext import commands,tasks
from discord.ext.commands.context import Context
from MyBot.formatter.Formatter import Formatter
from server import User
from server.guilds.models import Guild
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
        print(args,kwargs)
        msg:discord.Message = args[0]
        user = msg.author
        User.update_call(id=user.id,name=user.name)
        for attach in msg.attachments:
            print(f"{attach=}")
            Attachment._create(id=attach.id,user_id=user.id,filename=attach.filename,url=attach.url)
        if msg.guild:
            Guild.get_or_update(id=msg.guild.id,name=msg.guild.name)
            History.create(guild_id=msg.guild.id,user_id=user.id,text=msg.content)
        return cmd
    
    def get_author(self,ctx:Context):
        return ctx.author
    
    @tasks.loop(seconds=60.0)
    async def increase_hungry(self):
        cats = Cat.call_all()
        for cat in cats:
            cat.increase_hungry()