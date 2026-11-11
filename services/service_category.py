from fastapi import Depends, HTTPException
from dto.dto_category import dto_category_create
from repositories.repo_category import Repo_Category

class Service_Category :
    def __init__(self , repo = Depends(Repo_Category)):
        self.repo = repo

    def create_category(self , new_Category : dto_category_create) :
        check = self.repo.find_by_name_category(new_Category.name)

        if check is not None :
            raise HTTPException(400 , "name already exist")
        
        data_dict = new_Category.model_dump()
        result = self.repo.create_category(data_dict)
        return {
            "message" : f"berhasil ditambahkan"
        }

    def find_all_categories(self):
        result = self.repo.find_all_categories()
        if result is None :
            raise HTTPException(404, "not found")
        return result

    def update_category(self , id : str, name : str , desc : str) :
        check = self.repo.find_by_name_category(name)
        if check is not None :
            raise HTTPException(400 , "name already exist")
        result = self.repo.update_category(id , name , desc)
        return {
            "message" : f"berhasil diubah : {result}"
        }

    def delete_category(self , id : str):
        return self.repo.delete_category(id)