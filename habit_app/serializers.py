from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from datetime import datetime
from time import mktime
import datetime as dt
from habit_app.models import Habit
from habit_app.validators import HabitValidator
from users.models import User


class HabitSerializer(serializers.ModelSerializer):
    # habit_time_minus = serializers.SerializerMethodField()

    # def get_habit_time_minus(self, obj):
    #     convert_time = obj.time_when_execute.strftime('%Y-%m-%d %H:%M:%S.%f')
    #     time_minus = convert_time - dt.timedelta(minutes=3)
    #     return time_minus

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [HabitValidator(nice_habit='nice_habit', related_habit='related_habit', reward='reward',
                                     lead_time='lead_time',)]
