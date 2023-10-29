from flask import request, send_file
from flask_restful import Resource
from modelos import db, VideoConversion

from io import BytesIO


class VistaVideoConversion(Resource):

    def get(self):
        conversion = VideoConversion.query.filter_by(
            id=request.json['conversion_id'], usuario_id=request.json['usuario_id']).first()

        if conversion is None:
            return {"mensaje": "Conversion no encontrada"}

        if conversion.state != "DONE":
            return {"mensaje": "Conversion se encuentra en proceso"}

        if conversion.original_format == request.json['format']:
            video_name = "".join(
                [conversion.video_name, ".", conversion.original_format])
            return send_file(BytesIO(conversion.video),
                             download_name=video_name, as_attachment=True)
        else:
            video_name = "".join(
                [conversion.video_name, ".", conversion.conversion_format])
            return send_file(BytesIO(conversion.video_converted),
                             download_name=video_name, as_attachment=True)


class VistaVideoConversions(Resource):

    def get(self):
        usuario_id = request.json['usuario_id']
        conversions = VideoConversion.query.filter_by(
            usuario_id=usuario_id).all()

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
            return {'conversions': conversion_list, }, 200
        else:
            return {'conversions': 'El usuario no tiene tareas de converión aún.'}, 200


class VistaDeleteVideoConversion(Resource):

    def delete(self):
        id = request.json['id']
        conversion = VideoConversion.query.get(id)

        if conversion is not None:
            db.session.delete(conversion)
            db.session.commit()
            return {'mensaje': 'La conversión se ha eliminado exitosamente'}
        else:
            return {'mensaje': 'No se encontró la conversión'}, 404
