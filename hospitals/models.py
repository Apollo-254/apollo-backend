from django.db import models


# Create your models here.


class Hospital(models.Model):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=100)
    consultation_fee = models.FloatField(default=0.0)
    date_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
