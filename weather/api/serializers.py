from rest_framework import serializers
from .models import Location, Parameter

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'description', 'owner', 'lat', 'lon', 'aggregation']
        extra_kwargs = {
            'id': {'read_only': True},
            'owner': {'write_only': True},
            'aggregation': {'read_only': True},
        }

class ParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parameter
        fields = ['id', 'name', 'unit', 'api_id', 'values', 'location']
        extra_kwargs = {
            'id': {'read_only': True},
            'location': {'write_only': True},
            'values': {'read_only': True},
        }