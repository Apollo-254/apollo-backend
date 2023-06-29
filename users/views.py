from django.shortcuts import render

# Create your views here.
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from auth_apps.serializers import UserSerializer
from users.models import User


class UsersView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination

    search_fields = ('^name', '^phone', )
    ordering_fields = ['phone']
