from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
    )


urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='get_token'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('verify/', TokenVerifyView.as_view(), name='verify_token'),
]