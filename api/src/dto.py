from pydantic import BaseModel
from typing import Optional, List
from datetime import date


class FilmDBDTO(BaseModel):
    """Класс-тело для удостоверения из БД."""

    film_id: str
    date_of_registration: Optional[date] = None
    name: str
    director: Optional[str] = None
    studio: Optional[str] = None
    category: str
    film_type: str
    color: Optional[str] = None
    age: str
    start_date: Optional[date] = None
    year: Optional[str] = None
    country: Optional[str] = None


class APIRequestDTO(BaseModel):
    """Класс-тело для формирования запроса."""

    page: Optional[int] = 0
    film_id: Optional[str] = None
    date_of_registration: Optional[date] = None
    name: Optional[str] = None
    director: Optional[str] = None
    studio: Optional[str] = None
    category: Optional[str] = None
    film_type: Optional[str] = None
    color: Optional[str] = None
    age: Optional[str] = None
    start_date: Optional[date] = None
    year: Optional[str] = None
    country: Optional[str] = None


class QueryDTO(BaseModel):
    """Класс-тело для удостоверений из БД."""

    queryset: List[FilmDBDTO]
