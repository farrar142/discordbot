from datetime import datetime

from peewee import ForeignKeyField,CharField,DateTimeField,IntegerField
from server.base.models import BaseModel
from server.users.models import User

class Attachment(BaseModel):
    user = ForeignKeyField(User)
    filename = CharField()
    url = CharField()
    
    @classmethod
    def _create(cls,user_id:int,id:int,filename:str,url:str):
        instance = cls.create(id=id,user=user_id,filename=filename,url=url)
        instance.save()
        return instance