
from django.db import models

class instructor (models.Model):
    instructor_name = models.CharField('ФИО', max_length=100)
    instructor_login = models.CharField('Логин', max_length=100)
    instructor_password = models.CharField('Пароль', max_length=100)
    instructor_flight_time = models.TimeField('Полетное время', max_length=100)
    aircraft_type = models.CharField('Тип ВС', max_length=10)
    instructor_type = models.CharField('Должность', max_length=30)

    def __str__(self):
        return self.instructor_name
    class Meta:

        verbose_name = 'Инструктор'
        verbose_name_plural = 'Инструктора'  # вот эта штука не работает (Потому что эта штука должна быть внутри класса, а не вне. Теперь все работает
        ordering = ['instructor_name']
# Create your models here.

class instructor_type (models.Model):
    instructor_type = models.CharField('Должность', max_length=30)

    def __str__(self):
        return self.instructor_type

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'  # вот эта штука не работает (Потому что эта штука должна быть внутри класса, а не вне. Теперь все работает
        ordering = ['instructor_type']
# Create your models here.
class aircraft_type (models.Model):
    aircraft_type = models.CharField('Тип ВС', max_length=10)

    class Meta:
        verbose_name = 'Тип ВС'
        verbose_name_plural = 'Типы ВС'  # вот эта штука не работает (Потому что эта штука должна быть внутри класса, а не вне. Теперь все работает
        ordering = ['aircraft_type']
    def __str__(self):
        return self.aircraft_type
