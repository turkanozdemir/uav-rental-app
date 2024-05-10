from django.contrib.auth.models import Group, Permission
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import MinLengthValidator
from django.db import models
from rentals.models import Rental
from uav.models import UAV


class BaseUser(models.Model):
    email = models.EmailField(unique=True, null=False, blank=False)
    password = models.CharField(max_length=30, validators=[MinLengthValidator(8)], null=False, blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    address = models.TextField(max_length=250)
    phone_number = models.CharField(max_length=15)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    last_login = models.DateTimeField(null=True, blank=True)  # Add this field


    class Meta:
        abstract = True

class CustomUser(BaseUser):
    first_name = models.CharField(max_length=50, validators=[UnicodeUsernameValidator()], null=False, blank=False)
    last_name = models.CharField(max_length=50, validators=[UnicodeUsernameValidator()], null=False, blank=False)
    payment_info = models.TextField(null=True, blank=True)
    reservation_history = models.ManyToManyField(Rental, related_name='reservations', blank=True)
    favorite_list = models.ManyToManyField(UAV, related_name='favorites', blank=True)
    groups = models.ManyToManyField(Group, related_name='customuser_groups', blank=True)
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',
        blank=True,
    )

class BrandUser(BaseUser):
    company_name = models.CharField(max_length=100, validators=[UnicodeUsernameValidator()], null=False, blank=False)
    company_description = models.TextField()
    uav_list = models.ManyToManyField(UAV, related_name='listed_uavs', blank=True)
    promotions_and_discounts = models.TextField()
    groups = models.ManyToManyField(Group, related_name='branduser_groups', blank=True)
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='brand_user_permissions',
        blank=True,
    )