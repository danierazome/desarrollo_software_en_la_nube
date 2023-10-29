from flask import request
from flask_restful import Resource

import requests

import os

SIGN_HOST = os.getenv('SIGN_HOST')


class VistaLogin(Resource):
    def post(self):
        print(SIGN_HOST)
        response_login = requests.post(
            url=f'http://{SIGN_HOST}:5000/api/login',
            json=request.json)

        return response_login.json(), response_login.status_code
