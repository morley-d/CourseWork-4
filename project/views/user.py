from flask import request
from flask_restx import Resource, Namespace
from project.setup.api.models import user_api_model
from project.container import user_service
from project.decorators import auth_required
from project.exceptions import ItemNotFound

user_ns = Namespace('user', description="Routes for working with users")


@user_ns.route('/')
class UserView(Resource):
    @auth_required
    @user_ns.marshal_with(user_api_model, as_list=True, code=200, description='OK')
    def get(self):
        try:
            auth_data = request.headers['Authorization']
            token = auth_data.split("Bearer ")[-1]
            email = user_service.get_email_from_token(token)
            user = user_service.get_by_email(email)
        except ItemNotFound:
            pass
        return user

    def patch(self):
        auth_data = request.headers['Authorization']
        token = auth_data.split("Bearer ")[-1]
        email = user_service.get_email_from_token(token)
        updated_data = request.json
        user_service.update(updated_data, email)
        return "", 201


@user_ns.route('/password/')
class UserResetPassView(Resource):
    @auth_required
    def put(self):
        auth_data = request.headers['Authorization']
        token = auth_data.split("Bearer ")[-1]
        email = user_service.get_email_from_token(token)

        passwords = request.json
        user_service.update_password(passwords, email)

    def delete(self, uid):
        user_service.delete(uid)
        return "", 204
