import os

INTERNAL_LOAD_BALANCER = os.getenv('INTERNAL_LOAD_BALANCER')
VALIDATE_TOKEN_ENDPOINT = "/api/auth-server/validar-token"
SIGNUP_ENDPOINT = "/api/sign/signup"
LOGIN_ENDPOINT = "/api/sign/login"
UPLOAD_VIDEO_ENDPOINT = "/api/man-conv/upload-video"
CONVERSION_ENDPOINT = "/api/man-conv/video"
CONVERSIONS_ENDPOINT = "/api/man-conv/tareas-conversion"
DELETE_CONVERSION_ENDPOINT = "/api/man-conv/eliminar-conversion"
