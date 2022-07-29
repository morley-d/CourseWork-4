from flask import request
from flask_restx import Namespace, Resource

from project.container import auth_service, user_service

auth_ns = Namespace("auth", description="Routes for Authorization and Authentication")


"""Роуты для авторизации"""
@auth_ns.route('/login/')
class AuthsView(Resource):
    def post(self):
        """Авторизация по email и паролю"""
        data = request.json
        email = data.get("email", None)
        password = data.get("password", None)
        if None in [email, password]:
            return "Не задан email или пароль", 401
        tokens = auth_service.generate_tokens(email, password)
        return tokens, 201

    def put(self):
        """Авторизация по refresh_token"""
        data = request.json
        ref_token = data.get("refresh_token")
        if not ref_token:
            return "Не задан токен", 401
        tokens = auth_service.approve_refresh_token(ref_token)
        return tokens, 201


"""Роуты для регистрации"""
@auth_ns.route('/register/')
class AuthsView(Resource):
    def post(self):
        """Регистрация по email и паролю"""
        data = request.json
        email = data.get("email", None)
        password = data.get("password", None)
        if None in [email, password]:
            return "Не задан email или пароль", 401
        user = user_service.create(data)
        return "", 201, {"location": f"/users/{user.id}"}
