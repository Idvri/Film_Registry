from typing import Optional
from datetime import date, datetime
from pydantic import BaseModel, field_validator


class FilmDTO(BaseModel):
    """Класс для валидации данных из таблицы."""

    cardNumber: str
    cardDate: Optional[date] = None
    filmname: str
    director: Optional[str] = None
    studio: Optional[str] = None
    category: str
    viewMovie: str
    color: Optional[str] = None
    ageCategory: str
    startDateRent: Optional[date] = None
    crYearOfProduction: Optional[str] = None
    countryOfProduction: Optional[str] = None

    @field_validator('cardDate', 'startDateRent', mode='before')
    @classmethod
    def datetime_to_date(cls, value: str | None) -> date | None:
        """Функция для преобразования даты со временем в просто дату."""

        if value is not None:
            return datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%fZ").date()
        return None
