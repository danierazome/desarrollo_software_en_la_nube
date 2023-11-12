from flask import Flask
from flask_restful import Api
from healthcheck import HealthCheck, EnvironmentDump

from modelos import db
from vistas import VistaSignup, VistaLogin
from constant import DB_URL_CONNECTION

# ----------> FLASK APP
app = Flask(__name__)

health = HealthCheck()
envdump = EnvironmentDump()

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL_CONNECTION
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True


db.init_app(app)

api = Api(app)
api.add_resource(VistaSignup, '/api/sign/signup')
api.add_resource(VistaLogin, '/api/sign/login')

app.add_url_rule("/healthcheck", "healthcheck", view_func=lambda: health.run())
app.add_url_rule("/environment", "environment",
                 view_func=lambda: envdump.run())
