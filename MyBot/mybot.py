import dotenv,subprocess
import discord
from typing import Dict, TypedDict,Union
from discord.ext import commands
from server import User

dotenv.load_dotenv()

class MyBot(commands.Bot):
    process:Union[None,subprocess.Popen] = None

    def runDevServer(self):
        if self.process:
            print("kill discord server")
            self.process.terminate()
        self.process = subprocess.Popen('python3 exec.py'.split(' '))

    def get_context(self,*args,**kwargs):
        cmd = super().get_context(*args,**kwargs)
        msg:discord.Message = args[0]
        user = msg.author
        User.update_call(id=user.id,name=user.name)
        return cmd