from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from habit_app.models import Habit
from users.models import User


class HabitSerializer(serializers.ModelSerializer):
    # course = SlugRelatedField(slug_field='title', queryset=Course.objects.all())
    # owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # owner = SlugRelatedField(slug_field='email', queryset=User.objects.all())

    class Meta:
        model = Habit
        fields = '__all__'
