from django.urls import path

from src.apps import SrcConfig
from src.views import FilmRegisterAPIView

app_name = SrcConfig.name

urlpatterns = [
    path('', FilmRegisterAPIView.as_view(), name='get_recs'),
]
