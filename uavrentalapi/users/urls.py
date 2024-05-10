from django.urls import path

from . import views
from .views import BrandUserListView, CustomUserListView

urlpatterns = [
    path('register/', views.UserRegisterAPIView.as_view(), name='user-register'),
    path('login/', views.UserLoginAPIView.as_view(), name='user-login'),
    path('logout/', views.UserLogoutAPIView.as_view(), name='user-logout'),
    path('profile/', views.UserProfileAPIView.as_view(), name='user-profile'),
    path('brand-users-list/', BrandUserListView.as_view(), name='brand_user_list'),
    path('custom-users-list/', CustomUserListView.as_view(), name='custom_user_list'),
]