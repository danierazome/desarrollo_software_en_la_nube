from google.cloud import pubsub_v1
from constant import CONVER_VIDEO_TOPIC, PROJECT_ID


def publish_message(message):
    publisher = pubsub_v1.PublisherClient()
    topic_name = f'projects/{PROJECT_ID}/topics/{CONVER_VIDEO_TOPIC}'
    future = publisher.publish(
        topic_name,
        bytes(message, 'utf-8'),
        spam='conversion-video')
    future.result()
