from sqlalchemy import Integer, Text, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base

class Note(Base):
    __tablename__ = "notes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    content: Mapped[str] = mapped_column(Text, nullable=False)

    author_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    author: Mapped["User"] = relationship()

    # Polymorphic relationship to attach notes to different objects
    parent_id: Mapped[int] = mapped_column(Integer, nullable=False, index=True)
    parent_type: Mapped[str] = mapped_column(String(50), nullable=False, index=True)

    account_id: Mapped[int] = mapped_column(Integer, ForeignKey("accounts.id"), nullable=False, index=True)
    account: Mapped["Account"] = relationship(back_populates="notes")
