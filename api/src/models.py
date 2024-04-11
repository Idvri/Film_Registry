from datetime import date

from django.db import models


# Create your models here.
class Film(models.Model):
    """Класс для сбора данных из таблицы БД в один объект."""

    id: int = models.IntegerField(primary_key=True, verbose_name='Номер удостоверения')
    film_id: str = models.TextField(verbose_name='Название фильма', null=True, blank=True)
    date_of_registration: date = models.DateField(verbose_name='Дата регистрации удостоверения', null=True, blank=True)
    name: str = models.TextField(verbose_name='Название фильма')
    director: str = models.TextField(verbose_name='Режиссер', null=True, blank=True)
    studio: str = models.TextField(verbose_name='Студия-производитель', null=True, blank=True)
    category: str = models.TextField(verbose_name='Категория')
    film_type: str = models.TextField(verbose_name='Вид фильма')
    color: str = models.TextField(verbose_name='Цвет', null=True, blank=True)
    age: str = models.TextField(verbose_name='Возрастная категория')
    start_date: date = models.DateField(verbose_name='Дата начала показа фильма', null=True, blank=True)
    year: str = models.TextField(verbose_name='Год производства', null=True, blank=True)
    country: str = models.TextField(verbose_name='Страна производства', null=True, blank=True)

    class Meta:
        db_table = 'film'
