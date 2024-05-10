from django.contrib import admin

from .models import BrandUser, CustomUser

admin.site.register(CustomUser)
admin.site.register(BrandUser)