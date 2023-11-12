from google.cloud import storage
from constant import BUCKET_NAME

def save_video(video, uuid):

    gcs = storage.Client()

    video_name = f'{uuid}{video.filename}'

    bucket = gcs.get_bucket(BUCKET_NAME)

    blob = bucket.blob(video_name)

    blob.upload_from_string(
        video.read(), content_type=video.content_type
    )

    blob.make_public()

    return blob.public_url


def delete_video(video_name):
    gcs = storage.Client()

    bucket = gcs.get_bucket(BUCKET_NAME)

    blob = bucket.blob(video_name)

    blob.delete()
