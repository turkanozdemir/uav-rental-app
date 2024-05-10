from django.core.validators import MinValueValidator
from django.db import models


class UAV(models.Model):
    serial_number = models.CharField(max_length=16, primary_key=True)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField() 
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    max_range = models.FloatField(validators=[MinValueValidator(0)])
    max_speed = models.FloatField(validators=[MinValueValidator(0)])
    max_flight_time = models.IntegerField(validators=[MinValueValidator(0)])
    max_payload_capacity = models.FloatField(validators=[MinValueValidator(0)])
    daily_rental_fee = models.DecimalField(max_digits=10, decimal_places=2,validators = [MinValueValidator(1)])
    availability = models.BooleanField(default=True)

    category = models.JSONField(default=list, blank=False, null=False)    
    sensors = models.JSONField(default=list)   
    functionality = models.JSONField(default=list)   
    durability_and_design = models.JSONField(default=list)   
    communication_system = models.JSONField(default=list)   
    security = models.JSONField(default=list)   
    propulsion_system = models.JSONField(default=list)   
    
    def __str__(self):
        return self.serial_number
