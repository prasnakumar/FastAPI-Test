from sqlalchemy import Column, Integer, String, Numeric
from .database import Base

class Item(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Numeric(10, 2))
    tax = Column(Numeric(10, 2))
