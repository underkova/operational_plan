from django.db import models
from student.models import student

class instructor(models.Model):
    instructor_name = models.CharField('ФИО', max_length=100)
    instructor_login = models.CharField('Логин', max_length=100)
    instructor_password = models.CharField('Пароль', max_length=100)
    instructor_flight_time = models.DurationField('Полетное время', default='0')
    aircraft_type = models.ForeignKey('instructor.aircraft_type', on_delete=models.CASCADE,
                              related_name='from_aircraft_set',
                              verbose_name='Тип ВС', default=1)
    instructor_type = models.ForeignKey('instructor.instructor_type', on_delete=models.CASCADE,
                                      related_name='from_instructor_type_set',
                                      verbose_name='Должность', default=1)
    list = models.ManyToManyField(student, verbose_name='Список студентов', related_name='stud_list', default='1')

    def __str__(self):
        hours, minutes = divmod(self.instructor_flight_time.total_seconds() // 60, 60)
        return f"{hours}:{minutes:02}"
    class Meta:
        verbose_name = 'Инструктор'
        verbose_name_plural = 'Инструктора'
        ordering = ['instructor_name']


class instructor_type(models.Model):
    instructor_type = models.CharField('Должность', max_length=30)

    def __str__(self):
        return self.instructor_type

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
        ordering = ['instructor_type']

class aircraft_type(models.Model):
    aircraft_type = models.CharField('Тип ВС', max_length=10)

    class Meta:
        verbose_name = 'Тип ВС'
        verbose_name_plural = 'Типы ВС'
        ordering = ['aircraft_type']
    def __str__(self):
        return self.aircraft_type
