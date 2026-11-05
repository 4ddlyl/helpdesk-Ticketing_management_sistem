from models.model_user import Model_User_Regist
from pydantic import TypeAdapter
from fastapi import Depends
from typing import Any
from config.database import get_db
from pymongo.synchronous.database import Database

class Repo_Auth :
    def __init__(self , db : Database =  Depends(get_db)) :
        self.collection = db.get_collection("user")

    def regist_user(self , new_user : dict) :
        return self.collection.insert_one(new_user)

    def find_by_username(self , username : str) :
        result = self.collection.find_one({"username" : username})
        if result is not None :
            if "_id" in result :
                result["_id"] = str(result["_id"])
            return TypeAdapter(Model_User_Regist).validate_python(result)
        return None                    

