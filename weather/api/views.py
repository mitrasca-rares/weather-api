from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Location
from .serializers import LocationSerializer

@login_required
@csrf_exempt
def LocationList(request):
    """
    List all locations, or create a new location.
    """
    if request.method == 'GET':
        locations = Location.objects.filter(user=request.user)
        serializer = LocationSerializer(locations, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LocationSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def LocationDetail(request, pk):
    """
    Retrieve, update or delete a location.
    """
    try:
        location = Location.objects.get(pk=pk)
    except Location.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LocationSerializer(location)
        return JsonResponse(serializer.data)

    elif request.method == 'PATCH':
        data = JSONParser().parse(request)
        serializer = LocationSerializer(location, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        location.delete()
        return HttpResponse(status=204)