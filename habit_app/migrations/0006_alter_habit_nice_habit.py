# Generated by Django 4.2.10 on 2024-02-18 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit_app', '0005_alter_habit_nice_habit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='nice_habit',
            field=models.BooleanField(default=True, verbose_name='Признак приятной привычки'),
        ),
    ]
