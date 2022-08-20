from pydantic import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseSettings):
    # Containerlab files settings
    path_to_lab_files: str = os.getenv("WEBNETLAB_PATH_TO_LABFILES")
    lab_spec_filename: str = os.getenv("WEBNETLAB_LAB_SPEC_FILENAME")

    # Server settings
    server_ip: str = os.getenv("WEBNETLAB_SERVER_IP")
    server_port: int = os.getenv("WEBNETLAB_SERVER_PORT")
    worker_count: int = os.getenv("WEBNETLAB_SERVER_WORKERS")
    reload_app_on_change: bool = os.getenv("WEBNETLAB_SERVER_RELOAD")

    # Database settings
    database_uri: str = os.getenv("WEBNETLAB_SQLALCHEMY_DATABASE_URI")
    database_echo: bool = os.getenv("WEBNETLAB_DATABASE_ECHO")

    # JWT settings
    jwt_secret: str = os.getenv("WEBNETLAB_JWT_SECRET")
    jwt_algorithm: str = os.getenv("WEBNETLAB_JWT_ALGORITHM")
    jwt_token_expiry: int = os.getenv("WEBNETLAB_JWT_TOKEN_EXPIRY")


settings = Settings()
