from fastapi import Depends
from pymongo.synchronous.database import Database
from config.database import get_db

class Repo_Ticket :

    def __init__(self , db : Database = Depends(get_db)):
        self.collection = db.get_collection("tickets")

    def create_ticket_repo(self , data : dict) :
        return self.collection.insert_one(data)    


