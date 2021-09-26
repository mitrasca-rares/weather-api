from rest_framework import serializers
from .models import Location, Parameter

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'description', 'owner', 'aggregation']
        extra_kwargs = {
            'id': {'read_only': True},
            'owner': {'write_only': True},
        }

class ParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parameter
        fields = ['id', 'name', 'values', 'location']
        extra_kwargs = {
            'id': {'read_only': True},
            'location': {'write_only': True},
        }