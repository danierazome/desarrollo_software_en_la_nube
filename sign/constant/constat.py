import os


INTERNAL_LOAD_BALANCER = os.getenv('INTERNAL_LOAD_BALANCER')
DB_URL_CONNECTION = os.getenv('DB_URL_CONNECTION')
GENERATE_TOKEN_ENDPOINT = "/api/auth-server/generar-token"
