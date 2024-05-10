from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .models import UAV
from .serializers import UAVSerializer


class UAVCreateAPIView(generics.CreateAPIView):
    serializer_class = UAVSerializer
    permission_classes = [IsAdminUser]

class UAVListAPIView(generics.ListAPIView):
    queryset = UAV.objects.all()
    serializer_class = UAVSerializer

class UAVRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UAV.objects.all()
    serializer_class = UAVSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'serial_number'