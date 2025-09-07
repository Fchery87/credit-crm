from typing import List
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base

class DisputeCase(Base):
    __tablename__ = "dispute_cases"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    status: Mapped[str] = mapped_column(String(50), nullable=False, default="open")

    client_id: Mapped[int] = mapped_column(Integer, ForeignKey("client_profiles.id"), nullable=False, index=True)
    client: Mapped["ClientProfile"] = relationship(back_populates="dispute_cases")

    account_id: Mapped[int] = mapped_column(Integer, ForeignKey("accounts.id"), nullable=False, index=True)
    account: Mapped["Account"] = relationship(back_populates="dispute_cases")

    dispute_items: Mapped[List["DisputeItem"]] = relationship(back_populates="case")
