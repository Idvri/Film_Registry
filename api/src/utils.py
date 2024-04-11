from rest_framework.response import Response

from src.models import Film
from src.dto import QueryDTO


def get_pagination(body: dict) -> tuple:
    """Функция для определения пагинации."""

    start = 0
    end = 25
    if 'page' in body:
        try:
            if int(body['page']) > 0:
                end *= int(body['page'])
                start = end - 25
        except TypeError:
            pass
    return start, end


def get_db_request_parameters(body: dict) -> dict | None:
    """Функция сборки полей поиска нужных данных для формирования запроса к БД."""

    req = {}
    for k, v in body.items():
        if k != 'page' and v is not None and v != 'null' and v != '':
            req[k] = v
    if len(req) > 0:
        return req
    else:
        return None


def get_data_db(request: Response) -> dict:
    """Функция для получения нужных данных из БД с пагинацией."""

    start, end = get_pagination(request.data)
    db_request = get_db_request_parameters(request.data)
    if db_request is not None:
        data = list(Film.objects.filter(**db_request)[start:end].values())
    else:
        data = list(Film.objects.all()[start:end].values())
    validated_data = QueryDTO(queryset=data).model_dump()
    return validated_data
