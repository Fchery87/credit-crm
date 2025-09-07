from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.db.base_class import Base

class RefreshToken(Base):
    __tablename__ = 'refresh_tokens'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    token: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'), nullable=False)
    user: Mapped["User"] = relationship("User")
    expires_at: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
