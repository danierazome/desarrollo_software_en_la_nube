from flask import request
from flask_restful import Resource

from modelos import db, VideoConversion, Usuario
from gcp_storage import save_converted_video, get_video_as_bytes
from notifications import send_email

import logging
import base64
import datetime
import os


class VistaConvertVideo(Resource):

    def post(self):

        data_encoded = request.json['message']['data']
        base64_bytes = data_encoded.encode('ascii')
        data_bytes = base64.b64decode(base64_bytes)
        data = data_bytes.decode('ascii')
        logging.warning(data)

        # self.convert_video(conversion_id=data)

        return

    def get_video_name(self, id, name, format):
        return f'{id}{name}.{format}'

    def convert_video(self, conversion_id):

        conversion = VideoConversion.query.filter(
            VideoConversion.id == conversion_id).first()

        usuario = Usuario.query.filter(
            Usuario.id == conversion.usuario_id).first()

        # UPDATE STATUS
        conversion.state = "IN-PROGRESS"
        db.session.commit()

        # VIDEO INFORMATION
        formated_video_name = self.get_video_name(
            id=conversion.id, name=conversion.video_name, format=conversion.conversion_format
        )
        video_name = self.get_video_name(
            id=conversion.id, name=conversion.video_name, format=conversion.original_format
        )
        # OPEN CONVERTED VIDEO
        with open(formated_video_name, "wb") as binary_file:
            binary_file.write(get_video_as_bytes(video_name=video_name))

        formated_video = open(formated_video_name, "rb")

        try:
            video_url = save_converted_video(video=formated_video)

            conversion.state = "DONE"
            conversion.video_converted = video_url
            conversion.conversion_date = datetime.datetime.now()
            db.session.commit()

            send_email(usuario=usuario, conversion=conversion)

        except Exception as e:
            logging.warning(str(e))

        # CLOSE AND DELETE VIDEO FILE
        formated_video.close()
        os.remove(formated_video_name)
