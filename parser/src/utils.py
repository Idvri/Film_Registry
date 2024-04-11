import aiohttp

from sqlalchemy import insert

from .config import DATABASE_ENGINE
from .dto import FilmDTO
from .models import Film

HEADERS = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Content-Type': 'application/x-www-form-urlencoded',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/123.0.0.0 Safari/537.36'
}
URL = 'https://opendata.mkrf.ru/datatable/register_movies_6013e9b63f75a075a5cb7599/'


async def save_data_db(data: dict) -> None:
    """Функция для сохранения данных в БД."""

    dto = FilmDTO(**data)
    async with DATABASE_ENGINE.connect() as conn:
        stmt = insert(Film).values(
            film_id=dto.cardNumber,
            date_of_registration=dto.cardDate,
            name=dto.filmname,
            director=dto.director,
            studio=dto.studio,
            category=dto.category,
            film_type=dto.viewMovie,
            color=dto.color,
            age=dto.ageCategory,
            start_date=dto.startDateRent,
            year=dto.crYearOfProduction,
            country=dto.countryOfProduction,
        )
        await conn.execute(stmt)
        await conn.commit()


async def get_rec_pagination_and_count(session: aiohttp.ClientSession) -> tuple:
    """Функция для получения пагинации и кол-ва записей в таблице."""

    response = await session.post(headers=HEADERS, url=URL, data={'length': f'100'})
    data = await response.json()
    pagination = data['pages']
    count = data['recordsTotal']
    return pagination, count


async def start_parsing(session: aiohttp.ClientSession) -> None:
    """Функция для получения данных из таблицы фильмов и сохранения данных в БД."""

    pagination, _ = await get_rec_pagination_and_count(session)
    start = -100
    end = 0
    for _ in range(pagination + 1):
        start += 100
        end += 100
        response = await session.post(headers=HEADERS, url=URL, data={'start': start, 'end': end,  'length': '100'})
        content = await response.json()
        [await save_data_db(film['data']['general']) for film in content['data']]


