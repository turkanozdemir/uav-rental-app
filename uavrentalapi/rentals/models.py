from django.contrib.auth.models import User
from django.db import models
from uav.models import UAV


class Rental(models.Model):
    uav = models.ForeignKey(UAV, on_delete=models.CASCADE)
    renting_member = models.ForeignKey(User, on_delete=models.CASCADE)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    total_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.uav.brand} - {self.start_datetime} to {self.end_datetime}"
