import calendar
import datetime

import jwt
from flask import current_app
from project.config import config
from flask_restx import abort

from project.services.user_service import UserService

# JWT_ALGO = current_app.config.get('JWT_ALGORITHM')
# JWT_SECRET = current_app.config.get('JWT_SECRET')
JWT_ALGO = config.JWT_ALGO
JWT_SECRET = config.JWT_SECRET


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_tokens(self, email, password, is_refresh=False):
        user = self.user_service.get_by_email(email)
        if user is None:
            raise abort(404)
        if not is_refresh:
            if not self.user_service.compare_passwords(user.password, password):
                abort(400)

        data = {
            "email": user.email
        }

        # 30 minutes for access token
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGO)

        # 130 days for refresh token
        day130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(day130.timetuple())
        refresh_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGO)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }

    def approve_refresh_token(self, ref_token):
        data = jwt.decode(ref_token, JWT_SECRET, algorithms=[JWT_ALGO])
        email = data["email"]
        return self.generate_tokens(email, None, is_refresh=True)
