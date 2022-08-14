from pydantic import BaseModel, constr


class UserBase(BaseModel):
    login: constr(max_length=30)
    email: constr(max_length=30)
    is_admin: bool = False


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class UserInDBBase(UserBase):
    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    pass
