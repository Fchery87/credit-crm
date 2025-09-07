from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, func, Boolean
from sqlalchemy.orm import as_declarative, declared_attr, Mapped, mapped_column

@as_declarative()
class Base:
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)
    deleted_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    version: Mapped[int] = mapped_column(Integer, nullable=False, default=1)

    __mapper_args__ = {
        "version_id_col": version
    }

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + "s"

    def delete(self):
        self.deleted_at = func.now()

    def undelete(self):
        self.deleted_at = None

    @property
    def is_deleted(self) -> bool:
        return self.deleted_at is not None
