import time

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from incident_api.filters import ReportDateFilterBackend
from incident_api.models import Incident
from incident_api.paginators import IncidentListPagination
from incident_api.serializers import IncidentSerializer


class IncidentListAPIView(APIView):
    # queryset = Incident.objects.all()
    # serializer_class = IncidentSerializer
    # pagination_class = IncidentListPagination
    # filter_backends = [ReportDateFilterBackend]
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        start = time.time()
        queryset = Incident.objects.filter(report_date__gt="2017-10-10")
        print(len(queryset))
        print(time.time() - start)
