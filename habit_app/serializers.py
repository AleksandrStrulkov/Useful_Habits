from rest_framework import serializers
from habit_app.models import Habit
from habit_app.validators import HabitValidator


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [HabitValidator(nice_habit='nice_habit', related_habit='related_habit', reward='reward',
                                     lead_time='lead_time',)]
