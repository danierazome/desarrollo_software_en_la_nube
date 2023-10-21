from flask import request, send_file
from flask_restful import Resource

import requests
from io import BytesIO

import os

AUTH_HOST = os.getenv('AUTH_HOST')
MANAGE_CONVERSION_HOST = os.getenv('MANAGE_CONVERSION_HOST')


class VistaManageConversion(Resource):
    def get(self):
        validar_token = requests.post(
            url=f'http://{AUTH_HOST}:5000/api/validar-token',
            headers={"Authorization": request.headers['Authorization']})

        if validar_token.status_code != 200:
            return validar_token.json(), validar_token.status_code

        request.json['usuario_id'] = validar_token.json()['usuario_id']

        response_service = requests.get(
            url=f'http://{MANAGE_CONVERSION_HOST}:5000/api/video',
            json=request.json)

        file_name = response_service.headers.get(
            'Content-Disposition').split("filename=")[1]

        if response_service.status_code == 200:
            return send_file(BytesIO(response_service.content),
                             download_name=file_name, as_attachment=True)
        else:
            return response_service.json(), response_service.status_code
