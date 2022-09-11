from peewee import MySQLDatabase,Model
import os
import logging
import dotenv

dotenv.load_dotenv()

logger = logging.getLogger("peewee")
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

DB_USER=os.getenv("DB_USER","")
DB_PASSWORD=os.getenv("DB_PASSWORD","")
DB_HOST=os.getenv("DB_HOST")

mysql_db = MySQLDatabase(
  'discord',user=DB_USER,password=DB_PASSWORD,host=DB_HOST,port=3306
)
mysql_db.connect()