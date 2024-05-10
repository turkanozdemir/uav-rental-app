from django.urls import path

from .views import (RentalCreateAPIView, RentalDeleteAPIView,
                    RentalListAPIView, RentalUpdateAPIView)

urlpatterns = [
    path('', RentalCreateAPIView.as_view(), name='rental-create'),
    path('', RentalListAPIView.as_view(), name='rental-list'),
    path('<int:pk>', RentalUpdateAPIView.as_view(), name='rental-update'),
    path('<int:pk>', RentalDeleteAPIView.as_view(), name='rental-delete'),
]