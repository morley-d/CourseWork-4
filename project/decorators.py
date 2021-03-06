import jwt
from flask import request, abort
from project.config import config

JWT_ALGO = config.JWT_ALGO
JWT_SECRET = config.JWT_SECRET

def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]
        try:
            jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGO])
        except Exception as e:
            print(f"JWT Decode Error: {e}")
            abort(401)
        return func(*args, **kwargs)
    return wrapper


def admin_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]
        role = None
        try:
            user = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGO])
            role = user.get("role", "user")
        except Exception as e:
            print(f"JWT Decode Error: {e}")
            abort(401)
        if role != "admin":
            print("Недостаточно прав доступа")
            abort(403)
        return func(*args, **kwargs)
    return wrapper
