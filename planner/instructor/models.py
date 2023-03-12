
from django.db import models

class instructor (models.Model):
    instructor_name = models.CharField('ФИО', max_length=100)
    instructor_login = models.CharField('Логин', max_length=100)
    instructor_password = models.CharField('Пароль', max_length=100)
    instructor_flight_time = models.TimeField('Полетное время', max_length=100)
    aircraft_type = models.CharField('Тип ВС', max_length=10)
    instructor_type = models.CharField('Должность', max_length=30)
# Create your models here.

class instructor_type (models.Model):
    instructor_type = models.CharField('Должность', max_length=30)
# Create your models here.
class aircraft_type (models.Model):
    aircraft_type = models.CharField('Тип ВС', max_length=10)
