from flask import request
from flask_restful import Resource
from modelos import Usuario
from constant import AUTH_SERVER_ENDPOINT, GENERATE_TOKEN_ENDPOINT

import requests


class VistaLogin(Resource):
    def post(self):
        usuario = Usuario.query.filter(
            Usuario.usuario == request.json['usuario']).first()

        if usuario == None:
            return {"mensaje": "Usuario no registrado"}, 404

        if usuario.password == request.json['password']:
            response_generar_token = requests.post(
                url=f'{AUTH_SERVER_ENDPOINT}{GENERATE_TOKEN_ENDPOINT}',
                json={"user_id": usuario.id})

            return response_generar_token.json()

        return {"mensaje": "Password incorrecto"}, 400

    def get(self):
        return {"url": f'{AUTH_SERVER_ENDPOINT}{GENERATE_TOKEN_ENDPOINT}'}
