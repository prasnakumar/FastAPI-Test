from pydantic import BaseModel

class UserDetailBase(BaseModel):
    username: str
    email: str
    full_name: str

class UserDetailCreate(UserDetailBase):
    pass

class UserDetail(UserDetailBase):
    id: int

    class Config:
        orm_mode: True
