from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from healthcheck import HealthCheck, EnvironmentDump
from constant import GENERATE_TOKEN_ENDPOINT, VALIDATE_TOKEN_ENDPOINT

from vistas import VistaGenerar, VistaValidar

# ----------> FLASK APP
app = Flask(__name__)

health = HealthCheck()
envdump = EnvironmentDump()

app.config['JWT_SECRET_KEY'] = 'frase-secreta'
app.config['PROPAGATE_EXCEPTIONS'] = True


api = Api(app)
api.add_resource(VistaGenerar, GENERATE_TOKEN_ENDPOINT)
api.add_resource(VistaValidar, VALIDATE_TOKEN_ENDPOINT)


app.add_url_rule("/healthcheck", "healthcheck", view_func=lambda: health.run())
app.add_url_rule("/environment", "environment",
                 view_func=lambda: envdump.run())

jwt = JWTManager(app)
