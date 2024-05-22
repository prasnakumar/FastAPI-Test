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
def create_user(user: schemas.UserDetailCreate, db: Session = Depends(get_db)):
    try:
        return user_service.create_user(db=db, user=user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/users/", response_model=list[schemas.UserDetail])
def read_users(db: Session = Depends(get_db)):
    try:
        return user_service.get_users(db=db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
