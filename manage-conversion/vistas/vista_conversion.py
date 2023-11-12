from flask import request
from flask_restful import Resource
from modelos import db, VideoConversion
from .gcp_storage import delete_video



class VistaVideoConversion(Resource):

    def get(self):
        conversion = VideoConversion.query.filter_by(
            id=request.json['conversion_id'], usuario_id=request.json['usuario_id']).first()

        if conversion is None:
            return {"mensaje": "Conversion no encontrada"}

        if conversion.state != "DONE":
            return {"mensaje": "Conversion se encuentra en proceso"}

        return {
                    'id': conversion.id,
                    'video': conversion.video,
                    'video_name': conversion.video_name,
                    'original_format': conversion.original_format,
                    'video_converted': conversion.video_converted,
                    'conversion_format': conversion.conversion_format,
                    'state': conversion.state
                }


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
                    'video': conversion.video,
                    'video_name': conversion.video_name,
                    'original_format': conversion.original_format,
                    'video_converted': conversion.video_converted,
                    'conversion_format': conversion.conversion_format,
                    'state': conversion.state
                })
            return {'conversions': conversion_list, }
        else:
            return {'conversions': 'El usuario no tiene tareas de converión aún.'}


class VistaDeleteVideoConversion(Resource):

    def delete(self):
        id = request.json['id']
        usuario_id = request.json['usuario_id']
        
        conversion = VideoConversion.query.filter_by(
            id=id, usuario_id=usuario_id).first()

        if conversion is None:
            return {'mensaje': 'No se encontró la conversión'}, 404
        
        if conversion.state != "DONE":
            return {"mensaje": "Conversion en proceso no puede ser borrada"}

        # DELETE ORIGINAL VIDEO FILE

        video_name = self.get_video_name(
            id=conversion.id, name=conversion.video_name, format=conversion.original_format)
        delete_video(video_name=video_name)

        # DELETE CONVERTED VIDEO FILE
        converted_video_name = self.get_video_name(
            id=conversion.id, name=conversion.video_name, format=conversion.conversion_format)
        delete_video(video_name=converted_video_name)

        # DELETE ENTITY FROM DATABASE
        db.session.delete(conversion)
        db.session.commit()

        return {'mensaje': 'La conversión se ha eliminado exitosamente'}
       
    
    def get_video_name(self, id, name, format):
        return f'{id}{name}.{format}'

