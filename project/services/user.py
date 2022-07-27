import base64
import hashlib
import hmac
from flask import current_app
from project.dao.user import UserDAO
from project.config import config


# PWD_HASH_SALT = current_app.config.get('PWD_HASH_SALT')
# PWD_HASH_ITERATIONS = current_app.config.get('PWD_HASH_ITERATIONS')

PWD_HASH_SALT = config.PWD_HASH_SALT
PWD_HASH_ITERATIONS = config.PWD_HASH_ITERATIONS


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_by_email(self, email):
        return self.dao.get_by_email(email)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        data["password"] = self.get_hash(data["password"])
        return self.dao.create(data)

    def update(self, data):
        self.dao.update(data)
        return self.dao

    def delete(self, uid):
        self.dao.delete(uid)

    def get_hash(self, password):
        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return base64.b64encode(hash_digest)

    def compare_passwords(self, password_hash, other_password):
        decoded_hash = base64.b64decode(password_hash)
        other_pass_hash = hashlib.pbkdf2_hmac(
            'sha256',
            other_password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return hmac.compare_digest(decoded_hash, other_pass_hash)
