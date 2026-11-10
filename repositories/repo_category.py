from fastapi import Depends
from pymongo.synchronous.database import Database
from config.database import get_db

class Repo_Category :
    def __init__(self , db : Database = Depends(get_db)):
        self.repo = db.get_collection("categories")