from utils.hashing import HashHelper
from fastapi import HTTPException
from dto.dto_user import dto_user_regist
from fastapi import Depends
from repositories.repo_auth import Repo_Auth

class ServiceAuth :
    def __init__(self , repo = Depends(Repo_Auth)) :
        self.repo = repo

    def regist_user(self , new_user : dto_user_regist ) :
        user_dict = new_user.dict()
        check_user = self.repo.find_by_username(user_dict['username'])

        if check_user is not None:
            raise HTTPException(400 , "user already exist")

        plain_password = user_dict['password']
        #hashing
        password_terenkripsi = HashHelper.hash_password(plain_password)
        user_dict['password'] = password_terenkripsi
        db = self.repo.regist_user(user_dict)
        return {
            "message" : "berhasil",
            "id" : str(db.inserted_id)
        }    