from sqlalchemy.orm import Session
from app.models import user_model
from app.schemas import UserDetailCreate

def create_user(db: Session, user: UserDetailCreate):
    db_user = user_model.UserDetail(username=user.username, email=user.email, full_name=user.full_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(user_model.UserDetail).all()

def get_user(db: Session, user_id: int):
    return db.query(user_model).filter(user_model.id == user_id).first()
