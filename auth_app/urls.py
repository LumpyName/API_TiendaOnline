from django.urls import path
from .views import (
    CustomTokenObtainPairView,
    TokenRefreshViewWithActivity,
    ActualizarUltimaActividadView,
    RefreshTokenManuallyView,
    RegistroUsuarioView
)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/refresh-activity/', TokenRefreshViewWithActivity.as_view(), name='refresh_with_activity'),
    path('actividad/', ActualizarUltimaActividadView.as_view(), name='actualizar_actividad'),
    path('refresh/manual/', RefreshTokenManuallyView.as_view(), name='refresh_manual'),
    path('register/', RegistroUsuarioView, name="register")
]
