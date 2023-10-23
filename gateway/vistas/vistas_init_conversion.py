from flask import request
from flask_restful import Resource

import requests

import os

AUTH_HOST = os.getenv('AUTH_HOST')
INIT_CONVERSION_HOST = os.getenv('INIT_CONVERSION_HOST')


class VistaInitVideoConversion(Resource):
    def post(self):
        validar_token = requests.post(
            url=f'http://{AUTH_HOST}:5000/api/validar-token',
            headers={"Authorization": request.headers['Authorization']})

        if validar_token.status_code != 200:
            return validar_token.json(), validar_token.status_code

        file = request.files['file']
        usuario_id = str(validar_token.json()['usuario_id'])

        response_service = requests.post(
            url=f'http://{INIT_CONVERSION_HOST}:5000/api/upload-video/' + usuario_id,
            data=request.form,
            files={'file': (file.filename, file)})

        return response_service.json(), response_service.status_code
