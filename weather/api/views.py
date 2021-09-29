from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

import requests

from .models import Location, Parameter
from .serializers import LocationSerializer, ParameterSerializer
from .permissions import IsAuthenticatedAndOwner, IsAuthenticatedAndLocationOwner

class LocationViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedAndOwner,)
    serializer_class = LocationSerializer
    """
    A simple ViewSet for CRUD locations.
    """
    def get_queryset(self):
        """
        Return a list of all the locations for the currently 
        authenticated user.
        """
        user = self.request.user
        return Location.objects.filter(owner=user)

    def list(self, request):
        queryset = Location.objects.filter(owner=request.user)
        serializer = LocationSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Location.objects.filter(owner=request.user)
        location = get_object_or_404(queryset, pk=pk)
        serializer = LocationSerializer(location, context={'request': request})
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        request.data['owner'] = request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    

class ParameterViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedAndLocationOwner,)
    serializer_class = ParameterSerializer
    """
    A simple ViewSet for CRUD location parameters.
    """
    def get_queryset(self):
        location = self.kwargs['location_id']
        return Parameter.objects.filter(location=location, location__owner=self.request.user)

    def create(self, request, *args, **kwargs):
        request.data['location'] = self.kwargs['location_id']
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)