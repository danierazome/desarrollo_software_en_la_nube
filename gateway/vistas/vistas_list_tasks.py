from flask import request
from flask_restful import Resource
from constant import INTERNAL_LOAD_BALANCER, VALIDATE_TOKEN_ENDPOINT, CONVERSIONS_ENDPOINT

import requests


class VistaListTasks(Resource):
    def get(self):
        user_data = {}
        validar_token = requests.post(
            url=f'{INTERNAL_LOAD_BALANCER}{VALIDATE_TOKEN_ENDPOINT}',
            headers={"Authorization": request.headers['Authorization']})

        if validar_token.status_code != 200:
            return validar_token.json(), validar_token.status_code

        user_data['usuario_id'] = validar_token.json()['usuario_id']

        response_service = requests.get(
            url=f'{INTERNAL_LOAD_BALANCER}{CONVERSIONS_ENDPOINT}',
            json=user_data)

        return response_service.json(), response_service.status_code
