from flask import request
from flask_restful import Resource

import requests

import os

SIGNUP_HOST = os.getenv('SIGNUP_HOST')


class VistaSignup(Resource):
    def post(self):
        response_login = requests.post(
            url=f'http://{SIGNUP_HOST}:5000/api/signup',
            json=request.json)

        return response_login.json(), response_login.status_code
