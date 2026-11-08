from typing import List
from models.model_user import Model_User_Regist
from pydantic import EmailStr, TypeAdapter
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

    def update_username(self , email : EmailStr , new_username :str) :
        result = self.collection.find_one_and_update({"email" : email} , {"$set" : {"username" : new_username}} , return_document=True)
        if result is not None :
            if "_id" in result :
                result["_id"] = str(result["_id"])
            return TypeAdapter(Model_User_Regist).validate_python(result)
        return None  

    def update_password(self , email :EmailStr , new_password : str) :
        result = self.collection.find_one_and_update({"email" : email}, {"$set" : {"password" : new_password}} , return_document=True)  
        if result is not None:
            if "_id" in result :
                result["_id"] = str(result["_id"])
            return TypeAdapter(Model_User_Regist).validate_python(result)
        return None    

    def find_by_email(self , email : EmailStr) :
        result = self.collection.find_one({"email" : email})
        if result is not None :
            if "_id" in result:
                result["_id"] = str(result["_id"])
            return TypeAdapter(Model_User_Regist).validate_python(result)

    def get_all(self):
        cursor = self.collection.find({})
        result = []
        for i in cursor :
            if "_id" in i :
                i["_id"] = str(i["_id"])
            result.append(i)
        return TypeAdapter(List[Model_User_Regist]).validate_python(result)
