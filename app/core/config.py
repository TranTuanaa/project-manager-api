from os import getenv

SECRET_KEY = getenv("SECRET_KEY", "local-dev-secret-key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
