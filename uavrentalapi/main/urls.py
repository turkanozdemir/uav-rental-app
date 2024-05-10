from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path('uavs/', include('uav.urls')),
    path('rentals/', include('rentals.urls')),
    path('users/', include('users.urls')),
]
