from flask import request
from flask_restful import Resource
import requests
import os

AUTH_HOST = os.getenv('AUTH_HOST')
LIST_TASKS_HOST = os.getenv('LIST_TASKS_HOST')

class VistaListTasks(Resource):
    def get(self):
        user_data = {}
        validar_token = requests.post(
            url=f'http://{AUTH_HOST}:5000/api/validar-token',
            headers={"Authorization": request.headers['Authorization']})
        
        if validar_token.status_code != 200:
            return validar_token.json(), validar_token.status_code
        user_data['usuario_id'] = validar_token.json()['usuario_id']
        response_service = requests.get(
            url=f'http://{LIST_TASKS_HOST}:5000/api/tareas-conversion',
            json=user_data)

        return response_service.json(), response_service.status_code