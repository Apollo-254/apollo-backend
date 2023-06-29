from django.shortcuts import render

# Create your views here.
from rest_framework_simplejwt.views import TokenObtainPairView

from auth_apps.serializers import UserSerializer
from users.models import User


class UserAuthView(TokenObtainPairView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
