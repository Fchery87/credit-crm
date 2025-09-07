from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps, audit
from app.core import security
from pydantic import EmailStr, BaseModel

router = APIRouter()

class PasswordResetRequest(BaseModel):
    email: EmailStr

class PasswordReset(BaseModel):
    token: str
    new_password: str

@router.post("/password-recovery/{email}", response_model=schemas.Message)
def recover_password(email: str, db: Session = Depends(deps.get_db)):
    """
    Password Recovery
    """
    user = crud.user.get_user_by_email(db, email=email)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system.",
        )
    password_reset_token = security.generate_password_reset_token(email=email)
    # In a real app, you would email this token to the user
    # For now, we will just log it to the console for testing purposes
    print(f"Password reset token for {email}: {password_reset_token}")
    return {"message": "Password recovery email sent"}

@router.post("/reset-password/", response_model=schemas.Message)
def reset_password(
    body: PasswordReset,
    db: Session = Depends(deps.get_db),
    _: None = Depends(audit.get_auditer("password_reset"))
):
    """
    Reset password
    """
    email = security.verify_password_reset_token(token=body.token)
    if not email:
        raise HTTPException(status_code=400, detail="Invalid token")
    user = crud.user.get_user_by_email(db, email=email)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system.",
        )
    elif not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")

    hashed_password = security.get_password_hash(body.new_password)
    crud.user.update_password(db, user=user, hashed_password=hashed_password)
    return {"message": "Password updated successfully"}
