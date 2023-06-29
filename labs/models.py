from django.db import models

# Create your models here.
from hospitals.models import Hospital


class Lab(models.Model):
    hospital_id = models.ForeignKey(Hospital, related_name='hospitals', on_delete=models.CASCADE)
    availability = models.CharField(max_length=50, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
