from sqlalchemy import Column, Integer, String
from .base import Base

class UserDetail(Base):
    __tablename__ = 'user_details'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String, index=True)
