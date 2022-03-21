from passlib.context import CryptContext

#tell passlib to use bcrypt alogrithm
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(pwd: str):
    return pwd_context.hash(pwd)

def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)