from rest_framework import serializers
from .models import Location

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'description', 'owner']
        extra_kwargs = {
            'id': {'read_only': True},
            'owner': {'write_only': True},
        }