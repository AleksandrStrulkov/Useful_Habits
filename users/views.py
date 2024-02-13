from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from users.models import User
# from users.serializers import UserSerializer, UserOwnerSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from users.serializers import UserSerializer


class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
