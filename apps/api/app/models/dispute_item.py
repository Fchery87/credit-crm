from sqlalchemy import Integer, String, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base

class DisputeItem(Base):
    __tablename__ = "dispute_items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    item_type: Mapped[str] = mapped_column(String(50), nullable=False) # e.g., tradeline, collection, public_record
    status: Mapped[str] = mapped_column(String(50), nullable=False, default="pending")
    reason: Mapped[str] = mapped_column(Text, nullable=True)

    case_id: Mapped[int] = mapped_column(Integer, ForeignKey("dispute_cases.id"), nullable=False, index=True)
    case: Mapped["DisputeCase"] = relationship(back_populates="dispute_items")

    bureau_id: Mapped[int] = mapped_column(Integer, ForeignKey("credit_bureaus.id"), nullable=False, index=True)
    bureau: Mapped["CreditBureau"] = relationship()

    creditor_id: Mapped[int] = mapped_column(Integer, ForeignKey("creditors.id"), nullable=True, index=True)
    creditor: Mapped["Creditor"] = relationship()

    account_id: Mapped[int] = mapped_column(Integer, ForeignKey("accounts.id"), nullable=False, index=True)
    # This relationship is provided by the back-populates on the Account model
    # account = relationship("Account")
