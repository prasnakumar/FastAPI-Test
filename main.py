from lib2to3.pytree import Base
from fastapi import FastAPI

from database import  engine
from app.models.base import Base


from routers import user_router

app = FastAPI()

# Include the user router
app.include_router(user_router.router, prefix="/api")

# Create database tables
Base.metadata.create_all(bind=engine)
