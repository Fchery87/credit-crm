from datetime import date
from typing import List
from sqlalchemy import Integer, String, ForeignKey, Numeric, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base

class Invoice(Base):
    __tablename__ = "invoices"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    amount: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    due_date: Mapped[date] = mapped_column(Date, nullable=False)
    status: Mapped[str] = mapped_column(String(50), nullable=False, default="unpaid") # unpaid, paid, void

    client_id: Mapped[int] = mapped_column(Integer, ForeignKey("client_profiles.id"), nullable=False, index=True)
    client: Mapped["ClientProfile"] = relationship()

    subscription_id: Mapped[int] = mapped_column(Integer, ForeignKey("subscriptions.id"), nullable=True, index=True)
    subscription: Mapped["Subscription"] = relationship(back_populates="invoices")

    account_id: Mapped[int] = mapped_column(Integer, ForeignKey("accounts.id"), nullable=False, index=True)
    account: Mapped["Account"] = relationship(back_populates="invoices")
