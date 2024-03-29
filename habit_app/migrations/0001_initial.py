# Generated by Django 4.2.10 on 2024-02-11 09:54

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Название привычки')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('place', models.CharField(blank=True, max_length=100, null=True, verbose_name='Место выполнения')),
                ('time_when_execute', models.TimeField(verbose_name='Время когда выполнять')),
                ('action', models.CharField(blank=True, max_length=150, null=True, verbose_name='Действие')),
                ('nice_habit', models.BooleanField(default=True, verbose_name='Признак приятной привычки')),
                ('periodicity', models.CharField(choices=[('Каждый час', 'Каждый час'), ('Каждые три часа', 'Каждые три часа'), ('Ежедневно', 'Ежедневно'), ('Раз в три дня', 'Раз в три дня'), ('Еженедельно', 'Еженедельно')], default='Ежедневно', max_length=30, verbose_name='Периодичность')),
                ('reward', models.CharField(blank=True, max_length=50, null=True, verbose_name='Вознаграждение')),
                ('lead_time', models.DurationField(default=datetime.timedelta(seconds=120), verbose_name='Время на выполнение')),
                ('is_public', models.BooleanField(default=True, verbose_name='Признак публичности')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='habit', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('related_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='habit_app.habit', verbose_name='Связанная привычка')),
            ],
            options={
                'verbose_name': 'Привычка',
                'verbose_name_plural': 'Привычки',
                'get_latest_by': 'date',
            },
        ),
    ]
