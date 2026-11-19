from typing import List

from fastapi import Depends
from pydantic import TypeAdapter
from pymongo.synchronous.database import Database
from models.model_common import PyObjectId
from models.model_message import Model_Message
from config.database import get_db

class Repo_Message_Ticket:
    def __init__(self , db : Database = Depends(get_db)):
        self.collection = db.get_collection("ticket_messages")

    def kirim_message(self, new_message : dict):
        result = self.collection.insert_one(new_message)
        return str(result.inserted_id)

    def find_chat_every_ticket(self, ticket_id : str):
        result = self.collection.find({"ticket_id" : ticket_id})
        result.sort("created_at",1)
        wrapper = [] 
        for i in result:
            if "_id" in i:
                i["_id"] = str(i["_id"])
            wrapper.append(i)
        return TypeAdapter(List[Model_Message]).validate_python(wrapper)         