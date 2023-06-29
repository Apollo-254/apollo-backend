from django.db import models
from django.conf import settings


# Create your models here.
from users.models import Doctor


class Reviews(models.Model):
    rating = models.IntegerField(default=0)
    comment = models.TextField(null=True, blank=True)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
