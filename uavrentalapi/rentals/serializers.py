from django.contrib.auth.models import User
from rest_framework import serializers, status
from rest_framework.response import Response
from uav.serializers import UAVSerializer

from .models import Rental


class RentalSerializer(serializers.ModelSerializer):
    uav = UAVSerializer()  # Nested serializer for UAV
    renting_member = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Rental
        fields = ['id', 'uav', 'renting_member', 'start_datetime', 'end_datetime', 'total_fee']
        read_only_fields = ['total_fee']

    def create(self, validated_data):
        uav_data = validated_data.pop('uav')
        uav_serializer = UAVSerializer(data=uav_data)
        if uav_serializer.is_valid():
            uav_instance = uav_serializer.save()
            rental = Rental.objects.create(uav=uav_instance, **validated_data)
            return rental
        else:
            raise serializers.ValidationError(uav_serializer.errors)

    def update(self, instance, validated_data):
        uav_data = validated_data.pop('uav', None)
        if uav_data:
            uav_serializer = UAVSerializer(instance.uav, data=uav_data)
            if uav_serializer.is_valid():
                uav_instance = uav_serializer.save()
                instance.uav = uav_instance
            else:
                raise serializers.ValidationError(uav_serializer.errors)
        instance.start_datetime = validated_data.get('start_datetime', instance.start_datetime)
        instance.end_datetime = validated_data.get('end_datetime', instance.end_datetime)
        instance.save()
        return instance