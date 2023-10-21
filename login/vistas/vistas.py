from flask import request
from flask_restful import Resource
from modelos import db, Usuario

import requests
import os

AUTH_HOST = os.getenv('AUTH_HOST')


class VistaLogin(Resource):
    def post(self):

        usuario = Usuario.query.filter(
            Usuario.usuario == request.json['usuario']).first()

        if usuario == None:
            return {"mensaje": "Usuario no registrado"}, 404

        if usuario.password == request.json['password']:
            response_generar_token = requests.post(
                url=f'http://{AUTH_HOST}:5000/api/generar-token',
                json={"user_id": usuario.id})

            return response_generar_token.json()

        return {"mensaje": "Password incorrecto"}, 400
