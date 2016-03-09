from django.http import *
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from datetime import datetime
from .models import *
from django.apps import apps
from .forms import AddPlantForm, UpdateTextForm, UpdateSelectForm, UpdateMultiForm
from django.core import serializers
import json
import pdb

Characteristics = [
	'duration', 'height', 'spread', 'ph_min', 'ph_max', 'layer', 'canopy_density', 'active_growth_period', 'harvest_period', 'leaf_retention', 'flower_color',
	'foliage_color', 'fruit_color', 'degree_of_serotiny', 
]
Needs = [
	'fertility_needs', 'water_needs', 'innoculant', 'sun_needs', 'serotiny'
]
Behaviors = [
	'erosion_control', 'plants_insect_attractor', 'plants_insect_regulator', 'plants_animal_attractor', 'plants_animal_regulator', 'livestock_bloat', 'toxicity',
]
Tolerances = [
	'shade_tol', 'salt_tol', 'flood_tol', 'drought_tol', 'humidity_tol', 'wind_tol', 'soil_drainage_tol', 'fire_tol', 'minimum_temperature_tol'
]
Products = [
	'allelochemicals', 'food_prod', 'raw_materials_prod', 'medicinals_prod', 'biochemical_material_prod', 'cultural_and_amenity_prod', 'mineral_nutrients_prod',
]

PropertyToClassName={
	### Characteristics ###
	'duration':'Duration', #was multiselect but should be only one
	'height':'PlantHeightAtMaturityByRegion', #didnt work
	'spread':'PlantSpreadAtMaturityByRegion', #didnt work
	'ph_min': 'fixthis', 
	'ph_max' :'fixthis', 
	'layer' : 'Layer', 
	'canopy_density' : 'CanopyDensity', #was multiselect but should be only one
	'active_growth_period' : 'ActiveGrowthPeriod', 
	'harvest_period' : 'HarvestPeriod', 
	'leaf_retention' : 'LeafRetention', #was multiselect but should be only one
	'flower_color' : 'FlowerColor',
	'foliage_color' : 'FoliageColor', 
	'fruit_color' : 'FruitColor', 
	'degree_of_serotiny'  : 'DegreeOfSerotiny', #didnt work

	### Needs ###
	'fertility_needs':'NutrientRequirements', #didnt work
	'water_needs':'WaterNeeds', #was multiselect but should be only one
	'innoculant':'fixthis', #didnt work
	'sun_needs': 'SunNeeds', #didnt work 
	'serotiny' :'Serotiny', #didnt work

	### Behaviors ###
	'erosion_control' : 'ErosionControl', 
	'plants_insect_attractor' : 'PlantInsectAttractorByRegion', #didnt work
	'plants_insect_regulator' : 'PlantInsectRegulatorByRegion', #didnt work
	'plants_animal_attractor' : 'PlantAnimalAttractorByRegion', #didnt work
	'plants_animal_regulator' : 'PlantAnimalRegulatorByRegion', #didnt work
	'livestock_bloat' : 'LivestockBloat', 
	'toxicity' : 'Toxicity',

	### Tolerances ###
	'shade_tol': 'ShadeTol', #didnt give the default val
	'salt_tol': 'SaltTol', #didnt work
	'flood_tol' : 'FloodTol', 
	'drought_tol' : 'DroughtTol', 
	'humidity_tol' : 'HumidityTol', 
	'wind_tol' : 'WindTol', 
	'soil_drainage_tol': 'SoilDrainageTol', #didntw ork
	'fire_tol' : 'FireTol', #gave back wrong default
	'minimum_temperature_tol' : 'fixthis',

	### Products ###
	'allelochemicals': 'fixthis', 
	'food_prod' : 'FoodProd', 
	'raw_materials_prod': 'RawMaterialsProd', 
	'medicinals_prod': 'MedicinalsProd', 
	'biochemical_material_prod' : 'BiochemicalMaterialProd', 
	'cultural_and_amenity_prod' : 'CulturalAndAmenityProd', 
	'mineral_nutrients_prod' : 'MineralNutrientsProd',
	}

def getAttributeValues(request, attribute=None, default=None):
	if request.method == 'GET':
		response_data = {'dropdownvals':[], 'defaultIds':[]}
		defaults = default.split()

		class_name = attribute
		cls = globals()[class_name]
		cls_model = apps.get_model('frontend', class_name)
		values = cls_model.objects.values_list("value")
		# values = cls_model.objects.all()
		# print("loading values " + values)

		for i in range(0, len(list(values))):
			if list(values)[i][0] in defaults:
				response_data['defaultIds'].append(i)
			p = dict(id=i, text=list(values)[i][0])
			response_data['dropdownvals'].append(p)
		
		return JsonResponse(response_data)

def reload_attribute_vals_view(request, className=None, default=None):

	response_data = {'dropdownvals':[], 'defaultIds':[]}
	defaults = default.split()

	class_name = className
	cls = globals()[class_name]
	cls_model = apps.get_model('frontend', class_name)
	values = cls_model.objects.values_list("value", "id")

	for i in range(0, len(list(values))):
			if list(values)[i][0] in defaults:
				response_data['defaultIds'].append(list(values)[i][1])
			p = dict(id=list(values)[i][1], text=list(values)[i][0])
			response_data['dropdownvals'].append(p)


	return HttpResponse(json.dumps(response_data), content_type="application/json")

def updateText(request):
	if request.method == 'POST':
		form = UpdateTextForm(request.POST)

		if form.is_valid():
			property = request.POST['property_name']
			value = request.POST['text']
			plantId = request.POST['plant_id']
			transaction = Transactions.objects.create(timestamp=datetime.now(), users_id=1, plants_id=plantId, transaction_type='UPDATE', ignore=False)
			transaction.save()
			actions = []
			actions.append(Actions(transactions=transaction , action_type="UPDATE", property=property, value=value))
			Actions.objects.bulk_create(actions)
			response_data = {"Success":"success"}
		else:
			response_data = {'dropdownvals':[request.POST['select']], 'defaultIds':['post select- invalid']}
		return JsonResponse(response_data)


def updateSelect(request):
	if request.method == 'POST':
		cls_name = request.POST['class_name']
		form = UpdateSelectForm(request.POST, class_name=cls_name)
		#pdb.set_trace()
		
		if form.is_valid():
			property = request.POST['property_name']
			value = request.POST['select']
			plantId = request.POST['plant_id']
			transaction = Transactions.objects.create(timestamp=datetime.now(), users_id=1, plants_id=plantId, transaction_type='UPDATE', ignore=False)
			transaction.save()
			#print(transaction.id)
			actions = []
			actions.append(Actions(transactions=transaction , action_type="UPDATE", property=property, value=value))
			Actions.objects.bulk_create(actions)
			response_data = {"Success":"success"}
		else:
			response_data = {'dropdownvals':[request.POST['select']], 'defaultIds':['post select- invalid']}
		return JsonResponse(response_data)


def updateMulti(request):
	if request.method == 'POST':
		form = UpdateMultiForm(request.POST)
		
		if form.is_valid():
			property = request.POST['property_name']
			values = dict(request.POST)['multi']
			plantId = request.POST['plant_id']
			oldVals = request.POST['old_vals']
			oldVals = oldVals.split(",")
			transaction = Transactions.objects.create(timestamp=datetime.now(), users_id=1, plants_id=plantId, transaction_type='UPDATE', ignore=False)
			transaction.save()
			actions = []

			for i in range(0, len(values)):
				actions.append(Actions(transactions=transaction , action_type="INSERT", property=property, value=values[i]))
			Actions.objects.bulk_create(actions)

			response_data = {"Success":"success"}
		else:
			response_data = {'dropdownvals':[], 'defaultIds':['post multi- invalid', ]}
		return JsonResponse(response_data)

#Plant.imageurl_set

# def populateSearchDropDown():
# 	choices = {'genus':[], 'species':[], 'variety':[]}
	
# 	plants = Plant.objects
# 	plant_list = plants.all()

# 	genus_list = plants.distinct('genus')
# 	for plant in genus_list: 
# 		if plant.genus:
# 			p = dict(id=plant.id, text=plant.genus, field='genus')
# 			choices['genus'].append(p)

# 	species_list = plants.distinct('species')
# 	for plant in species_list: 
# 		if plant.species:
# 			p = dict(id=plant.id, text=plant.species, field='species')
# 			choices['species'].append(p)

# 	variety_list = plants.distinct('variety')
# 	for plant in variety_list: 
# 		if plant.variety:
# 			p = dict(id=plant.id, text=plant.variety, field='variety')
# 			choices['variety'].append(p)
	
# 	return choices

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
	plant = Plant.objects.get(id=plantId)
	result = {'Characteristics':[], 'Needs':[], 'Tolerances':[], 'Behaviors':[], 'Products':[], 'About':[]}
	for field in plant.get_all_fields:
		if field['name'] in Characteristics:
			field.update({'class_name':PropertyToClassName[field['name']]})
			result['Characteristics'].append(field)
		elif field['name'] in Needs:
			field.update({'class_name':PropertyToClassName[field['name']]})
			result['Needs'].append(field)
		elif field['name'] in Tolerances:
			field.update({'class_name':PropertyToClassName[field['name']]})
			result['Tolerances'].append(field)
		elif field['name'] in Products:
			field.update({'class_name':PropertyToClassName[field['name']]})
			result['Products'].append(field)
		elif field['name'] in Behaviors:
			field.update({'class_name':PropertyToClassName[field['name']]})
			result['Behaviors'].append(field)
		else:
			result['About'].append(field)
	genus = plant.genus
	species = plant.species
	variety = plant.variety
	common_name = plant.common_name
	family = plant.family
	family_common_name = plant.family_common_name
	endemic_status = plant.get_endemic_status

	context = {
		'result': result,
		'plantId': plantId, 
		'genus' : genus,
		'species' : species,
		'variety' : variety,
		'common_name' : common_name,
		'family' : family,
		'family_common_name' : family_common_name,
		'endemic_status' : endemic_status,
		'searchForThis': {},#json.dumps(populateSearchDropDown()),
		#'updateForm' : UpdateForm(),
		'updateTextForm': UpdateTextForm(),
		'updateSelectForm': UpdateSelectForm(class_name='Plant'),
		'updateMulitForm': UpdateMultiForm(),
	}
	return render(request, 'frontend/editplant.html', context)

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
			return HttpResponseRedirect('/home/edit/8667' )#+ transaction.id)


	else:
		add_plant_form = AddPlantForm()
		plant_list = Plant.objects.filter(id__gte=5000, id__lte=5005).order_by('id')[:5]
		if searchString != None:
			plant_list = Plant.objects.filter(Q()).order_by('id')
		context = {
			'addPlantForm': add_plant_form,
			'plant_list': plant_list,
			'searchForThis': [],#json.dumps(populateSearchDropDown()),
		}
		return render(request, 'frontend/cardview.html', context)
