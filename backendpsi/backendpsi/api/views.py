from rest_framework import viewsets
from .models import Patient, MCUrecord
from .serializers import PatientSerializer, MCUrecordSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class MCUrecordViewSet(viewsets.ModelViewSet):
    queryset = MCUrecord.objects.all()
    serializer_class = MCUrecordSerializer
