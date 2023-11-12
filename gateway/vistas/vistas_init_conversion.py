from flask import request
from flask_restful import Resource

from constant import INTERNAL_LOAD_BALANCER, VALIDATE_TOKEN_ENDPOINT, UPLOAD_VIDEO_ENDPOINT

import requests


class VistaInitVideoConversion(Resource):
    def post(self):
        validar_token = requests.post(
            url=f'{INTERNAL_LOAD_BALANCER}{VALIDATE_TOKEN_ENDPOINT}',
            headers={"Authorization": request.headers['Authorization']})

        if validar_token.status_code != 200:
            return validar_token.json(), validar_token.status_code

        file = request.files['file']
        usuario_id = str(validar_token.json()['usuario_id'])

        response_service = requests.post(
            url=f'{INTERNAL_LOAD_BALANCER}{UPLOAD_VIDEO_ENDPOINT}/' + usuario_id,
            data=request.form,
            files={'file': (file.filename, file)})

        return response_service.json(), response_service.status_code
