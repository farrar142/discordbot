from datetime import datetime
from peewee import Model,IntegerField,DateTimeField,CharField,BigIntegerField,BigAutoField
from MyBot.formatter.Formatter import Formatter
from server.base.settings import mysql_db

class BaseModel(Model):
    formatter=Formatter()
    id=BigAutoField(primary_key=True)
    created_at=DateTimeField(default=datetime.now)
    """Base Model for MySQL"""
    class Meta:
        database=mysql_db
      
    def refresh(self):
        newer_self = self.get_by_id(self.id)
        for field_name in self._meta.fields.keys(): # type: ignore
            val = getattr(newer_self, field_name)
            setattr(self, field_name, val)
        self._dirty.clear()