from pathlib import Path
from pydantic import BaseSettings


class Settings(BaseSettings):
    path_to_lab_files: Path = Path("/home/macheev/containerlab-test/")
    lab_spec_filename: str = "lab_specification.yml"


settings = Settings()
