from sqlalchemy import Column, String, Boolean

from core.db.declarative_base import Base


class User(Base):
    login = Column(String(30), nullable=False)
    email = Column(String(50), index=True, nullable=True)
    is_admin = Column(Boolean, default=False)
    hashed_password = Column(String, nullable=False)
