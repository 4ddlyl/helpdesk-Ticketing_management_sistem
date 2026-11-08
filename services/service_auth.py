from models.model_user import Model_User_Regist
from role.role_enum import UserRole
from utils.token_blacklist import add_to_blacklist
from utils.jwt_token import access_data_token
from utils.hashing import HashHelper
from fastapi import HTTPException
from dto.dto_user import dto_user_login, dto_user_regist 
from dto.dto_user_response import dto_user_response
from dto.dto_user_admin_and_aggent import dto_createstaff
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
        user_dict['role'] = UserRole.CUSTOMER.value
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

    def update_username(self , email : str , new_username : str) :
        check_user = self.repo.find_by_username(new_username)
        if check_user :
            raise HTTPException(400 , "username sudah digunakan")
        updated_user = self.repo.update_username(email , new_username)
        if not updated_user :
            raise HTTPException(404 , "Not found")
        return {
            "message" : f"berhasil mengubah menjadi {new_username} "
        }

    def update_password(self , new_password , old_pasword , current_user) :
        #cek pw lama
        if not HashHelper.verifikasi_password(old_pasword , current_user.password) :
            raise HTTPException(401 , "password lama salah")

        #hashing
        new_hash = HashHelper.hash_password(new_password)

        self.repo.update_password(current_user.email , new_hash)
        return {
            "message" : "berhasil"
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

    def get_user_profil(self , email : str) :
        user = self.repo.find_by_email(email)
        if not user :
            raise HTTPException(404, "Not found")

        return dto_user_response.model_validate(user)

    def create_staff(self , new_user : dto_createstaff) :
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
     
                    