from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Location, Parameter

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'description', 'owner', 'lat', 'lon', 'aggregation', 'parameters']
        extra_kwargs = {
            'id': {'read_only': True},
            'owner': {'write_only': True},
            'aggregation': {'read_only': True},
        }

    parameters = serializers.SerializerMethodField()

    def get_parameters(self, obj):
        url = reverse('location-detail', args=[obj.id], request=self.context['request'])
        s = url +"parameters"
        return s

class ParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parameter
        fields = ['id', 'name', 'unit', 'api_id', 'values', 'location']
        extra_kwargs = {
            'id': {'read_only': True},
            'values': {'read_only': True},
        }

    def to_representation(self, instance):
        """
        Used to convert the location field to url.
        """
        ret = super().to_representation(instance)
        url = reverse('location-detail', args=[instance.location.id], request=self.context['request'])
        ret['location'] = url
        
        return ret
