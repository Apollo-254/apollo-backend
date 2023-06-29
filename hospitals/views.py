from django.shortcuts import render


# Create your views here.
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from hospitals.models import Hospital
from hospitals.serializers import HospitalSerializer


class HospitalView(ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination

    search_fields = ('^name', '^location',)
    ordering_fields = ['id']
