from pydantic import BaseSettings


class Settings(BaseSettings):
    path_to_lab_files: str = "/home/gregory/test-lab-files"


settings = Settings()
