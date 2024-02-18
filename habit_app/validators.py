import re
from datetime import timedelta

from rest_framework.serializers import ValidationError


class HabitValidator:
    def __init__(self, nice_habit, related_habit, reward, lead_time):
        self.nice_habit = nice_habit
        self.related_habit = related_habit
        self.reward = reward
        self.lead_time = lead_time

    def __call__(self, field):
        errors = {}
        if not field['nice_habit'] and field['related_habit'] is not None and field['reward']:
            errors['nice_habit'] = ValidationError(
                'Для полезной привычки нужно указать связанную привычку или '
                'вознаграждение'
                )
            raise ValidationError(errors)

        if field['nice_habit']:
            if field['related_habit'] is not None:
                errors['related_habit'] = ValidationError('У приятной привычки не может быть связанной привычки')
            elif field['reward']:
                errors['reward'] = ValidationError('У приятной привычки не может быть вознаграждения')

        if field['lead_time'] > timedelta(minutes=2):
            errors['lead_time'] = ValidationError('Время выполнения должно быть не больше 2 минут')

        if field['related_habit']:
            if not field['related_habit'].nice_habit:
                errors['related_habit_true'] = ValidationError('В связанные привычки могут попадать только привычки'
                                                               ' с признаком приятной привычки')

        if field['name'] == 'Полезная':
            if field['nice_habit']:
                errors['nice_habit_false'] = ValidationError('Ели привычка полезная, то указывается false')
        if field['name'] == 'Приятная':
            if not field['nice_habit']:
                errors['nice_habit_true'] = ValidationError('Ели привычка приятная, то указывается true')

        if errors:
            raise ValidationError(errors)
