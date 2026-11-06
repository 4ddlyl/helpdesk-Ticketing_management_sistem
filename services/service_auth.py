from utils.token_blacklist import add_to_blacklist
from utils.jwt_token import access_data_token
from utils.hashing import HashHelper
from fastapi import HTTPException
from dto.dto_user import dto_user_login, dto_user_regist
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

    def login(self, inputlogin : dto_user_login) :
        check_email = self.repo.find_by_email(inputlogin.email)
        if not check_email :
            raise HTTPException(401 , "email salah")

        password_check = HashHelper.verifikasi_password(inputlogin.password , check_email.password)
        if not password_check :
            raise HTTPException(401 , "email atau password salah")

        token = access_data_token(data={"sub" : check_email.email})
        return {
            "access token" : token,
            "token type" : "bareer"
        }

    def logout(self , token:str):
        add_to_blacklist(token)
        return {"message" : "berhasil logout"}    

    def get_all_user(self) :
        result = self.repo.get_all()
        if result is None :
            raise HTTPException(404 , "not found")
        return {
            "data" : result
        } 

                        