from datetime import datetime
from peewee import Model,IntegerField,DateTimeField,CharField,BigIntegerField,BigAutoField
from MyBot.formatter.Formatter import Formatter
from server.base.settings import mysql_db

class BaseModel(Model):
    formatter=Formatter()
    id = BigAutoField(primary_key=True)
    created_at = DateTimeField(default=datetime.now)
    """Base Model for MySQL"""
    class Meta:
      database=mysql_db