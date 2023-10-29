from flask import Flask
from flask_restful import Api

from modelos import db

from vistas import VistaInitVideoConversion, VistaVideoConversion, VistaVideoConversions, VistaDeleteVideoConversion

import os

# ----------> FLASK APP
app = Flask(__name__)

DATABASE_HOST = os.getenv('DB_HOST')
print(f'DATABASE ADDRESS {DATABASE_HOST}')

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://user:password@{DATABASE_HOST}:5432/arquitectura'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True


db.init_app(app)

api = Api(app)
api.add_resource(VistaInitVideoConversion,
                 '/api/upload-video/<int:usuario_id>')

api.add_resource(VistaVideoConversion,
                 '/api/video')

api.add_resource(VistaVideoConversions,
                 '/api/tareas-conversion')

api.add_resource(VistaDeleteVideoConversion,
                 '/api/eliminar-conversion')
