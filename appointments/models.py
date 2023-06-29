from django.db import models

# Create your models here.
from labs.models import Lab
from users.models import User

APPOINTMENT_TYPE = {
    "lab": "lab appointment",
    "doctor": "Doctor appointment"
}


class Appointments(models.Model):
    ap_type = models.CharField(default=APPOINTMENT_TYPE.get('doctor'), max_length=100)
    app_date = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="appointment_user", null=True, blank=True)
    ap_status = models.CharField(default="Pending", max_length=50)
    lab_id = models.ForeignKey(Lab, on_delete=models.CASCADE, null=True, blank=True, related_name='lab_appointment')
