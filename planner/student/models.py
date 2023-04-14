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
    total_time = models.DurationField('Полетное время', default='0')
    instrument_time = models.DurationField('Приборное время', default='0')
    night_time = models.DurationField('Ночное время', default='0')
    copilot_time = models.DurationField('Время ВП', default='0')
    solo_time = models.DurationField('Время самостоятельно', default='0')
    PIC_time = models.DurationField('Время КВС', default='0')
    PIC_time_enroute = models.DurationField('Время КВС по маршруту', default='0')
    PIC_night_time = models.DurationField('Время КВС ночью', default='0')
    description = models.TextField('Описание упражнения', default='')
    exercise_type = models.ForeignKey('student.exercise_type', on_delete=models.CASCADE,
                                      related_name='from_exercise_type_set',
                                      verbose_name='Тип упражнения', default=1)
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
    ground_time = models.DurationField('Время наземной подготвки', default='0')

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



