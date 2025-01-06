from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .db import Base, int_pk


class User(Base):
    id: Mapped[int_pk]
    username: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(50), unique=True)
    password: Mapped[str] = mapped_column(String(50))

    def __str__(self):
        return f"User -> {self.username}"
