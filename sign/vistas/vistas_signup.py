from flask import request
from flask_restful import Resource
from modelos import db, Usuario


class VistaSignup(Resource):
    def post(self):

        usuario = Usuario.query.filter(
            Usuario.usuario == request.json['usuario']).first()

        if usuario is not None:
            return {"mensaje": "Usuario ya se encuentra registrado"}, 400

        usuario = Usuario.query.filter(
            Usuario.email == request.json['email']).first()

        if usuario is not None:
            return {"mensaje": "Email ya se encuentra registrado"}, 400

        nuevo_usuario = Usuario(
            usuario=request.json["usuario"],
            password=request.json["password"],
            email=request.json["email"]
        )

        db.session.add(nuevo_usuario)
        db.session.commit()

        return {"mensaje": "Usuario creado exitosamente"}
