from sqlalchemy.orm import Session
from app.core.security import get_password_hash
from app.models.user import User
from app.schemas.user import UserCreate

def get_user_by_email(db: Session, *, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()

def get_user_by_id(db: Session, *, user_id: int) -> User | None:
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, *, obj_in: UserCreate, account_id: int) -> User:
    db_obj = User(
        email=obj_in.email,
        hashed_password=get_password_hash(obj_in.password),
        role=obj_in.role,
        account_id=account_id,
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_password(db: Session, *, user: User, hashed_password: str):
    user.hashed_password = hashed_password
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
