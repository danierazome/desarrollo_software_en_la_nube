import os

AUTH_SERVER_ENDPOINT = os.getenv('AUTH_SERVER_ENDPOINT')
SIGN_ENDPOINT = os.getenv('SIGN_ENDPOINT')
MANAGE_CONVERSION_ENDPOINT = os.getenv('MANAGE_CONVERSION_ENDPOINT')

VALIDATE_TOKEN_ENDPOINT = "/api/auth-server/validar-token"
SIGNUP_ENDPOINT = "/api/sign/signup"
LOGIN_ENDPOINT = "/api/sign/login"
UPLOAD_VIDEO_ENDPOINT = "/api/man-conv/upload-video"
CONVERSION_ENDPOINT = "/api/man-conv/video"
CONVERSIONS_ENDPOINT = "/api/man-conv/tareas-conversion"
DELETE_CONVERSION_ENDPOINT = "/api/man-conv/eliminar-conversion"
