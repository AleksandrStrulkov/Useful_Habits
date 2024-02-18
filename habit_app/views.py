from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, \
    get_object_or_404
from habit_app.models import Habit
from habit_app.paginators import HabitPagination
from habit_app.serializers import HabitSerializer


class HabitCreateAPIView(CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitListAPIView(ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitPagination


class HabitRetrieveAPIView(RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitUpdateAPIView(UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitDestroyAPIView(DestroyAPIView):
    queryset = Habit.objects.all()



































































class HabitViewSet(ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        # course = serializer.validated_data.get('payment_course')
        habit = serializer.save()
        # payment.user = self.request.user
        # if payment.payment_method == 'Перевод':
        #     payment.session_id = get_session(payment).id
        #     payment.payment_amount = payment.payment_course.price
        habit.full_clean()
        habit.save()

    # def perform_create(self, serializer):
    #     new_course = serializer.save()
    #     new_course.owner = self.request.user
    #     new_course.save()