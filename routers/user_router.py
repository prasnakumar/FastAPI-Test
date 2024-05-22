from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas
from app.database import SessionLocal
from app.services import user_service

router = APIRouter()

# Dependency to get the SQLAlchemy session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/", response_model=schemas.UserDetailCreate)
async def create_user(user: schemas.UserDetailCreate, db: Session = Depends(get_db)):
    return await user_service.create_user(db=db, user=user)

@router.get("/users/{user_id}", response_model=schemas.UserDetailCreate)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = await user_service.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.get("/users/", response_model=list[schemas.UserDetailCreate])
async def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = await user_service.get_users(db=db, skip=skip, limit=limit)
    return users