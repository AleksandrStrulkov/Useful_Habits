from datetime import timedelta
from django.db import models
from django.contrib.auth import get_user_model

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    NAME = (
        ('Полезная', 'Полезная'),
        ('Приятная', 'Приятная')
    )

    class Period(models.IntegerChoices):
        DAILY = 1, 'Ежедневно'
        IN_ONE_DAY = 2, 'Каждые два дня'
        EVERY_THREE_DAYS = 3, 'Каждые три дня'
        WEEKLY = 7, 'Еженедельно'

    owner = models.ForeignKey(get_user_model(), verbose_name='Пользователь', related_name='habit',
                              on_delete=models.CASCADE, **NULLABLE)
    name = models.CharField(max_length=100, verbose_name='Название привычки', choices=NAME, **NULLABLE)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', **NULLABLE)
    place = models.CharField(max_length=100, verbose_name='Место выполнения', **NULLABLE)
    time_when_execute = models.TimeField(verbose_name='Время когда выполнять')
    action = models.CharField(max_length=150, verbose_name='Действие', **NULLABLE)
    nice_habit = models.BooleanField(default=True, verbose_name='Признак приятной привычки')
    related_habit = models.ForeignKey('self', verbose_name='Связанная привычка', **NULLABLE,
                                      on_delete=models.SET_NULL)
    periodicity = models.SmallIntegerField(verbose_name='Периодичность', choices=Period.choices,
                                           default=Period.DAILY, **NULLABLE)
    reward = models.CharField(max_length=50, verbose_name='Вознаграждение', **NULLABLE)
    lead_time = models.DurationField(default=timedelta(minutes=2), verbose_name='Время на выполнение',)
    is_public = models.BooleanField(verbose_name='Признак публичности', default=True)

    def __str__(self):
        return f'{self.owner} - {self.name}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
        get_latest_by = 'date'

    def save(self, *args, **kwargs):
        if self.nice_habit:
            self.related_habit = None
            self.reward = ''
            super().save(*args, **kwargs)
        elif not self.nice_habit:
            if self.related_habit is not None:
                self.reward = ''
            elif self.reward:
                self.related_habit = None
            super().save(*args, **kwargs)
