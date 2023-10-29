from flask import request
from flask_restful import Resource

import requests

import os

LOGIN_HOST = os.getenv('LOGIN_HOST')


class VistaLogin(Resource):
    def post(self):
        print(LOGIN_HOST)
        response_login = requests.post(
            url=f'http://{LOGIN_HOST}:5000/api/login',
            json=request.json)

        return response_login.json(), response_login.status_code
