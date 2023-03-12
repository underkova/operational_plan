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



