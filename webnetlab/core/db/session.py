from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.settings import settings


engine = create_engine(settings.database_uri,
                       connect_args={"check_same_thread": False},
                       )
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
