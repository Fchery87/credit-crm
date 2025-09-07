from fastapi import APIRouter, Depends, HTTPException, status, Body
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import datetime, timezone

from app import crud, schemas
from app.api import deps, audit
from app.core import security

router = APIRouter()

@router.post("/login/access-token", response_model=schemas.Token)
def login_access_token(
    db: Session = Depends(deps.get_db), form_data: OAuth2PasswordRequestForm = Depends(),
    _: None = Depends(audit.get_auditer("user_login"))
):
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user = crud.user.get_user_by_email(db, email=form_data.username)
    if not user or not security.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password",
        )
    elif not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")

    access_token = security.create_access_token(user.id)
    refresh_token = crud.refresh_token.create_refresh_token(db, user_id=user.id)

    return {
        "access_token": access_token,
        "refresh_token": refresh_token.token,
        "token_type": "bearer",
    }

@router.post("/login/refresh", response_model=schemas.Token)
def refresh_token(
    db: Session = Depends(deps.get_db), refresh_token_str: str = Body(...)
):
    """
    OAuth2 compatible token refresh, get a new access token
    """
    refresh_token = crud.refresh_token.get_refresh_token(db, token=refresh_token_str)
    if not refresh_token:
        raise HTTPException(status_code=400, detail="Invalid refresh token")
    if refresh_token.expires_at < datetime.now(timezone.utc):
        crud.refresh_token.delete_refresh_token(db, token=refresh_token.token)
        raise HTTPException(status_code=400, detail="Refresh token expired")

    access_token = security.create_access_token(refresh_token.user_id)

    return {
        "access_token": access_token,
        "refresh_token": refresh_token.token,
        "token_type": "bearer",
    }
