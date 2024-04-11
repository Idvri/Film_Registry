# Film Registry
Django API + Parser реестра фильмов (https://opendata.mkrf.ru/opendata/7705851331-register_movies).

## Stack:
- Python;
- Django (DRF);
- SQLAlchemy;
- Pydantic;
- AIOHTTP;
- Asyncio;
- Alembic;
- Swagger;
- Bash;
- ООП.

## Установка и запуск (Docker):
- git clone https://github.com/Idvri/Film_Registry.git - клонируем проект к себе в нужную директорию;
- docker-compose up --build - первоначальный запуск;
- docker-compose up - обычный запуск;

## Доступность (API: POST);
- http://localhost:8000/api/ | http://127.0.0.1:8000/api/;
- http://localhost:8000/api/docs/ - документация (Swagger).

## Функционал:
- Сохранение данных таблицы из реестра открытых данных Минкульта России в базу данных;
- API для доступа к базе данных;
- Поиск по данным через API (пагинация, номер удостоверения, название, режиссер и т.д., подробнее в документации);
- Docker-образ, который парсит встроенную в него таблицу и поднимает сервер с базой данных и API;
- Документация к API (выше).