from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from plants.models import Plant
from plants.serializers import PlantSerializer
from django.shortcuts import render, redirect #, render_to_response, redirect


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
        
def api_documentation(request):
    if request.method == 'GET':
        all = 'all-plants'
        cname="Coastal sagebrush"
        example_plant = Plant.objects.filter(common_name = cname)[0]
        context = {
            'all_plants': all,
            'example_plant_id': example_plant.id,
            'example_plant_cname': example_plant.common_name
        }
        return render(request, 'api/documentation.html', context)
