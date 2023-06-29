from django.db import models


# Create your models here.
from hospitals.models import Hospital
from users.models import User


class Payment(models.Model):
    reference_id = models.CharField(max_length=120)
    hospital_id = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name="hospital_payment")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_payment")
    amount = models.FloatField(default=0.0)
    payments_phone = models.CharField(max_length=30)
