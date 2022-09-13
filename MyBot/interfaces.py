import abc
from typing import List, Optional
from discord.ext.commands.context import Context

class GuildInterface:
    id:int
    name:str
    
class AuthorInterface:
    id:int
    name:str

class AttachmentInterface:
    id:int
    filename:str
    url:str
    
    
class CTX(Context,metaclass=abc.ABCMeta):
    """
    implement discord.Message and Context
    """
    author:AuthorInterface
    guild:Optional[GuildInterface]
    attachments:List[AttachmentInterface]
    content:str
    
    @abc.abstractmethod
    async def send(self,*args,**kwargs):
        pass
    