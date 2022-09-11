from typing import Union
from peewee import CharField,IntegerField
from server.base.models import BaseModel

class User(BaseModel):
    name = CharField()
    call = IntegerField()

    @classmethod
    def update_call(cls,id:int,name:str):
        db_user:Union[User,None] = User.get_or_none(id=id)
        if db_user:
            query = User.update(call=db_user.call+1).where(User.id == id)
            query.execute()  # type: ignore
            return db_user
        else:
            db_user = User.create(id=id,name=name,call=1)
            db_user.save()
            return db_user
