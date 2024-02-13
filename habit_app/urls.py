from django.urls import path
from rest_framework import routers

from habit_app.apps import HabitAppConfig
# from online_training.apps import OnlineTrainingConfig
# from online_training.views.course import CourseViewSet
# from online_training.views.lesson import APILessonDetail, APILesson
# from online_training.views.payments import APIPayments, PaymentCreateAPIView, PaymentRetrieveAPIView
# from online_training.views.subscription import SubscriptionCreateAPIView, SubscriptionDestroyAPIView

from habit_app.views import HabitViewSet

app_name = HabitAppConfig.name

# urlpatterns = [
#         path('api/habit/', HabitViewSet.as_view()),
# ]

router = routers.SimpleRouter()
router.register(r'api/habit', HabitViewSet, basename='Привычки')

urlpatterns = router.urls
