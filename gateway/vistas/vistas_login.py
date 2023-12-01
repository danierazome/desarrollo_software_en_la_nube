from flask import request
from flask_restful import Resource
from constant import SIGN_ENDPOINT, LOGIN_ENDPOINT

import requests


class VistaLogin(Resource):
    def post(self):
        response_login = requests.post(
            url=f'{SIGN_ENDPOINT}{LOGIN_ENDPOINT}',
            json=request.json)

        return response_login.json(), response_login.status_code
