from google.cloud import storage
from constant import BUCKET_NAME

video_content_types = {
    'avi': 'video/x-msvideo',
    'webm': 'video/webm',
    'mp4': 'video/mp4'
}


def save_converted_video(video):

    gcs = storage.Client()

    bucket = gcs.get_bucket(BUCKET_NAME)

    blob = bucket.blob(video.name)

    blob.upload_from_string(
        video.read(), content_type=get_content_type(video.name)
    )

    blob.make_public()

    return blob.public_url


def get_video_as_bytes(video_name):

    gcs = storage.Client()

    bucket = gcs.get_bucket(BUCKET_NAME)

    blob = bucket.blob(video_name)

    return blob.download_as_bytes()


def get_content_type(name):
    metadata = name.split('.')
    return video_content_types[metadata[1]]
