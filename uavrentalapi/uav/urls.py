from django.urls import path

from .views import (UAVCreateAPIView, UAVListAPIView,
                    UAVRetrieveUpdateDestroyAPIView)

urlpatterns = [
    path('', UAVCreateAPIView.as_view(), name='uav-create'),
    path('', UAVListAPIView.as_view(), name='uav-list'),
    path('<str:serial_number>', UAVRetrieveUpdateDestroyAPIView.as_view(), name='uav-retrieve-update-destroy'),
]