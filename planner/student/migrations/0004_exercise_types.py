# Generated by Django 4.1.6 on 2023-03-12 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_exercise'),
    ]

    operations = [
        migrations.CreateModel(
            name='exercise_types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise_type', models.CharField(max_length=100, verbose_name='Тип упражнения')),
            ],
        ),
    ]
