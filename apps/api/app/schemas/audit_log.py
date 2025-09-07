from pydantic import BaseModel
from typing import Optional, Dict, Any

class AuditLogCreate(BaseModel):
    action: str
    details: Optional[str] = None
    user_id: Optional[int] = None
    target_id: Optional[int] = None
    target_type: Optional[str] = None
    changes: Optional[Dict[str, Any]] = None
    account_id: int
