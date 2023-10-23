from flask import Flask
from flask_restful import Api

from modelos import db
from vistas import VistaSignup

import os


# ----------> FLASK APP
app = Flask(__name__)

DATABASE_HOST = os.getenv('DB_HOST')

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://user:password@{DATABASE_HOST}:5432/arquitectura'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True


db.init_app(app)

api = Api(app)
api.add_resource(VistaSignup, '/api/signup')
