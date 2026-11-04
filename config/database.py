import pymongo
from dotenv import load_workbook, load_dotenv
import os

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")

client = pymongo.MongoClient(MONGO_URL)
db = client.get_database("db_HTMS")

def get_db() :
    return db