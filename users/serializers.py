from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        # fields = ("id", "first_name", "email", "payments",)
        fields = ("id", "first_name", "email", )




