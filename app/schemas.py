from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional, List

from pydantic.types import conint


class PostBase(BaseModel):  # Base model is a Pydantic model
    title: str
    content: str
    published: bool = True  # if user does not give defaults to true
    # no problem even if the user does not give the parameter here
    #rating: Optional[int] = None


class PostCreate(PostBase):
    pass


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

class Post(PostBase):
    id: int
    created_at = datetime
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode = True


class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
