from typing import List
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base

class Account(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)

    users: Mapped[List["User"]] = relationship(back_populates="account")
    client_profiles: Mapped[List["ClientProfile"]] = relationship(back_populates="account")
    leads: Mapped[List["Lead"]] = relationship(back_populates="account")
    dispute_cases: Mapped[List["DisputeCase"]] = relationship(back_populates="account")
    letter_templates: Mapped[List["LetterTemplate"]] = relationship(back_populates="account")
    generated_letters: Mapped[List["GeneratedLetter"]] = relationship(back_populates="account")
    tasks: Mapped[List["Task"]] = relationship(back_populates="account")
    notes: Mapped[List["Note"]] = relationship(back_populates="account")
    attachments: Mapped[List["Attachment"]] = relationship(back_populates="account")
    invoices: Mapped[List["Invoice"]] = relationship(back_populates="account")
    subscriptions: Mapped[List["Subscription"]] = relationship(back_populates="account")
    webhook_events: Mapped[List["WebhookEvent"]] = relationship(back_populates="account")
    audit_logs: Mapped[List["AuditLog"]] = relationship(back_populates="account")
