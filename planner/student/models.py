from django.db import models
from django.urls import reverse


class student(models.Model):
    name = models.CharField('ФИО', max_length=100)
    log = models.ManyToManyField('exercise')
    group = models.ForeignKey('student.group', on_delete=models.CASCADE,
                             related_name='from_group_set',
                             verbose_name='Группа', default=1)

    class Meta:
        db_table = 'student'
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        ordering = ['name']

    def __str__(self):
        return f'{self.name}, гр.{self.group.group_number}'
    def get_absolute_url(self):
        return reverse('student:detail', kwargs={'pk': self.pk})






class group(models.Model):
    group_number = models.CharField('Номер группы', max_length=10)

    def __str__(self):
        return self.group_number

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ['group_number']

class exercise(models.Model):
    exercise_name = models.CharField('Название', max_length=10000)
    exercise_code = models.CharField('Шифр', max_length=100)
    total_time = models.TimeField('Полетное время', max_length=100)
    instrument_time = models.TimeField('Приборное время', max_length=100)
    night_time = models.TimeField('Ночное время', max_length=100)
    copilot_time = models.TimeField('Время ВП', max_length=100)
    solo_time = models.TimeField('Время самостоятельно', max_length=100)
    PIC_time = models.TimeField('Время КВС', max_length=100)
    PIC_time_enroute = models.TimeField('Время КВС по маршруту', max_length=100)
    PIC_night_time = models.TimeField('Время КВС ночью', max_length=100)
    description = models.TextField('Описание упражнения', default='')
    exercise_type = models.CharField('Тип упражнения', max_length=100)
    approaches = models.PositiveIntegerField('Заходы')
    landings = models.PositiveIntegerField('Посадки')
    equivalent = models.PositiveIntegerField('Эквивалент')

    class Meta:
        verbose_name = 'Упражнение'
        verbose_name_plural = 'Упражнения'
        ordering = ['exercise_code']
    def __str__(self):
        return self.exercise_code




class briefing(models.Model):
    briefing_code = models.CharField('Шифр', max_length=100)
    briefing_name = models.CharField('Название', max_length=1000)
    ground_time = models.TimeField('Время наземной подготвки', max_length=100)

    class Meta:
        verbose_name = 'Наземная подготовка'
        verbose_name_plural = 'Наземные подготовки'
        ordering = ['briefing_code']
    def __str__(self):
        return self.briefing_code




class exercise_type(models.Model):
    exercise_type = models.CharField('Тип упражнения', max_length=100)

    class Meta:
        verbose_name = 'Тип упражнения'
        verbose_name_plural = 'Типы упражнений'
        ordering = ['exercise_type']
    def __str__(self):
        return self.exercise_type



