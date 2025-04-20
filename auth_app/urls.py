from django.urls import path
from .views import (
    CustomTokenObtainPairView,
    RegistroUsuarioView,
    LogoutView,
)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('revocar_token', LogoutView.as_view(), name= "revocar_token"),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token_refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegistroUsuarioView.as_view(), name="register_user")
]
