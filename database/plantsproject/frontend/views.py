from django.http import *
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from datetime import datetime
from .models import *
from django.apps import apps
from .forms import AddPlantForm
import json

def getAttributeValues(request, attribute=None, default=None):
	if request.method == 'GET':
		response_data = {'dropdownvals':[], 'defaultIds':[]}
		defaults = default.split()

		class_name = attribute
		cls = globals()[class_name]
		cls_model = apps.get_model('frontend', attribute)
		values = cls_model.objects.values_list("value")

		for i in range(0, len(list(values))):
			if list(values)[i][0] in defaults:
				response_data['defaultIds'].append(i)
			p = dict(id=i, text=list(values)[i][0])
			response_data['dropdownvals'].append(p)
		
		return JsonResponse(response_data)

def populateSearchDropDown():
	choices = {'genus':[], 'species':[], 'variety':[]}
	
	plants = Plant.objects
	plant_list = plants.all()

	genus_list = plants.distinct('genus')
	for plant in genus_list: 
		if plant.genus:
			p = dict(id=plant.id, text=plant.genus, field='genus')
			choices['genus'].append(p)

	species_list = plants.distinct('species')
	for plant in species_list: 
		if plant.species:
			p = dict(id=plant.id, text=plant.species, field='species')
			choices['species'].append(p)

	variety_list = plants.distinct('variety')
	for plant in variety_list: 
		if plant.variety:
			p = dict(id=plant.id, text=plant.variety, field='variety')
			choices['variety'].append(p)
	
	return choices

# def search(request, searchString=None):
# 	add_plant_form = AddPlantForm()
# 	plant_list = Plant.objects.filter(id__gte=5000, id__lte=5005).order_by('id')

# 	context = {
# 		'addPlantForm': add_plant_form,
# 		'plant_list': plant_list,
# 		'searchForThis': json.dumps(populateSearchDropDown()),
# 	}
# 	return render(request, 'frontend/cardview.html', context)

def editPlant(request, plantId=None):
	# if request.method == 'POST':
	# 	form = EditPlantForm(request.POST)
	# 	if form.is_valid():
	# 		return HttpResponseRedirect('POST')
	# else:
	# 	form = EditPlantForm()
		context = {
			'plant': Plant.objects.filter(id=plantId)[0],
			'test': "THIS IS A GET",
			'searchForThis':json.dumps(populateSearchDropDown()),
		}
		redirectURL = 'frontend/editplant.html'
		return render(request, redirectURL, context)

def addPlant(request, searchString=None):
	if request.method == 'POST':
		addPlantForm = AddPlantForm(request.POST)

		if 'add' in request.POST and addPlantForm.is_valid():
			nameArray = str(request.POST["latinName"]).split()
			commonName = request.POST["commonName"]

			# IF EITHER OF THE ABOVE ARE "NONE" RETURN ERRORS!!!!!!!

			genus = None
			species = None
			variety = None

			if len(nameArray) > 0:
				genus = nameArray[0]
			if len(nameArray) > 1:
				species = nameArray[1]
			if len(nameArray) > 2:
				variety = nameArray[2]

			transaction = Transactions.objects.create(timestamp=datetime.now(), users_id=1, transaction_type='INSERT', ignore=False)
			transaction.save()
			#print(transaction.id)
			actions = []
			if genus:
				actions.append(Actions(transactions=transaction , action_type="INSERT", property='genus', value=genus))
			if species: 
				actions.append(Actions(transactions=transaction , action_type="INSERT", property='species', value=species))
			if variety:
				actions.append(Actions(transactions=transaction , action_type="INSERT", property='variety', value=variety))
			if commonName:
				actions.append(Actions(transactions=transaction , action_type="INSERT", property='common_name', value=commonName))
			Actions.objects.bulk_create(actions)

			#add plant id to url below
			return HttpResponseRedirect('/home/edit/1234')


	else:
		add_plant_form = AddPlantForm()
		if searchString == None:
			plant_list = Plant.objects.filter(id__gte=5000, id__lte=5005).order_by('id')
		else:
			plant_list = Plant.objects.filter(id__gte=6000, id__lte=6005).order_by('id')
		context = {
			'addPlantForm': add_plant_form,
			#'searchForm': search_form,
			'plant_list': plant_list,
			'searchForThis': json.dumps(populateSearchDropDown()),
		}
		return render(request, 'frontend/cardview.html', context)
