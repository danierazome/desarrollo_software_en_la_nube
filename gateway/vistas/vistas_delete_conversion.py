from flask import request
from flask_restful import Resource
import requests
import os

AUTH_HOST = os.getenv('AUTH_HOST')
MANAGE_CONVERSION_HOST = os.getenv('MANAGE_CONVERSION_HOST')


class VistaDeleteTask(Resource):
    def delete(self):
        validar_token = requests.post(
            url=f'http://{AUTH_HOST}:5000/api/validar-token',
            headers={"Authorization": request.headers['Authorization']})

        if validar_token.status_code != 200:
            return validar_token.json(), validar_token.status_code

        response_service = requests.delete(
            url=f'http://{MANAGE_CONVERSION_HOST}:5000/api/eliminar-conversion',
            json=request.json)

        return response_service.json(), response_service.status_code
