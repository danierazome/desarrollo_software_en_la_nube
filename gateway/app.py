from flask import Flask
from flask_restful import Api

from vistas import VistaSignup
from vistas import VistaLogin
from vistas import VistaInitVideoConversion
from vistas import VistaManageConversion
from vistas import VistaListTasks
from vistas import VistaDeleteTask

# ----------> FLASK APP
app = Flask(__name__)

app.config['PROPAGATE_EXCEPTIONS'] = True

api = Api(app)
api.add_resource(VistaSignup, '/api/signup')
api.add_resource(VistaLogin, '/api/login')
api.add_resource(VistaInitVideoConversion, '/api/upload-video')
api.add_resource(VistaManageConversion, '/api/video')
api.add_resource(VistaListTasks, '/api/list-user-tasks')
api.add_resource(VistaDeleteTask, '/api/delete-task')
