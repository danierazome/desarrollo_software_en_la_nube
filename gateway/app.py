from flask import Flask
from flask_restful import Api
from healthcheck import HealthCheck, EnvironmentDump

from vistas import VistaSignup
from vistas import VistaLogin
from vistas import VistaInitVideoConversion
from vistas import VistaManageConversion
from vistas import VistaListTasks
from vistas import VistaDeleteTask

from constant import SIGNUP_ENDPOINT, LOGIN_ENDPOINT, \
    UPLOAD_VIDEO_ENDPOINT, CONVERSION_ENDPOINT, CONVERSIONS_ENDPOINT, DELETE_CONVERSION_ENDPOINT

# ----------> FLASK APP
app = Flask(__name__)

health = HealthCheck()
envdump = EnvironmentDump()

app.config['PROPAGATE_EXCEPTIONS'] = True

api = Api(app)
api.add_resource(VistaSignup, SIGNUP_ENDPOINT)
api.add_resource(VistaLogin, LOGIN_ENDPOINT)
api.add_resource(VistaInitVideoConversion, UPLOAD_VIDEO_ENDPOINT)
api.add_resource(VistaManageConversion, CONVERSION_ENDPOINT)
api.add_resource(VistaListTasks, CONVERSIONS_ENDPOINT)
api.add_resource(VistaDeleteTask, DELETE_CONVERSION_ENDPOINT)

app.add_url_rule("/healthcheck", "healthcheck", view_func=lambda: health.run())
app.add_url_rule("/environment", "environment",
                 view_func=lambda: envdump.run())
