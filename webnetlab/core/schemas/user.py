from typing import Optional

from pydantic import BaseModel, constr


class UserBase(BaseModel):
    login: Optional[constr(max_length=30)]
    email: Optional[constr(max_length=30)] = None
    is_admin: bool = False


class UserCreate(UserBase):
    login: constr(max_length=30)
    password: str


class UserUpdate(UserBase):
    pass


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    pass
