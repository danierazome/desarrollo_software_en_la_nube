from flask import request
from flask_restful import Resource
from modelos import db, VideoConversion


class VistaVideoConversion(Resource):

    def delete(self):
        id = request.json['id']
        conversion = VideoConversion.query.get(id)

        if conversion is not None:
            db.session.delete(conversion)
            db.session.commit()
            return {'mensaje': 'La conversión se ha eliminado exitosamente'}
        else:
            return {'mensaje': 'No se encontró la conversión'}, 404