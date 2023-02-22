from django.db import models


class students(models.Model):  # проблема с отображением назавания таблицы (в конце автоматом ставит S)
    name = models. CharField('ФИО', max_length=100)
    group = models.CharField('Группа', max_length=10)  # нужно ли ссылаться на таблицу groups через столбик group_id?


def _str_(self):
    return self.name


class Meta:
    verbose_name = 'Студент'
    verbose_name_plural = 'Студенты'  # вот эта штука не работает


class groups(models.Model):
    group_number = models.CharField('Номер группы', max_length=10)


from django.db import models

