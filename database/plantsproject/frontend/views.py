from django.http import *
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from datetime import datetime
from .models import *
from django.apps import apps
from .forms import AddPlantForm, UpdateAttributeForm, UpdatePlantNamesForm #, UpdateTextForm, UpdateSelectForm, UpdateMultiForm
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
import pdb


EmptyPlant = {
	'Characteristics':[
		{'name':'ph_min', 'field_type':'other', 'value':None, 'label':'pH min', 'class_name':'temp'},
		{'name':'ph_max', 'field_type':'other', 'value':None, 'label':'pH max', 'class_name':'temp'},
		{'name':'degree_of_serotiny', 'field_type':'many_to_one', 'value':None, 'label':'degree of serotiny', 'class_name':'DegreeOfSerotiny'},
		{'name':'duration', 'field_type':'many_to_many', 'value':None, 'label':'duration', 'class_name':'Duration'},
		{'name':'height', 'field_type':'other', 'value':None, 'label':'height', 'class_name':'temp'},
		{'name':'spread', 'field_type':'other', 'value':None, 'label':'spread', 'class_name':'temp'},
		{'name':'root_depth', 'field_type':'other', 'value':None, 'label':'root depth', 'class_name':'temp'},
		{'name':'layer', 'field_type':'many_to_many', 'value':None, 'label':'layer', 'class_name':'Layer'},
		{'name':'canopy_density', 'field_type':'many_to_many', 'value':None, 'label':'canopy density', 'class_name':'CanopyDensity'},
		{'name':'active_growth_period', 'field_type':'many_to_many', 'value':None, 'label':'active growth period', 'class_name':'ActiveGrowthPeriod'},
		{'name':'harvest_period', 'field_type':'many_to_many', 'value':None, 'label':'harvest period', 'class_name':'HarvestPeriod'},
		{'name':'leaf_retention', 'field_type':'many_to_many', 'value':None, 'label':'leaf retention', 'class_name':'LeafRetention'},
		{'name':'flower_color', 'field_type':'many_to_many', 'value':None, 'label':'flower color', 'class_name':'FlowerColor'},
		{'name':'foliage_color', 'field_type':'many_to_many', 'value':None, 'label':'foliage color', 'class_name':'FoliageColor'},
		{'name':'fruit_color', 'field_type':'many_to_many', 'value':None, 'label':'fruit color', 'class_name':'FruitColor'}
	],
	'Needs':[
		{'name':'innoculant', 'field_type':'other', 'value':None, 'label':'innoculant', 'class_name':'temp'},
		{'name':'serotiny', 'field_type':'many_to_one', 'value':None, 'label':'serotiny', 'class_name':'temp'},
		{'name':'fertility_needs', 'field_type':'many_to_many', 'value':None, 'label':'Nutrient Requirements', 'class_name':'NutrientRequirements'},
		{'name':'water_needs', 'field_type':'many_to_many', 'value':None, 'label':'water needs', 'class_name':'WaterNeeds'},
		{'name':'sun_needs', 'field_type':'many_to_many', 'value':None, 'label':'sun needs', 'class_name':'SunNeeds'}
	],
	'Behaviors':[
		{'name':'livestock_bloat', 'field_type':'many_to_one', 'value':None, 'label':'livestock bloat', 'class_name':'LivestockBloat'},
		{'name':'toxicity', 'field_type':'many_to_one', 'value':None, 'label':'toxicity', 'class_name':'Toxicity'},
		{'name':'erosion_control', 'field_type':'many_to_many', 'value':None, 'label':'erosion control', 'class_name':'ErosionControl'},
		{'name':'plants_insect_attractor', 'field_type':'many_to_many', 'value':None, 'label':'plants insect attractor', 'class_name':'PlantInsectAttractorByRegion'},
		{'name':'plants_insect_regulator', 'field_type':'many_to_many', 'value':None, 'label':'plants insect regulator', 'class_name':'PlantInsectRegulatorByRegion'},
		{'name':'plants_animal_regulator', 'field_type':'many_to_many', 'value':None, 'label':'plants animal regulator', 'class_name':'PlantAnimalRegulatorByRegion'},
		{'name':'plants_animal_attractor', 'field_type':'many_to_many', 'value':None, 'label':'plants animal attractor', 'class_name':'PlantAnimalAttractorByRegion'}
	],
	'Tolerances':[
		{'name':'salt_tol', 'field_type':'many_to_one', 'value':None, 'label':'salt tol', 'class_name':'SaltTol'},
		{'name':'flood_tol', 'field_type':'many_to_one', 'value':None, 'label':'flood tol', 'class_name':'FloodTol'},
		{'name':'drought_tol', 'field_type':'many_to_one', 'value':None, 'label':'drought tol', 'class_name':'DroughtTol'},
		{'name':'humidity_tol', 'field_type':'many_to_one', 'value':None, 'label':'humidity tol', 'class_name':'HumidityTol'},
		{'name':'wind_tol', 'field_type':'many_to_one', 'value':None, 'label':'wind tol', 'class_name':'WindTol'},
		{'name':'fire_tol', 'field_type':'many_to_one', 'value':None, 'label':'fire tol', 'class_name':'FireTol'},
		{'name':'minimum_temperature_tol', 'field_type':'other', 'value':None, 'label':'minimum temperature tol', 'class_name':'temp'},
		{'name':'shade_tol', 'field_type':'many_to_many', 'value':None, 'label':'shade tol', 'class_name':'ShadeTol'},
		{'name':'soil_drainage_tol', 'field_type':'many_to_many', 'value':None, 'label':'soil drainage tol', 'class_name':'SoilDrainageTol'},
	],
	'Products':[
		{'name':'allelochemicals', 'field_type':'other', 'value':None, 'label':'allelochemicals', 'class_name':'temp'},
		{'name':'food_prod', 'field_type':'many_to_many', 'value':None, 'label':'food prod', 'class_name':'FoodProd'},
		{'name':'raw_materials_prod', 'field_type':'many_to_many', 'value':None, 'label':'raw materials prod', 'class_name':'RawMaterialsProd'},
		{'name':'medicinals_prod', 'field_type':'many_to_many', 'value':None, 'label':'medicinals prod', 'class_name':'MedicinalsProd'},
		{'name':'biochemical_material_prod', 'field_type':'many_to_many', 'value':None, 'label':'biochemical material prod', 'class_name':'BiochemicalMaterialProd'},
		{'name':'cultural_and_amenity_prod', 'field_type':'many_to_many', 'value':None, 'label':'cultural and amenity prod', 'class_name':'CulturalAndAmenityProd'},
		{'name':'mineral_nutrients_prod', 'field_type':'many_to_many', 'value':None, 'label':'mineral nutrients prod', 'class_name':'MineralNutrientsProd'}
	]
}

Characteristics = [
	'duration', 'pH_min', 'pH_max', 'layer', 'canopy_density', 'active_growth_period', 'harvest_period', 'leaf_retention', 'flower_color',
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
	'pH_min': 'fixthis', 
	'pH_max' :'fixthis', 
	'region':'fixthis',
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

def reload_attribute_vals_view(request, className=None, default=None):
	response_data = {'dropdownvals':[], 'defaultIds':[]}
	defaults = default.split()

	if "insect" in className.lower():
		insects = Insects.objects.all()
		for i in range(0, len(insects)):
			if insects[i].value in defaults: ## THE WAY THIS IS EVALUATED NEEDS TO BE CHANGED EX. AMBROSIA BEETLE
				response_data['defaultIds'].append(insects[i].value)
			p = dict(id=insects[i].id, text = insects[i].value)
			response_data['dropdownvals'].append(p)
		return HttpResponse(json.dumps(response_data), content_type="application/json")
	elif "animal" in className.lower():
		animals = Animals.objects.all()
		for i in range(0, len(animals)):
			if animals[i].value in defaults: ## THE WAY THIS IS EVALUATED NEEDS TO BE CHANGED EX. AMBROSIA BEETLE
				response_data['defaultIds'].append(animals[i].value)
			p = dict(id=animals[i].id, text = animals[i].value)
			response_data['dropdownvals'].append(p)
		return HttpResponse(json.dumps(response_data), content_type="application/json")
	else:
		cls = globals()[className]
		cls_model = apps.get_model('frontend', className)
		values = cls_model.objects.values_list("value", "id")
		for i in range(0, len(list(values))):
			if list(values)[i][0] in defaults: ## THE WAY THIS IS EVALUATED NEEDS TO BE CHANGED MANY TO MANY DEFAULTS NOT WORKING
				response_data['defaultIds'].append(list(values)[i][1])
			p = dict(id=list(values)[i][1], text=list(values)[i][0])
			response_data['dropdownvals'].append(p)
		return HttpResponse(json.dumps(response_data), content_type="application/json")

def addImg(request):
	if request.method == 'POST':
		plant = Plant.objects.get(id=request.POST['plant_id'])
		relation = ImageURL(plants=plant, value=request.POST['image_url'])
		relation.save()

		#transaction/action instead??

		response_data = "post"
	else:
		response_data = "get"

	return HttpResponse(json.dumps(response_data), content_type="application/json")

def updateNames(request):
	if request.method == 'POST': 
		form = UpdatePlantNamesForm(request.POST)
		plantId = int(request.POST['plant_id'])

		transaction_id = int(request.POST['transaction_id'])
		action_type = "UPDATE"

		if transaction_id == 0:
			#transaction = Transactions.objects.create(timestamp=datetime.now(), users_id=1, plants_id=plantId, transaction_type=action_type, ignore=False)
			transaction = Transactions.objects.create(timestamp=datetime.now(), users_id=request.user.id, plants_id=plantId, transaction_type=action_type, ignore=False)
			transaction.save()
		else:
			transaction = Transactions.objects.get(id=transaction_id)

		actions = []
		
		#pdb.set_trace()
		genus = request.POST['genus']
		species = request.POST['species']
		variety = request.POST['variety']
		common_name = request.POST['commonName']
		family = request.POST['family']
		family_common_name = request.POST['familyCommonName']
		endemic_status_text = request.POST['endemicStatus_text']
		if endemic_status_text == '0' or '---' in endemic_status_text:
			endemic_status_text = None

		if int(request.POST['genus_flag']) == 1:
			actions.append(Actions(transactions=transaction , action_type=action_type, property='genus', value=genus))
		if int(request.POST['species_flag']) == 1:
			actions.append(Actions(transactions=transaction , action_type=action_type, property='species', value=species))
		if int(request.POST['variety_flag']) == 1:
			actions.append(Actions(transactions=transaction , action_type=action_type, property='variety', value=variety))
		if int(request.POST['commonName_flag']) == 1:
			actions.append(Actions(transactions=transaction , action_type=action_type, property='common_name', value=common_name))
		if int(request.POST['family_flag']) == 1:
			actions.append(Actions(transactions=transaction , action_type=action_type, property='family_name', value=family))
		if int(request.POST['familyCommonName_flag']) == 1:
			actions.append(Actions(transactions=transaction , action_type=action_type, property='family_common_name', value=family_common_name))
		if int(request.POST['endemicStatus_flag']) == 1:
			endemic_status = request.POST['endemicStatus']
			if endemic_status != '':
				actions.append(Actions(transactions=transaction , action_type=action_type, property='endemic_status', value=endemic_status))
		Actions.objects.bulk_create(actions)
		return HttpResponse()

def updateText(request, transaction_id, action_type):
	if request.method == 'POST':
		form = UpdateAttributeForm(request.POST, class_name='Plant')

		if form.is_valid():
			print("Update Text is valid")
			property = request.POST['property_name']
			value = request.POST['text']
			plantId = request.POST['plant_id']

			if int(transaction_id) == 0:
				#transaction = Transactions.objects.create(timestamp=datetime.now(), users_id=1, plants_id=plantId, transaction_type='UPDATE', ignore=False)
				transaction = Transactions.objects.create(timestamp=datetime.now(), users_id=request.user.id, plants_id=plantId, transaction_type='UPDATE', ignore=False)
				transaction.save()
			else:
				transaction = Transactions.objects.get(id = transaction_id)
			actions = []
			actions.append(Actions(transactions=transaction , action_type=action_type, property=property, value=value))
			Actions.objects.bulk_create(actions)
			response_data = transaction.id
		else:
			print("~~INVALID FORM~~")
			response_data = int(transaction_id)
		return HttpResponse(json.dumps(response_data), content_type="application/json")

def updateSelect(request, transaction_id, action_type):
	if request.method == 'POST':
		cls_name = request.POST['class_name']

		form = UpdateAttributeForm(request.POST, class_name=cls_name)
		#form = UpdateAttributeForm(request.POST, class_name='Plant')
		
		if form.is_valid():
			print("Update select is valid")
			property = request.POST['property_name']
			value = request.POST['select']
			plantId = request.POST['plant_id']

			if int(transaction_id) == 0:
				#transaction = Transactions.objects.create(timestamp=datetime.now(), users_id=1, plants_id=plantId, transaction_type='UPDATE', ignore=False)
				transaction = Transactions.objects.create(timestamp=datetime.now(), users_id=request.user.id, plants_id=plantId, transaction_type='UPDATE', ignore=False)
				transaction.save()
			else:
				transaction = Transactions.objects.get(id = transaction_id)
			actions = []
			actions.append(Actions(transactions=transaction , action_type=action_type, property=property, value=value))
			Actions.objects.bulk_create(actions)
			response_data = transaction.id
		else:
			print("~~INVALID FORM~~")
			response_data = int(transaction_id)
		return HttpResponse(json.dumps(response_data))

def updateMulti(request, transaction_id, action_type):
	
	if request.method == 'POST':
		#form = UpdateMultiForm(request.POST)
		cls_name = request.POST['class_name']
		form = UpdateAttributeForm(request.POST, class_name=cls_name)
		#pdb.set_trace()
		if form.is_valid():
			print("Update multi is valid")
			property = request.POST['property_name']
			values = dict(request.POST)['multi']
			plantId = request.POST['plant_id']
			# oldVals = request.POST['old_vals']
			# oldVals = oldVals.split(",") WHY WAS THIS HERE

			if int(transaction_id) == 0: 
				transaction = Transactions.objects.create(timestamp=datetime.now(), users_id=request.user.id, plants_id=plantId, transaction_type='UPDATE', ignore=False)
				#transaction = Transactions.objects.create(timestamp=datetime.now(), users_id=1, plants_id=plantId, transaction_type='UPDATE', ignore=False)
				transaction.save()
			else:
				transaction = Transactions.objects.get(id = transaction_id)
			actions = []

			for i in range(0, len(values)):
				actions.append(Actions(transactions=transaction , action_type=action_type , property=property, value=values[i]))
			Actions.objects.bulk_create(actions)

			response_data = transaction.id
		else:
			print("~~INVALID FORM~~")
			response_data = int(transaction_id)
		return HttpResponse(json.dumps(response_data))

#Plant.imageurl_set

def editPlant(request, plantId=None):
	plant = Plant.objects.get(id=plantId)
	result = {'Characteristics':[], 'Needs':[], 'Tolerances':[], 'Behaviors':[], 'Products':[], 'About':[]}
	for field in plant.get_all_fields:
		if field['name'] is 'region':
			if plant.get_region() is None:
				height = dict(name='height', field_type='other', value=None, label='height', class_name = 'FIXME')
				spread = dict(name='spread', field_type='other', value=None, label='spread', class_name = 'FIXME')
				root_depth = dict(name='root_depth', field_type='other', value=None, label='root depth', class_name = 'FIXME')
			else:
				height = dict(name='height', field_type='other', value=plant.get_region()['height'], label='height', class_name = 'FIXME')
				spread = dict(name='spread', field_type='other', value=plant.get_region()['spread'], label='spread', class_name = 'FIXME')
				root_depth = dict(name='root_depth', field_type='other', value=plant.get_region()['root_depth'], label='root depth', class_name = 'FIXME')
			
			result['Characteristics'].append(height)
			result['Characteristics'].append(spread)
			result['Characteristics'].append(root_depth)
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

	context = {
		# 'isNew': 1,
		'userId': request.user.id,
		'transactionId' : 0,
		'result': result,
		'plantId': plantId, 
		'genus' : plant.genus,
		'species' : plant.species,
		'variety' : plant.variety,
		'common_name' : plant.common_name,
		'family' : plant.family,
		'family_common_name' : plant.family_common_name,
		'endemic_status' : plant.get_endemic_status,
		'images': ImageURL.objects.filter(plants_id=plantId),
		'searchForThis': {},#json.dumps(populateSearchDropDown()),
		# 'updateTextForm': UpdateTextForm(),
		# 'updateSelectForm': UpdateSelectForm(class_name='Plant'),
		# 'updateMulitForm': UpdateMultiForm(),
		'updatePlantNamesForm' : UpdatePlantNamesForm(),
		'updateAttributeForm' : UpdateAttributeForm(class_name='Plant'),
	}
	return render(request, 'frontend/editplant.html', context)

@login_required
def addPlant(request):
	if request.method == 'POST':
		addPlantForm = AddPlantForm(request.POST)

		if 'add' in request.POST and addPlantForm.is_valid():
			nameArray = str(request.POST["latinName"]).split()
			commonName = request.POST["commonName"]

			# IF EITHER OF THE ABOVE ARE "NONE" RETURN ERRORS!!!!!!! -- the UI doesnt allow ether to be none

			genus = None
			species = None
			variety = None

			if len(nameArray) > 0:
				genus = nameArray[0]
			if len(nameArray) > 1:
				species = nameArray[1]
			if len(nameArray) > 2:
				variety = nameArray[2]

			transaction = Transactions.objects.create(timestamp=datetime.now(), users_id=request.user.id, transaction_type='INSERT', ignore=False)
			#transaction = Transactions.objects.create(timestamp=datetime.now(), users_id=1, transaction_type='INSERT', ignore=False)
			transaction.save()
			actions = []

			if genus:
				actions.append(Actions(transactions=transaction , action_type='INSERT', property='genus', value=genus))
			if species:
				actions.append(Actions(transactions=transaction , action_type='INSERT', property='species', value=species))
			if variety:
				actions.append(Actions(transactions=transaction , action_type='INSERT', property='variety', value=variety))
			if commonName:
				actions.append(Actions(transactions=transaction , action_type='INSERT', property='common_name', value=commonName))
			Actions.objects.bulk_create(actions)

			# plant = Plant.objects.create()
			# result = {'Characteristics':[], 'Needs':[], 'Tolerances':[], 'Behaviors':[], 'Products':[], 'About':[]}
			# for field in plant.get_all_fields:
			# 	if field['name'] is 'region':
			# 		if plant.get_region() is None:
			# 			height = dict(name='height', field_type='other', value=None, label='height', class_name = 'FIXME')
			# 			spread = dict(name='spread', field_type='other', value=None, label='spread', class_name = 'FIXME')
			# 			root_depth = dict(name='root_depth', field_type='other', value=None, label='root depth', class_name = 'FIXME')
			# 		else:
			# 			height = dict(name='height', field_type='other', value=plant.get_region()['height'], label='height', class_name = 'FIXME')
			# 			spread = dict(name='spread', field_type='other', value=plant.get_region()['spread'], label='spread', class_name = 'FIXME')
			# 			root_depth = dict(name='root_depth', field_type='other', value=plant.get_region()['root_depth'], label='root depth', class_name = 'FIXME')
			# 		result['Characteristics'].append(height)
			# 		result['Characteristics'].append(spread)
			# 		result['Characteristics'].append(root_depth)
			# 	if field['name'] in Characteristics:
			# 		field.update({'class_name':PropertyToClassName[field['name']]})
			# 		result['Characteristics'].append(field)
			# 	elif field['name'] in Needs:
			# 		field.update({'class_name':PropertyToClassName[field['name']]})
			# 		result['Needs'].append(field)
			# 	elif field['name'] in Tolerances:
			# 		field.update({'class_name':PropertyToClassName[field['name']]})
			# 		result['Tolerances'].append(field)
			# 	elif field['name'] in Products:
			# 		field.update({'class_name':PropertyToClassName[field['name']]})
			# 		result['Products'].append(field)
			# 	elif field['name'] in Behaviors:
			# 		field.update({'class_name':PropertyToClassName[field['name']]})
			# 		result['Behaviors'].append(field)
			# 	else:
			# 		result['About'].append(field)



			# pdb.set_trace()

			context = {
				'newPlant':{
					'genus': genus,
					'species': species,
					'variety': variety,
					'common_name': commonName
				},
				'userId': request.user.id,
				'transactionId' : transaction.id,
				'result': EmptyPlant,
				'plantId': 0, 
				'genus' : genus,
				'species' : species,
				'variety' : variety,
				'common_name' : commonName,
				'family' : None,
				'family_common_name' : None,
				'endemic_status' : None,
				#'images': ImageURL.objects.get(plant.id=4121),
				'searchForThis': {},#json.dumps(populateSearchDropDown()),
				# 'updateTextForm': UpdateTextForm(),
				# 'updateSelectForm': UpdateSelectForm(class_name='Plant'),
				# 'updateMulitForm': UpdateMultiForm(),
				'updatePlantNamesForm':UpdatePlantNamesForm(),
				'updateAttributeForm' : UpdateAttributeForm(class_name='Plant'),
			}
			return render(request, 'frontend/editplant.html', context)

from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key):
	return dictionary.get(key)

def viewPlants(request):
	if request.method == 'GET':
		plant_list = Plant.objects.all()
		paginator = Paginator(plant_list, 35)
		page = request.GET.get('page')

		try:
			plants = paginator.page(page)
		except PageNotAnInteger:
			plants = paginator.page(1)
		except EmptyPage:
			plants = paginator.page(paginator.num_pages)

		iterableImages = ImageURL.objects.all()
		images = {}
		plantIdsAlreadyUsed = []
		for img in iterableImages:
			if img.plants.id not in plantIdsAlreadyUsed:
				images[img.plants.id] = img.value
				plantIdsAlreadyUsed.append(img.plants.id)


		context = {
			'addPlantForm': AddPlantForm(),
			'plants':plants,
			'images': images,
			'searchForThis': [],#json.dumps(populateSearchDropDown()),
		}
		return render(request, 'frontend/cardview.html', context)

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

from itertools import chain


def search(request):
	searchString = request.POST['searchVal']
	plants = Plant.objects
	#plant_list = Plant.objects.all()


	layer_results = Plant.objects.filter(layer__in=Layer.objects.filter(value__icontains=searchString))
	food_results = Plant.objects.filter(food_prod__in=FoodProd.objects.filter(value__icontains=searchString))
	rawmat_results = Plant.objects.filter(raw_materials_prod__in=RawMaterialsProd.objects.filter(value__icontains=searchString))
	med_results = Plant.objects.filter(medicinals_prod__in=MedicinalsProd.objects.filter(value__icontains=searchString))
	biomed_results = Plant.objects.filter(biochemical_material_prod__in=BiochemicalMaterialProd.objects.filter(value__icontains=searchString))
	# water_results = Plant.objects.filter(water_needs__in=WaterNeeds.objects.filter(value__icontains=searchString))
	# sun_results = Plant.objects.filter(sun_needs__in=SunNeeds.objects.filter(value__icontains=searchString))
	# nutrients_results = Plant.objects.filter(fertility_needs__in=NutrientRequirements.objects.filter(value__icontains=searchString))
	serotiny_results = Plant.objects.filter(serotiny__in=Serotiny.objects.filter(value__icontains=searchString))
	erosion_results = Plant.objects.filter(erosion_control__in=ErosionControl.objects.filter(value__icontains=searchString))
	insect_attract_results = Plant.objects.filter(plants_insect_attractor__in=Insects.objects.filter(value__icontains=searchString))
	insect_reg_results = Plant.objects.filter(plants_insect_regulator__in=Insects.objects.filter(value__icontains=searchString))

	name_matches = Plant.objects.filter(Q(genus__icontains=searchString) | 
		Q(species__icontains=searchString) | 
		Q(variety__icontains=searchString) |
		Q(common_name__icontains=searchString) |
		Q(innoculant__icontains=searchString))
	# results_list = list(chain(name_matches, layer_results, food_results, rawmat_results, med_results, biomed_results, water_results, sun_results, nutrients_results, serotiny_results, erosion_results, insect_attract_results, insect_reg_results))
	results_list = list(chain(name_matches, layer_results, food_results, rawmat_results, med_results, biomed_results, serotiny_results, erosion_results, insect_attract_results, insect_reg_results))

	paginator = Paginator(results_list, 35)
	page = request.GET.get('page')
	try:
		plants = paginator.page(page)
	except PageNotAnInteger:
		plants = paginator.page(1)
	except EmptyPage:
		plants = paginator.page(paginator.num_pages)
	iterableImages = ImageURL.objects.all()
	images = {}
	plantIdsAlreadyUsed = []
	for img in iterableImages:
		if img.plants.id not in plantIdsAlreadyUsed:
			images[img.plants.id] = img.value
			plantIdsAlreadyUsed.append(img.plants.id)


	context = {
		'addPlantForm': AddPlantForm(),
		'plants':plants,
		'images': images,
		'searchForThis': [],#json.dumps(populateSearchDropDown()),
	}
	return render(request, 'frontend/cardview.html', context)