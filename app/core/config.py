from os import getenv

class Settings:
    SECRET_KEY: str = getenv("SECRET_KEY", "local-dev-secret-key")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

settings = Settings()
