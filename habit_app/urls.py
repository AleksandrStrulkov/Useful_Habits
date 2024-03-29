from django.urls import path
from habit_app.apps import HabitAppConfig


from habit_app.views import HabitCreateAPIView, HabitListAPIView, HabitRetrieveAPIView, \
    HabitUpdateAPIView, HabitDestroyAPIView, HabitPublicListAPIView

app_name = HabitAppConfig.name

urlpatterns = [
    path('api/habit/create/', HabitCreateAPIView.as_view(), name='post_habit'),
    path('api/habit/', HabitListAPIView.as_view(), name='list_get_habit'),
    path('api/habit/public/', HabitPublicListAPIView.as_view(), name='list_get_habit_public'),
    path('api/habit/<int:pk>/', HabitRetrieveAPIView.as_view(), name='detail_get_habit'),
    path('api/habit/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='put_patch_habit'),
    path('api/habit/delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='delete_habit'),
]
