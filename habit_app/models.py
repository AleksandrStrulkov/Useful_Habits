from django.conf import settings
from django.db import models
from django.db import connection
from django.contrib.auth import get_user_model

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    PERIOD = (
            ('Ежедневно', 'Ежедневно'),
            ('Еженедельно', 'Еженедельно',),

    )

    owner = models.ForeignKey(get_user_model(), verbose_name='Пользователь', related_name='habit',
                              on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    place = models.CharField(max_length=200, verbose_name='Место выполнения')
    time_when_execute = models.TimeField(verbose_name='Время когда выполнять')
    good_habit = models.CharField(max_length=200, verbose_name='Действие',)
    nice_habit = models.CharField(max_length=200, verbose_name='Признак приятной привычки')
    related_habit = models.CharField(max_length=200, verbose_name='Связанная привычка')
    periodicity = models.CharField(max_length=200, verbose_name='Периодичность', default='Ежедневно')
    reward = models.CharField(max_length=200, verbose_name='Вознаграждение')
    lead_time = models.TimeField(verbose_name='Время на выполнение')
    is_public = models.BooleanField(verbose_name='Признак публичности')


