from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app import models, schemas

async def create_user(db: AsyncSession, user: schemas.UserDetailCreate):
    db_user = models.UserDetail(**user.dict())
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def get_user(db: AsyncSession, user_id: int):
    result = await db.execute(select(models.UserDetail).filter(models.UserDetail.id == user_id))
    return result.scalars().first()

async def get_users(db: AsyncSession, skip: int = 0):
    result = await db.execute(select(models.UserDetail).offset(skip))
    return result.scalars().all()
