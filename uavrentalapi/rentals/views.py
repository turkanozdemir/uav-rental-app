from rest_framework import generics, status

from .models import Rental
from .serializers import RentalSerializer


class RentalCreateAPIView(generics.CreateAPIView):
    serializer_class = RentalSerializer

    def perform_create(self, serializer):
        rental = serializer.save()
        # Calculate total_fee
        duration = rental.end_datetime - rental.start_datetime + 1
        daily_fee = rental.uav.daily_fee
        total_fee = duration * daily_fee
        rental.total_fee = total_fee
        rental.save()

class RentalUpdateAPIView(generics.UpdateAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer

class RentalDeleteAPIView(generics.DestroyAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer

class RentalListAPIView(generics.ListAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer

    def get_queryset(self):
        user = self.request.user
        return Rental.objects.filter(renting_member=user)
