from datetime import date

from sqlalchemy import Integer, Date, Text
from sqlalchemy.orm import Mapped, mapped_column

from .config import Base


class Film(Base):
    """Класс для сохранения данных из таблицы с сайта в БД."""

    __tablename__ = 'film'

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    film_id: Mapped[str] = mapped_column(Text)
    date_of_registration: Mapped[date] = mapped_column(Date, nullable=True)
    name: Mapped[str] = mapped_column(Text)
    director: Mapped[str] = mapped_column(Text, nullable=True)
    studio: Mapped[str] = mapped_column(Text, nullable=True)
    category: Mapped[str] = mapped_column(Text)
    film_type: Mapped[str] = mapped_column(Text)
    color: Mapped[str] = mapped_column(Text, nullable=True)
    age: Mapped[str] = mapped_column(Text)
    start_date: Mapped[date] = mapped_column(Date, nullable=True)
    year: Mapped[str] = mapped_column(Text, nullable=True)
    country: Mapped[str] = mapped_column(Text, nullable=True)
