from typing import Union
from peewee import IntegerField,CharField
from server.base.models import BaseModel

class Guild(BaseModel):
    name = CharField()
    
    @classmethod
    def get_or_update(cls,id:int,name:str):
        db_user:Union[cls,None] = cls.get_or_none(id=id)
        if db_user:
            query = cls.update(name=db_user.name).where(cls.id == id)
            query.execute()  # type: ignore
            return db_user
        else:
            db_user = cls.create(id=id,name=name,call=1)
            db_user.save()
            return db_user