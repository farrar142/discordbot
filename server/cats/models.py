from typing import List
from pydantic import BaseModel as Schema
from peewee import IntegerField,CharField,TextField,SmallIntegerField
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
    
    @classmethod
    def get_default_cat(cls):
        cats =  Cat.select()
        if cats.exists(mysql_db):
            cat:Cat = cats[0]
            return cat
        else:
            instance = Cat.create(name="방울이")
            instance.save()
            return instance
        
    @classmethod
    def call_all(cls):
        cats_from_db = Cat.select()
        if not cats_from_db.exists(mysql_db):
            cat = Cat.get_default_cat()
            return [cat]
        else:
            cats:List[Cat] = [cat for cat in cats_from_db]
            return cats
    
    @property
    def is_hungry(self):
        if self.hungry >= 10:
            return True
        else:
            return False
        
