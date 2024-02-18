from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# from django.urls import path

from users.apps import UsersConfig
from users.views import UsersViewSet

from django.urls import path

app_name = UsersConfig.name

router = routers.SimpleRouter()
router.register(r'api/users', UsersViewSet, basename='пользователи')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls

