from flask import Flask
from flask_restful import Api
from threading import Thread
from google.cloud import pubsub_v1
from healthcheck import HealthCheck, EnvironmentDump

from convert_video import Video

from constant import DB_URL_CONNECTION, PROJECT_ID, CONVER_VIDEO_TOPIC, CONVER_VIDEO_SUBSC

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

app.add_url_rule("/healthcheck", "healthcheck", view_func=lambda: health.run())
app.add_url_rule("/environment", "environment",
                 view_func=lambda: envdump.run())

# -------> MESSAGE BROKER

topic_name = f'projects/{PROJECT_ID}/topics/{CONVER_VIDEO_TOPIC}'

subscription_name = f'projects/{PROJECT_ID}/subscriptions/{CONVER_VIDEO_SUBSC}'

video = Video(app=app)


def callback(message):
    video.convert_video(conversion_id=message.data.decode('utf-8'))
    message.ack()


def subscribe_topic():
    with pubsub_v1.SubscriberClient() as subscriber:
        future = subscriber.subscribe(
            subscription_name, callback)
        try:
            future.result()
        except KeyboardInterrupt:
            future.cancel()


t = Thread(target=subscribe_topic)
t.start()
