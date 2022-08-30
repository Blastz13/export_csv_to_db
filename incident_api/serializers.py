from rest_framework import serializers

from incident_api.models import Incident


class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = '__all__'
