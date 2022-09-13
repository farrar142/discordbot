from datetime import datetime
from peewee import DateTimeField,TextField,ForeignKeyField
from server.base.models import BaseModel
from server.users.models import User
from server.cats.models import Cat

class History(BaseModel):
    cat = ForeignKeyField(Cat)
    user = ForeignKeyField(User)
    text = TextField()
    created_at = DateTimeField()
    
    @classmethod
    def create(cls,guild_id:int,user_id:int,text:str):
        instance = super().create(cat=guild_id,user=user_id,text=text)
        instance.save()
        