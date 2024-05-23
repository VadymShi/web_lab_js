from rest_framework import serializers
from .models import Office, Worker

class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = ['id', 'name', 'location']

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ['first_name', 'last_name', 'birth_date', 'hire_date', 'profession', 'offices']
