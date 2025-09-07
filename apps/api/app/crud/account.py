from sqlalchemy.orm import Session

from app.models.account import Account
from app.schemas.account import AccountCreate

def create_account(db: Session, *, obj_in: AccountCreate) -> Account:
    db_obj = Account(name=obj_in.name)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
