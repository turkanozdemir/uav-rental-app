from rest_framework import serializers
from users.models import BrandUser

from .models import UAV


class UAVSerializer(serializers.ModelSerializer):
    class Meta:
        model = UAV
        fields = '__all__'
    
    def create(self, request, validated_data):
        brand_user_email = request.user.email if request and request.user.is_authenticated else None

        if brand_user_email:
            try:
                brand_user = BrandUser.objects.get(user_email=brand_user_email)
                validated_data['brand'] = brand_user.company_name
            except BrandUser.DoesNotExist:
                pass  
        return super().create(validated_data)
