import base64
import hashlib
import hmac
import jwt
from flask import current_app
from werkzeug.exceptions import MethodNotAllowed
from project.dao.base import BaseDAO
from project.config import config
from project.exceptions import InvalidToken, IncorrectPassword


# PWD_HASH_SALT = current_app.config.get('PWD_HASH_SALT')
# PWD_HASH_ITERATIONS = current_app.config.get('PWD_HASH_ITERATIONS')
PWD_HASH_SALT = config.PWD_HASH_SALT
PWD_HASH_ITERATIONS = config.PWD_HASH_ITERATIONS


class UserService:
    def __init__(self, dao: BaseDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_by_email(self, email):
        return self.dao.get_by_email(email)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        data["password"] = self.get_hash(data["password"])
        return self.dao.create_user(data)

    def update(self, data, email):
        self.dao.update_user(data, email)
        return self.dao

    def delete(self, uid):
        self.dao.delete(uid)

    def update_password(self, data: dict, email: str) -> None:
        """
        Partially update user information

        :raises MethodNotAllowed: If wrong fields passed
        "raises IncorrectPassword: If password isn't correct
        """

        # Check data is okay
        user = self.get_by_email(email)
        current_password = data.get('old_password')
        new_password = data.get('new_password')

        if None in [current_password, new_password]:
            raise MethodNotAllowed

        if not self.compare_passwords(user.password, current_password):
            raise IncorrectPassword

        # Hash password and update
        data = {
            'password': (self.get_hash(new_password))
        }
        self.dao.update_password(data, user)

    def get_hash(self, password):
        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return base64.b64encode(hash_digest)

    def get_email_from_token(self, token: str) -> str:
        """
        Get email from token

        :raise InvalidToken: if no valid token passed
        """
        try:
            data = jwt.decode(token,
                              current_app.config.get('JWT_SECRET'),
                              algorithms=[current_app.config.get('JWT_ALGO')])
            email = data.get('email')
            return email
        except Exception:
            raise InvalidToken

    def compare_passwords(self, password_hash, other_password):
        decoded_hash = base64.b64decode(password_hash)
        other_pass_hash = hashlib.pbkdf2_hmac(
            'sha256',
            other_password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return hmac.compare_digest(decoded_hash, other_pass_hash)
