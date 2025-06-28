import json
import os

USERS_FILE = "users.json"

def get_salt_path(username: str) -> str:
    return f"{username}.salt"

def get_data_path(username: str) -> str:
    return f"{username}.dat"

def load_users() -> list:
    if not os.path.exists(USERS_FILE):
        return []
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def save_users(users: list):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f)

def load_salt(username: str) -> bytes | None:
    salt_file = get_salt_path(username)
    if not os.path.exists(salt_file):
        return None
    with open(salt_file, "rb") as f:
        return f.read()

def save_salt(username: str, salt: bytes):
    salt_file = get_salt_path(username)
    with open(salt_file, "wb") as f:
        f.write(salt)

def load_encrypted_data(username: str) -> bytes | None:
    data_file = get_data_path(username)
    if not os.path.exists(data_file):
        return None
    with open(data_file, "rb") as f:
        return f.read()

def save_encrypted_data(username: str, data: bytes):
    data_file = get_data_path(username)
    with open(data_file, "wb") as f:
        f.write(data)

def delete_user_files(username: str):
    salt_file = get_salt_path(username)
    data_file = get_data_path(username)
    if os.path.exists(salt_file):
        os.remove(salt_file)
    if os.path.exists(data_file):
        os.remove(data_file)