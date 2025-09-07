from sqlalchemy.orm import Session
from app.models.refresh_token import RefreshToken
import uuid
from datetime import datetime, timedelta
from app.core.config import settings

def create_refresh_token(db: Session, *, user_id: int) -> RefreshToken:
    expires_at = datetime.now(timezone.utc) + timedelta(minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES)
    db_token = RefreshToken(user_id=user_id, token=str(uuid.uuid4()), expires_at=expires_at)
    db.add(db_token)
    db.commit()
    db.refresh(db_token)
    return db_token

def get_refresh_token(db: Session, *, token: str) -> RefreshToken | None:
    return db.query(RefreshToken).filter(RefreshToken.token == token).first()

def delete_refresh_token(db: Session, *, token: str):
    db_token = db.query(RefreshToken).filter(RefreshToken.token == token).first()
    if db_token:
        db.delete(db_token)
        db.commit()
    return db_token
