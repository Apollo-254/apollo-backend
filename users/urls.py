from django.urls import path, include
from rest_framework import routers

from .views import UsersView

app_name = "users"

router = routers.DefaultRouter(trailing_slash=False)
router.register('users', UsersView)

urlpatterns = [

    path('', include(router.urls),)
]