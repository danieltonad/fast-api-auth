import hashlib

def hash_pwd(pwd: str):
    hash_object = hashlib.sha256(pwd.encode())
    return hash_object.hexdigest()