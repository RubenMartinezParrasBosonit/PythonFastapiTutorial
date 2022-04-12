from sqlalchemy import Column, Integer, String, ForeignKey
from .connection import base
from sqlalchemy.orm import relationship


class User(base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    name = Column(String)
    password = Column(String)

    blogs = relationship('Blog', back_populates="creator")

class Blog(base):
    __tablename__= 'blog'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))

    creator = relationship("User", back_populates="blogs")
