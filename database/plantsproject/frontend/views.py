#from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render

from .models import Plant

def index(request):	
	plant_list = Plant.objects.all()
	#template = loader.get_template('frontend/index.html')
	context = {
		'plant_list': plant_list,
	}

	return render(request, 'frontend/index.html', context)
	#return HttpResponse(template.render(context, request))