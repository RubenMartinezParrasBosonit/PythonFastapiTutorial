from typing import List, Optional

from pydantic import BaseModel

class User(BaseModel):
    email:str
    name:str
    password:str
    class Config():
        orm_mode=True

class UserUpdate(BaseModel):
    nombre:str

    class Config():
        orm_mode=True

class Respuesta(BaseModel):
    mensaje:str

class BlogBase(BaseModel):
    title: str
    body: str

class Blog(BlogBase):
    class Config():
        orm_mode=True

class ShowUser(BaseModel):
    name:str
    email:str
    blogs: List[Blog] = []
    class Config():
        orm_mode=True

class ShowUserWithoutBlog(BaseModel):
    name:str
    email:str
    class Config():
        orm_mode=True

class ShowBlog(BaseModel):
    title: str
    body: str
    creator: Optional[ShowUserWithoutBlog]
    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None