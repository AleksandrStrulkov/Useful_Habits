from rest_framework import routers
# from django.urls import path

from users.apps import UsersConfig
from users.views import UsersViewSet

from django.urls import path

app_name = UsersConfig.name

router = routers.SimpleRouter()
router.register(r'api/users', UsersViewSet, basename='пользователи')
urlpatterns = router.urls
