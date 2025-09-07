from fastapi import Depends
from sqlalchemy.orm import Session
from app import crud, schemas, models
from app.api import deps

from typing import Optional, Any, Dict

def get_auditer(
    action: str,
    target_id: Optional[int] = None,
    target_type: Optional[str] = None,
    changes: Optional[Dict[str, Any]] = None,
):
    def auditer(
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(deps.get_current_active_user),
    ) -> None:
        audit_log = schemas.AuditLogCreate(
            action=action,
            user_id=current_user.id,
            account_id=current_user.account_id,
            target_id=target_id,
            target_type=target_type,
            changes=changes,
        )
        crud.audit_log.create_audit_log(db, obj_in=audit_log)

    return auditer
