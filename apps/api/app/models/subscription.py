from datetime import date
from typing import List
from sqlalchemy import Integer, String, ForeignKey, Numeric, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base

class Subscription(Base):
    __tablename__ = "subscriptions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    stripe_subscription_id: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    status: Mapped[str] = mapped_column(String(50), nullable=False) # active, canceled, etc.
    plan: Mapped[str] = mapped_column(String(255), nullable=False)
    price: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    current_period_end: Mapped[date] = mapped_column(Date, nullable=False)

    client_id: Mapped[int] = mapped_column(Integer, ForeignKey("client_profiles.id"), nullable=False, index=True)
    client: Mapped["ClientProfile"] = relationship()

    account_id: Mapped[int] = mapped_column(Integer, ForeignKey("accounts.id"), nullable=False, index=True)
    account: Mapped["Account"] = relationship(back_populates="subscriptions")

    invoices: Mapped[List["Invoice"]] = relationship(back_populates="subscription")
