from flask import Flask
from flask_restful import Api
from flask_coney import Coney

from convert_video import Video

from modelos import db

import os

DB_HOST = os.getenv('DB_HOST')
BROKER_HOST = os.getenv('BROKER_HOST')


# ----------> FLASK APP
app = Flask(__name__)


app.config["CONEY_BROKER_URI"] = f'amqp://guest:guest@{BROKER_HOST}:5672'
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://user:password@{DB_HOST}:5432/arquitectura'
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
