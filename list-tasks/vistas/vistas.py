from flask import request
from flask_restful import Resource
from modelos import db, VideoConversion


class VistaVideoConversion(Resource):

    def get(self):
        usuario_id = request.json['usuario_id']
        conversions = VideoConversion.query.filter_by(usuario_id=usuario_id).all()

        if conversions:
            conversion_list = []
            for conversion in conversions:
                conversion_list.append({
                    'id': conversion.id,
                    'video_name': conversion.video_name,
                    'original_format': conversion.original_format,
                    'conversion_format': conversion.conversion_format,
                    'state': conversion.state
                })
            return {'conversions': conversion_list,}, 200
        else:
            return{'conversions': 'El usuario no tiene tareas de converión aún.'}, 200