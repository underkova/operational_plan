# Generated by Django 4.1.6 on 2023-03-12 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_exercise_types'),
    ]

    operations = [
        migrations.CreateModel(
            name='briefing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('briefing_code', models.CharField(max_length=100, verbose_name='Шифр')),
                ('briefing_name', models.CharField(max_length=100, verbose_name='Название')),
                ('ground_time', models.TimeField(max_length=100, verbose_name='Время наземной подготвки')),
            ],
        ),
        migrations.AlterField(
            model_name='exercise',
            name='equivalent',
            field=models.PositiveIntegerField(max_length=100, verbose_name='Эквивалент'),
        ),
    ]
