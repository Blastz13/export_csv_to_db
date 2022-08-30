from django.urls import path

from incident_api.views import IncidentListAPIView
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('incident/list/', IncidentListAPIView.as_view()),

    path('token/login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
