from typing import List
from fastapi import Depends
from pymongo.synchronous.database import Database
from config.database import get_db
from pydantic import TypeAdapter
from models.model_category import Model_Category
from models.model_common import PyObjectId
from bson import ObjectId

class Repo_Category :
    def __init__(self , db : Database = Depends(get_db)):
        self.collection = db.get_collection("categories")

    def create_category(self , new_category : dict):
        return self.collection.insert_one(new_category)

    def find_all_categories(self):
        cursor = self.collection.find({})
        result = []
        for i in cursor :
            if "_id" in i :
                i["_id"] = str(i["_id"])
            result.append(i)
        return TypeAdapter(List[Model_Category]).validate_python(result)

    def find_by_id_Category(self , category_id : str) :
        if not ObjectId.is_valid(category_id):
            return None
        
        result = self.collection.find_one({"_id" : PyObjectId(category_id)})
        if result is not None :
            if "_id" in result:
                result["_id"] = str(result["_id"])
            return TypeAdapter(Model_Category).validate_python(result)
        return None

    def find_by_name_category(self , name : str) :
        result = self.collection.find_one({"name" : name})
        if result is not None :
            if "_id" in result :
                result["_id"] = str(result["_id"])
            return TypeAdapter(Model_Category).validate_python(result)      

    def update_category(self , id : str, new_category_name : str = None , new_category_desc : str = None):
        update_data = {}
        if new_category_name is not None :
            update_data["name"] = new_category_name
        if new_category_desc is not None:
            update_data["description"] = new_category_desc

        if not update_data :
            return None

        result = self.collection.find_one_and_update({"_id" : PyObjectId(id)} , {"$set" : update_data} , return_document=True)
        if result is not None :
            if "_id" in result :
                result["_id"] = str(result["_id"])
            return TypeAdapter(Model_Category).validate_python(result)

    def delete_category(self , id : str):
        result = self.collection.delete_one({"_id" : PyObjectId(id)})
        return result.deleted_count > 0        