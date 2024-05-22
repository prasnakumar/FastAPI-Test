from sqlalchemy.orm import Session
from app import models, schemas

async def create_user(db: Session, user: schemas.UserDetailCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def get_user(db: Session, user_id: int):
    return await db.query(models.UserDetail).filter(models.User.id == user_id).first()

async def get_users(db: Session, skip: int = 0, limit: int = 10):
    return await db.query(models.UserDetail).offset(skip).limit(limit).all()
