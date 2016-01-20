from django.shortcuts import render

from .models import Plant

def index(request):	
	plant_list = Plant.objects.filter(genus__startswith='Ag')
	context = {
		'plant_list': plant_list,
	}

	return render(request, 'frontend/cardview.html', context)