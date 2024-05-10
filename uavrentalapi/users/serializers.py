from rest_framework import serializers, status

from .models import BrandUser, CustomUser

BASE_FIELDS = ['email', 'password', 'is_active', 'is_staff', 'created_at', 'address', 'phone_number', 'profile_picture', 'last_login']

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields =  BASE_FIELDS + ['first_name', 'last_name', 'payment_info', 'reservation_history', 'favorite_list', 'groups', 'user_permissions']
        read_only_fields = ['id', 'reservation_history','last_login']

    def create(self, validated_data):
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        phone_number = validated_data.get('phone_number')

        if not first_name or not last_name or not phone_number:
            raise serializers.ValidationError({'error': 'First name, last name, phone, and number fields cannot be empty for custom user'}, status=status.HTTP_400_BAD_REQUEST)
        
        return super().create(validated_data)

class BrandUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandUser
        fields = BASE_FIELDS + ['company_name', 'company_description', 'uav_list', 'promotions_and_discounts', 'groups', 'user_permissions']
        read_only_fields = ['id', 'last_login']

    def create(self, validated_data):
        company_name = validated_data.get('company_name')
        phone_number = validated_data.get('phone_number')

        if not company_name or not phone_number:
            raise serializers.ValidationError({'Company name and phone_number fields cannot be empty for brand user'}, status=status.HTTP_400_BAD_REQUEST)

        validated_data['is_staff'] = True 

        return super().create(validated_data)
 