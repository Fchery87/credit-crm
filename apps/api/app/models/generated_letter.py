from sqlalchemy import Integer, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base

class GeneratedLetter(Base):
    __tablename__ = "generated_letters"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    content: Mapped[str] = mapped_column(Text, nullable=False)

    case_id: Mapped[int] = mapped_column(Integer, ForeignKey("dispute_cases.id"), nullable=False, index=True)
    case: Mapped["DisputeCase"] = relationship()

    template_id: Mapped[int] = mapped_column(Integer, ForeignKey("letter_templates.id"), nullable=False, index=True)
    template: Mapped["LetterTemplate"] = relationship()

    account_id: Mapped[int] = mapped_column(Integer, ForeignKey("accounts.id"), nullable=False, index=True)
    account: Mapped["Account"] = relationship(back_populates="generated_letters")
