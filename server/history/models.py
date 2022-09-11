from datetime import datetime
from peewee import DateTimeField,TextField,ForeignKeyField
from server.base.models import BaseModel
from server.guilds.models import Guild
from server.users.models import User

class History(BaseModel):
    guild = ForeignKeyField(Guild)
    user = ForeignKeyField(User)
    text = TextField()
    created_at = DateTimeField()
    
    @classmethod
    def create(cls,guild_id:int,user_id:int,text:str):
        instance = super().create(guild=guild_id,user=user_id,text=text)
        instance.save()
        