from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import as_declarative, declared_attr


class_registry = {}


@as_declarative(class_registry=class_registry)
class Base:
    id = Column(Integer, primary_key=True)

    @declared_attr
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"
