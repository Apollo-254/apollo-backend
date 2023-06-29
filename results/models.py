from django.db import models

# Create your models here.
from labs.models import Lab
from users.models import User


class Results(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_results")
    lab_id = models.ForeignKey(Lab, related_name="lab_results", on_delete=models.CASCADE)
    results_report = models.FileField(upload_to="uploads/", default='')
    date_submitted = models.DateTimeField(auto_now_add=True)
