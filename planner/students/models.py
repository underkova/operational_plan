from django.db import models


class students(models.Model):
    name = models.CharField('ФИО', max_length=100)
    group = models.CharField('Группа', max_length=10)

    class Meta:
        db_table = 'students'

    def __str__(self):
        return self.name


class Meta:
    verbose_name = 'Студент'
    verbose_name_plural = 'Студенты'  # вот эта штука не работает


class groups(models.Model):
    group_number = models.CharField('Номер группы', max_length=10)

class exercise(models.Model):
    exercise_code = models.CharField('Шифр', max_length=100)
    exercise_name = models.CharField('Название', max_length=10000)
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


class exercise_types(models.Model):
    exercise_type = models.CharField('Тип упражнения', max_length=100)



