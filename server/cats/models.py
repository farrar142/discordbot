from typing import Union
from typing import List
from pydantic import BaseModel as Schema
from peewee import IntegerField,CharField,TextField,SmallIntegerField,ForeignKeyField
from discord.ext.commands.context import Context
from server.base.settings import mysql_db
from server.base.models import BaseModel

class CatSerializer(Schema):
    name:str
    hungry:int

class Cat(BaseModel):
    name = CharField()
    hungry = SmallIntegerField(default=0)
        
    def increase_hungry(self,amount=1):
        if self.hungry>= 100:
            return
        query = Cat.update(hungry=self.hungry+amount).where(Cat.id == self.id)
        query.execute() # type: ignore
        
    def decrease_hungry(self,amount=1):
        if self.hungry<= 0:
            return
        query = Cat.update(hungry=self.hungry-amount).where(Cat.id == self.id)
        query.execute() # type: ignore
        
    def rename(self,name:str):
        query = Cat.update(name=name).where(Cat.id==self.id)
        query.execute() # type: ignore
    
    @classmethod
    def get_cat_from_ctx(cls,ctx:Context):
        guild_from_ctx = ctx.guild
        if guild_from_ctx:
            return cls.cat_factory(guild_from_ctx.id)
        else:
            return cls.cat_factory(999999)
        
    @classmethod
    def get_cat_from_id(cls,id:int):
        return cls.cat_factory(id)
        
    @classmethod
    def cat_factory(cls,id:int):
        cat:Union[cls,None] = cls.get_or_none(id=id)
        if cat:
            return cat
        else:
            instance= cls.create(id=id,name='고양이')
            instance.save()
            return instance
        
        
    @classmethod
    def call_all(cls):
        cats_from_db = Cat.select()
        cats:List[Cat] = [cat for cat in cats_from_db]
        return cats
    
    @property
    def is_hungry(self):
        if self.hungry >= 10:
            return True
        else:
            return False
        
