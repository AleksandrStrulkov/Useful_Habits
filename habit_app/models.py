from datetime import timedelta

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.db import connection
from django.contrib.auth import get_user_model

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    PERIOD = (
            ('Каждый час', 'Каждый час'),
            ('Каждые три часа', 'Каждые три часа'),
            ('Ежедневно', 'Ежедневно'),
            ('Раз в три дня', 'Раз в три дня'),
            ('Еженедельно', 'Еженедельно',)
    )

    owner = models.ForeignKey(get_user_model(), verbose_name='Пользователь', related_name='habit',
                              on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='Название привычки', **NULLABLE)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    place = models.CharField(max_length=100, verbose_name='Место выполнения', **NULLABLE)
    time_when_execute = models.TimeField(verbose_name='Время когда выполнять')
    action = models.CharField(max_length=150, verbose_name='Действие', **NULLABLE)
    nice_habit = models.BooleanField(default=True, verbose_name='Признак приятной привычки')
    related_habit = models.ForeignKey('self', verbose_name='Связанная привычка', **NULLABLE, on_delete=models.PROTECT)
    periodicity = models.CharField(max_length=30, verbose_name='Периодичность', choices=PERIOD, default='Ежедневно')
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
        elif not self.nice_habit:
            if self.related_habit is not None:
                self.reward = ''
            elif self.reward:
                self.related_habit = None
            super().save(*args, **kwargs)

    def clean(self):
        errors = {}
        if not self.nice_habit and self.related_habit is not None and self.reward:
            errors['nice_habit'] = ValidationError('Для полезной привычки нужно указать связанную привычку или '
                                                   'вознаграждение')
        if self.nice_habit:
            if self.related_habit is not None:
                errors['related_habit'] = ValidationError('У приятной привычки не может быть связанной привычки')
            elif self.reward:
                errors['reward'] = ValidationError('У приятной привычки не может быть вознаграждения')
        if errors:
            raise ValidationError(errors)

    def get_absolute_url(self):
        return "/habit_nice/%s" % self.pk

            


