from typing import List

from fastapi import Depends
from pydantic import TypeAdapter
from pymongo.synchronous.database import Database
from models.model_common import PyObjectId
from models.model_ticket import Model_Ticket
from config.database import get_db

class Repo_Ticket :

    def __init__(self , db : Database = Depends(get_db)):
        self.collection = db.get_collection("tickets")
         

    def create_ticket_repo(self , data : dict) :
        return self.collection.insert_one(data) 

    def find_ticket_by_id(self , ticket_id : str):
        result = self.collection.find_one({"_id" : PyObjectId(ticket_id)})
        if result is not None:
            if "_id" in result :
                result["_id"] = str(result["_id"])
            return TypeAdapter(Model_Ticket).validate_python(result)

    def get_all_ticket(self) :
        result = self.collection.find({})
        cursor = []
        for i in result :
            if "_id" in i :
                i["_id"] = str(i["_id"])
            cursor.append(i)
        return TypeAdapter(List[Model_Ticket]).validate_python(result)          


