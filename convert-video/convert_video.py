from modelos import db, VideoConversion, Usuario
from notifications import send_email
from gcp_storage import save_converted_video, get_video_as_bytes

import datetime
import os


class Video:

    def __init__(self, app):
        self.app = app

    def get_video_name(self, id, name, format):
        return f'{id}{name}.{format}'

    def convert_video(self, conversion_id):
        with self.app.app_context():

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
                print(str(e))

            # CLOSE AND DELETE VIDEO FILE
            formated_video.close()
            os.remove(formated_video_name)
