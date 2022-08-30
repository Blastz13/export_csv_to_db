from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from incident_api.filters import ReportDateFilterBackend
from incident_api.models import Incident
from incident_api.paginators import IncidentListPagination
from incident_api.serializers import IncidentSerializer


class IncidentListAPIView(generics.ListAPIView):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    pagination_class = IncidentListPagination
    filter_backends = [ReportDateFilterBackend]
    permission_classes = [IsAuthenticated]
