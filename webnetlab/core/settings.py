from pydantic import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseSettings):
    path_to_lab_files: str = os.getenv("WEBNETLAB_PATH_TO_LABFILES")
    lab_spec_filename: str = os.getenv("WEBNETLAB_LAB_SPEC_FILENAME")

    server_ip: str = os.getenv("WEBNETLAB_SERVER_IP")
    server_port: int = os.getenv("WEBNETLAB_SERVER_PORT")
    worker_count: int = os.getenv("WEBNETLAB_SERVER_WORKERS")
    reload_app_on_change: bool = os.getenv("WEBNETLAB_SERVER_RELOAD")

    database_uri: str = os.getenv("WEBNETLAB_SQLALCHEMY_DATABASE_URI")


settings = Settings()
