from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base

class Attachment(Base):
    __tablename__ = "attachments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    file_name: Mapped[str] = mapped_column(String(255), nullable=False)
    file_path: Mapped[str] = mapped_column(String(1024), nullable=False)
    file_type: Mapped[str] = mapped_column(String(255), nullable=True)

    # Polymorphic relationship to attach files to different objects
    parent_id: Mapped[int] = mapped_column(Integer, nullable=False, index=True)
    parent_type: Mapped[str] = mapped_column(String(50), nullable=False, index=True)

    account_id: Mapped[int] = mapped_column(Integer, ForeignKey("accounts.id"), nullable=False, index=True)
    account: Mapped["Account"] = relationship(back_populates="attachments")
