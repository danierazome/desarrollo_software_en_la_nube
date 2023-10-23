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
