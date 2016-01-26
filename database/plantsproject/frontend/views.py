from django.http import *
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Plant

#@login_required
def cardview(request):	
	plant_list = Plant.objects.filter(genus__startswith='Ag')
	context = {
		'plant_list': plant_list,
	}
	return render(request, 'frontend/cardview.html', context)

def editPlant(request):
	context = {}
	return render(request, 'frontend/editplant.html', context)