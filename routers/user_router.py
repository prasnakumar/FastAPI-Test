from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app import schemas
from app.database import get_db
from app.services import user_service

router = APIRouter()

@router.post("/users/", response_model=schemas.UserDetail)
async def create_user(user: schemas.UserDetailCreate, db: AsyncSession = Depends(get_db)):
    return await user_service.create_user(db=db, user=user)

@router.get("/users/{user_id}", response_model=schemas.UserDetail)
async def read_user(user_id: int, db: AsyncSession = Depends(get_db)):
    db_user = await user_service.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.get("/users/", response_model=list[schemas.UserDetail])
async def read_users(skip: int = 0, db: AsyncSession = Depends(get_db)):
    return await user_service.get_users(db=db, skip=skip)
