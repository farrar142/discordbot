from .users.models import User
from .messages.models import Message
from .base.settings import mysql_db

def create_tables():
    mysql_db.create_tables([User,Message])

create_tables()