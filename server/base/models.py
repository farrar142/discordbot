from peewee import Model
from server.base.settings import mysql_db

class BaseModel(Model):
    """Base Model for MySQL"""
    class Meta:
      database=mysql_db