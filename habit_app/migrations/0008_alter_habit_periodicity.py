# Generated by Django 4.2.10 on 2024-02-20 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit_app', '0007_alter_habit_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='periodicity',
            field=models.SmallIntegerField(blank=True, choices=[(1, 'Ежедневно'), (2, 'Каждые два дня'), (3, 'Каждые три дня'), (7, 'Еженедельно')], default=1, null=True, verbose_name='Периодичность'),
        ),
    ]
