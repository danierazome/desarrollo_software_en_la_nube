from flask import Flask
from flask_restful import Api
from flask_coney import Coney

from convert_video import Video

from constant import DB_URL_CONNECTION, BROKER_URL_CONNECTION

from modelos import db

# ----------> FLASK APP
app = Flask(__name__)


app.config["CONEY_BROKER_URI"] = BROKER_URL_CONNECTION
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL_CONNECTION
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

db.init_app(app)
app.app_context().push()

api = Api(app)

# -------> MESSAGE BROKER
coney = Coney(app)

video = Video(app)


@coney.queue(queue_name="convert-video")
def process_queue(ch, method, props, body):
    log_message = body.decode('utf-8')
    print(log_message)
    video.convert_video(log_message)
