from django.urls import path, include
from rest_framework import routers

from hospitals.views import HospitalView

app_name = "hospitals"

router = routers.DefaultRouter(trailing_slash=False)
router.register('hospitals', HospitalView)
urlpatterns = [
    path('', include(router.urls))
]
