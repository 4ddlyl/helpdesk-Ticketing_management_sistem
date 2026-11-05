import bcrypt

class HashHelper :
    @staticmethod
    def hash_password(password : str) -> str :
        password_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_pass = bcrypt.hashpw(password_bytes , salt)
        return hashed_pass.decode('utf-8')

    @staticmethod
    def verifikasi_password(plain_text : str , hash_pw : str) -> bool :
        plain_bytes = plain_text.encode('utf-8')
        plain_hash = hash_pw.encode("utf-8")
        return bcrypt.checkpw(plain_bytes , plain_hash)         
