"""
URL mappings for the user API.
"""
from django.urls import path

from user import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('jwt-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt-token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me/', views.ManageUserView.as_view(), name='me'),
]
