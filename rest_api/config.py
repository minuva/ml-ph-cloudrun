import os

HOSTNAME = "0.0.0.0"
PORT = 9612
WORKERS = 1

SECRET_KEY = os.environ.get("SECRET_KEY")
TOKEN_PREFIX = "mnv_"
