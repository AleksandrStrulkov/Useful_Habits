from rest_framework.permissions import IsAuthenticated, AllowAny, DjangoModelPermissionsOrAnonReadOnly
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, \
    get_object_or_404
from habit_app.models import Habit
from habit_app.paginators import HabitPagination
from habit_app.permissions import IsOwner
from habit_app.serializers import HabitSerializer
from habit_app.services import create_reminder, update_reminder, delete_reminder


class HabitCreateAPIView(CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.owner = self.request.user

        create_reminder(new_habit)
        new_habit.save()


class HabitListAPIView(ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitPagination
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        """ Определяем параметры вывода объектов """

        queryset = Habit.objects.filter(owner=self.request.user)
        return queryset


class HabitPublicListAPIView(ListAPIView):
    """ Вывод списка публичных привычек """

    serializer_class = HabitSerializer
    pagination_class = HabitPagination
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        """ Определяем параметры вывода объектов """

        queryset = Habit.objects.filter(is_public=True)
        return queryset


class HabitRetrieveAPIView(RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class HabitUpdateAPIView(UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_update(self, serializer):
        habit = serializer.save()
        update_reminder(habit)
        habit.save()


class HabitDestroyAPIView(DestroyAPIView):
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_destroy(self, instance):
        delete_reminder(instance)
        instance.delete()
