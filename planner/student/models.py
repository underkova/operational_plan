from django.db import models


class student(models.Model):
    name = models.CharField('ФИО', max_length=100)
    group = models.CharField('Группа', max_length=10)

    class Meta:
        db_table = 'student'

    def __str__(self):
        return self.name




class Meta:
    verbose_name = 'Студент'
    verbose_name_plural = 'Студенты'  # вот эта штука не работает


class group(models.Model):
    group_number = models.CharField('Номер группы', max_length=10)

    def __str__(self):
        return self.group_number

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
    ground_time = models.TimeField('Время наземной подготвки', max_length=100)
    exercise_type = models.CharField('Тип упражнения', max_length=100)
    approaches = models.PositiveIntegerField('Заходы', max_length=100)
    landings = models.PositiveIntegerField('Посадки', max_length=100)
    equivalent = models.PositiveIntegerField('Эквивалент', max_length=100)

    def __str__(self):
        return self.exercise_code




class briefing(models.Model):
    briefing_code = models.CharField('Шифр', max_length=100)
    briefing_name = models.CharField('Название', max_length=1000)
    ground_time = models.TimeField('Время наземной подготвки', max_length=100)

    def __str__(self):
        return self.briefing_code


class exercise_type(models.Model):
    exercise_type = models.CharField('Тип упражнения', max_length=100)

    def __str__(self):
        return self.exercise_type


