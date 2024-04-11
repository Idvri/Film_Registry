from django.http import JsonResponse
from drf_spectacular.utils import extend_schema, OpenApiExample

from rest_framework.response import Response
from rest_framework.views import APIView

from src.utils import get_data_db
from src.dto import QueryDTO, APIRequestDTO


# Create your views here.
@extend_schema(tags=['API'])
class FilmRegisterAPIView(APIView):
    """Эндпойнт для поиска и получения данных из БД."""

    @extend_schema(
        summary='Получение реестра.',
        request=APIRequestDTO,
        responses=QueryDTO,
    )
    def post(self, request: Response) -> JsonResponse:
        data = get_data_db(request)
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})
