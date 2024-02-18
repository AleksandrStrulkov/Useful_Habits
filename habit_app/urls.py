from django.urls import path
from rest_framework import routers

from habit_app.apps import HabitAppConfig


from habit_app.views import HabitViewSet, HabitCreateAPIView, HabitListAPIView, HabitRetrieveAPIView, \
    HabitUpdateAPIView, HabitDestroyAPIView

app_name = HabitAppConfig.name

urlpatterns = [
        # path('api/habit/', HabitViewSet.as_view()),
        path('api/habit/create/', HabitCreateAPIView.as_view(), name='post_habit'),
        path('api/habit/', HabitListAPIView.as_view(), name='list_get_habit'),
        path('api/habit/<int:pk>/', HabitRetrieveAPIView.as_view(), name='detail_get_habit'),
        path('api/habit/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='put_patch_habit'),
        path('api/habit/delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='delete_habit'),
]

# router = routers.SimpleRouter()
# router.register(r'api/habit', HabitViewSet, basename='Привычки')
#
# urlpatterns = router.urls
