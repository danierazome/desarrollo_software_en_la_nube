from flask import Flask
from flask_restful import Api
from healthcheck import HealthCheck, EnvironmentDump

from vistas import VistaConvertVideo

from constant import DB_URL_CONNECTION, CONVERT_VIDEO_ENDPOINT
from modelos import db

# ----------> FLASK APP
app = Flask(__name__)

health = HealthCheck()
envdump = EnvironmentDump()

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL_CONNECTION
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

db.init_app(app)
app.app_context().push()

api = Api(app)
api.add_resource(VistaConvertVideo, CONVERT_VIDEO_ENDPOINT)

app.add_url_rule("/healthcheck", "healthcheck", view_func=lambda: health.run())
app.add_url_rule("/environment", "environment",
                 view_func=lambda: envdump.run())
