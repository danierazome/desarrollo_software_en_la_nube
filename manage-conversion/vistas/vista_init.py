from flask import request
from flask_restful import Resource

from modelos import db, VideoConversion
from .gcp_storage import save_video
from .pub_message import publish_message

import datetime
import uuid


allowed_formats = ['mp4', 'webm', 'avi']


class VistaInitVideoConversion(Resource):

    def post(self, usuario_id):

        # GET FILE'S DATA
        file = request.files['file']
        video_metadata = file.filename.split(".")

        # GET CONVERSION DATA
        conversion_format = request.form.get("conversion_format")

        # VALIDATE VIDEO METADATA
        if len(video_metadata) != 2:
            return {'mensaje': 'Nombre del video es incorrecto'}, 400

        # VALIDATE SUPPORTED VIDEO FORMATS
        if conversion_format not in allowed_formats or video_metadata[1] not in allowed_formats:
            return {'mensaje': 'Formatos nos soportados'}, 400

        if conversion_format == video_metadata[1]:
            return {'mensaje': 'Formatos iguales'}, 400

        # UPLOAD VIDEO FILE AND ENTITY ON DATABASE
        conversion_id = str(uuid.uuid4())
        date_now = datetime.datetime.now()

        # #  UPLOAD VIDEOFILE
        video_url = save_video(video=file, uuid=conversion_id)

        conversion = VideoConversion(
            id=conversion_id,
            video=video_url,
            video_name=video_metadata[0],
            original_format=video_metadata[1],
            upload_date=date_now,
            conversion_format=conversion_format,
            state="UPLOADED",
            usuario_id=usuario_id)

        db.session.add(conversion)
        db.session.commit()

        # SEND TO MESSAGE SYSTEM
        publish_message(conversion_id)

        return {"result": "Video se ha cargado exitosamente y esta en proceso"}
