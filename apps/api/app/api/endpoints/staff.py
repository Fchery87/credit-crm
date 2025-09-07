from fastapi import APIRouter, Depends
from app import models
from app.api import deps
from app.schemas.user import UserRole

router = APIRouter()

@router.get("/staff-only")
def staff_only_endpoint(
    current_user: models.User = Depends(deps.rbac_enforcer([UserRole.STAFF, UserRole.OWNER]))
):
    return {"message": "Welcome, staff member!"}
