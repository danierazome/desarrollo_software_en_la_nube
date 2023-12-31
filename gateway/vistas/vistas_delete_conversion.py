from flask import request
from flask_restful import Resource
from constant import MANAGE_CONVERSION_ENDPOINT, AUTH_SERVER_ENDPOINT, VALIDATE_TOKEN_ENDPOINT, DELETE_CONVERSION_ENDPOINT

import requests


class VistaDeleteTask(Resource):
    def post(self):
        validar_token = requests.post(
            url=f'{AUTH_SERVER_ENDPOINT}{VALIDATE_TOKEN_ENDPOINT}',
            headers={"Authorization": request.headers['Authorization']})

        if validar_token.status_code != 200:
            return validar_token.json(), validar_token.status_code

        request.json['usuario_id'] = validar_token.json()['usuario_id']

        response_service = requests.post(
            url=f'{MANAGE_CONVERSION_ENDPOINT}{DELETE_CONVERSION_ENDPOINT}',
            json=request.json)

        return response_service.json(), response_service.status_code
