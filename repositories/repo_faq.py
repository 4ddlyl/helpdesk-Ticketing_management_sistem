from typing import List
from fastapi import Depends
from pydantic import TypeAdapter
from pymongo.synchronous.database import Database
from models.model_faq import Model_Faq
from config.database import get_db

class Repo_Faq :
    def __init__(self , db : Database = Depends(get_db)):
        self.collection = db.get_collection("faqs")

    def create_faq(self , new_faq : dict):
        return self.collection.insert_one(new_faq)

    def get_all_faqs(self):
        cursor = self.collection.find({})
        result = []
        for i in cursor:
            if "_id" in i:
                i["_id"] = str(i["_id"])
            result.append(i)
        return TypeAdapter(List[Model_Faq]).validate_python(result)            