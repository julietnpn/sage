from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from plants.models import Plant
from plants.serializers import PlantSerializer


def plant_list(request):
    """
    List all plants
    """
    if request.method == 'GET':
        plants = Plant.objects.all()
        serializer = PlantSerializer(plants, many=True)
        return JsonResponse(serializer.data, safe=False)

def plant_detail(request, pk):
    """
    Retrieve, a plant.
    """
    try:
        plant = Plant.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PlantSerializer(plant)
        return JsonResponse(serializer.data)
