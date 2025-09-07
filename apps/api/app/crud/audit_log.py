from sqlalchemy.orm import Session

from app.models.audit_log import AuditLog
from app.schemas.audit_log import AuditLogCreate

def create_audit_log(db: Session, *, obj_in: AuditLogCreate) -> AuditLog:
    db_obj = AuditLog(**obj_in.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
