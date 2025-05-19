from rest_framework import serializers
from .models import Patient, MCUrecord

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class MCUrecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MCUrecord
        fields = '__all__'
