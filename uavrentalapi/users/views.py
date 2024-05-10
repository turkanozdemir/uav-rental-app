from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import exceptions, generics, permissions, status
from rest_framework.response import Response

from .models import BrandUser, CustomUser
from .serializers import BrandUserSerializer, CustomUserSerializer


class UserRegisterAPIView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]

    def create(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user_type = request.data.get('user_type')

        if not email or not password:
            return Response({'error': 'Email and password fields cannot be empty'}, status=status.HTTP_400_BAD_REQUEST)

        if user_type == 'brand':
            serializer = BrandUserSerializer(data=request.data)
        elif user_type == 'custom':
            serializer = CustomUserSerializer(data=request.data)
        else: 
            raise ValueError("Invalid user type")

        if serializer.is_valid():
            user = serializer.save()
            login(request, user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginAPIView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    #authentication_classes = [SessionAuthentication]
    
    def authenticate(self, request, email, password):
        user_type = request.data.get('user_type')
        
        if user_type == 'brand':
            try:
                user = BrandUser.objects.get(Q(email=email) & Q(password=password))            
            except BrandUser.DoesNotExist:
                raise exceptions.AuthenticationFailed('No such user')
        elif user_type == 'custom':
            try:
                user = CustomUser.objects.get(Q(email=email) & Q(password=password)) 
            except CustomUser.DoesNotExist:
                raise exceptions.AuthenticationFailed('No such user')
        else: 
            raise ValueError("Invalid user type")
    
        return user
    
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        try: 
            user = self.authenticate(request, email=email, password=password)
            login(request, user)
            return Response({'error': 'Login succesfuly'}, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class UserLogoutAPIView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    #authentication_classes = [SessionAuthentication]

    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)

class UserProfileAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    #authentication_classes = [SessionAuthentication]

    def get_object(self):
        return self.request.user

    def get_serializer_class(self):
        if isinstance(self.request.user, BrandUser):
            return BrandUserSerializer
        return CustomUserSerializer

class BrandUserListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = BrandUser.objects.all()
    serializer_class = BrandUserSerializer

class CustomUserListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer