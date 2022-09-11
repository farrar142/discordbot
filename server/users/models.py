from typing import Union
from peewee import CharField,IntegerField
from server.base.models import BaseModel

class User(BaseModel):
    id = CharField(primary_key=True)
    name = CharField()
    call = IntegerField()

    @classmethod
    def update_call(self,id:str,name:str):
        db_user:Union[User,None] = User.get_or_none(id=id)
        if db_user:
            query = User.update(call=db_user.call+1).where(User.id == id)
            query.execute()
        else:
            db_user = User.create(id=id,name=name,call=1)
            db_user.save()
