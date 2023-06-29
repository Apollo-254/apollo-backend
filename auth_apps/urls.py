from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import UserAuthView

app_name = 'auth_apps'

urlpatterns = [
    path('signup', UserAuthView.as_view(), name="signup"),
    path('signin', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
