from django.http import *
from django.shortcuts import render #, render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from datetime import datetime
from plants.models import *
from login. models import *
from .models import Actions, Transactions
from django.apps import apps
from .forms import AddPlantForm, UpdateAttributeForm, UpdatePlantNamesForm #, UpdateTextForm, UpdateSelectForm, UpdateMultiForm
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
import pdb
from django.views.generic import View



from django.template.defaulttags import register
@register.filter
def get_item(dictionary, key):
	return dictionary.get(key)

EmptyPlant = {
	'Characteristics':[
		{'name':'pH_min', 'field_type':'other', 'value':None, 'label':'pH min', 'class_name':'temp'},
		{'name':'pH_max', 'field_type':'other', 'value':None, 'label':'pH max', 'class_name':'temp'},
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
		{'name':'serotiny', 'field_type':'many_to_one', 'value':None, 'label':'serotiny', 'class_name':'Serotiny'},
		{'name':'fertility_needs', 'field_type':'many_to_many', 'value':None, 'label':'nutrient requirements', 'class_name':'NutrientRequirements'},
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
		{'name':'food_prod', 'field_type':'many_to_many', 'value':None, 'label':'food', 'class_name':'FoodProd'},
		{'name':'raw_materials_prod', 'field_type':'many_to_many', 'value':None, 'label':'raw materials', 'class_name':'RawMaterialsProd'},
		{'name':'medicinals_prod', 'field_type':'many_to_many', 'value':None, 'label':'medicinals', 'class_name':'MedicinalsProd'},
		{'name':'biochemical_material_prod', 'field_type':'many_to_many', 'value':None, 'label':'biochemical material', 'class_name':'BiochemicalMaterialProd'},
		{'name':'cultural_and_amenity_prod', 'field_type':'many_to_many', 'value':None, 'label':'cultural and amenity', 'class_name':'CulturalAndAmenityProd'},
		{'name':'mineral_nutrients_prod', 'field_type':'many_to_many', 'value':None, 'label':'mineral nutrients', 'class_name':'MineralNutrientsProd'}
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
	'allelochemicals', 'food_prod', 'animal_food', 'raw_materials_prod', 'medicinals_prod', 'biochemical_material_prod', 'cultural_and_amenity_prod', 'mineral_nutrients_prod',
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
	'animal_food' : 'AnimalFood',
	'raw_materials_prod': 'RawMaterialsProd', 
	'medicinals_prod': 'MedicinalsProd', 
	'biochemical_material_prod' : 'BiochemicalMaterialProd', 
	'cultural_and_amenity_prod' : 'CulturalAndAmenityProd', 
	'mineral_nutrients_prod' : 'MineralNutrientsProd',
	}

def getCharacteristics(request):
	return HttpResponse(json.dumps(EmptyPlant['Characteristics']), content_type="application/json")

def getProducts(request):
	return HttpResponse(json.dumps(EmptyPlant['Products']), content_type="application/json")

def getTolerances(request):
	return HttpResponse(json.dumps(EmptyPlant['Tolerances']), content_type="application/json")

def getNeeds(request):
	return HttpResponse(json.dumps(EmptyPlant['Needs']), content_type="application/json")

def getBehaviors(request):
	return HttpResponse(json.dumps(EmptyPlant['Behaviors']), content_type="application/json")

def reload_attribute_vals_view(request, className=None):
	response_data = {'dropdownvals':[], 'defaultIds':[]}
	defaults = request.GET.getlist('defaultVals[]')
	print(defaults)
	if "insect" in className.lower() or "animal" in className.lower():
		if "insect" in className.lower():
			choices = Insects.objects.all()
		else:
			choices = Animals.objects.all()
		for i in range(0, len(choices)):
			if choices[i].value in defaults:
				response_data['defaultIds'].append(choices[i].id)
			p = dict(id=choices[i].id, text = choices[i].value)
			response_data['dropdownvals'].append(p)
		return HttpResponse(json.dumps(response_data), content_type="application/json")


	# if "insect" in className.lower():
	# 	insects = Insects.objects.all()
	# 	for i in range(0, len(insects)):
	# 		if insects[i].value in defaults: ## THE WAY THIS IS EVALUATED NEEDS TO BE CHANGED EX. AMBROSIA BEETLE
	# 			response_data['defaultIds'].append(insects[i].id)
	# 		p = dict(id=insects[i].id, text = insects[i].value)
	# 		response_data['dropdownvals'].append(p)
	# 	return HttpResponse(json.dumps(response_data), content_type="application/json")
	# elif "animal" in className.lower():
	# 	animals = Animals.objects.all()
	# 	for i in range(0, len(animals)):
	# 		if animals[i].value in defaults: ## THE WAY THIS IS EVALUATED NEEDS TO BE CHANGED EX. AMBROSIA BEETLE
	# 			response_data['defaultIds'].append(animals[i].id)
	# 		p = dict(id=animals[i].id, text = animals[i].value)
	# 		response_data['dropdownvals'].append(p)
	# 	return HttpResponse(json.dumps(response_data), content_type="application/json")
	else:
		cls = globals()[className]
		cls_model = apps.get_model('plants', className)
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

def removeAttribute(request):
	if request.method == 'POST':
		plantId = int(request.POST['plant_id'])
		transaction_id = int(request.POST['transaction_id'])
		prop = request.POST['property_name']

		if transaction_id == 0:
			#transaction = Transactions.objects.create(timestamp=datetime.now(), users_id=1, plants_id=plantId, transaction_type=action_type, ignore=False)
			transaction = Transactions.objects.create(timestamp=datetime.now(), users_id=request.user.id, plants_id=plantId, transaction_type='UPDATE', ignore=False)
			transaction.save()
			response_data = transaction.id
		else:
			transaction = Transactions.objects.get(id=transaction_id)
			response_data = transaction_id

		actions = []
		actions.append(Actions(transactions=transaction , action_type='UPDATE', property=prop, value=None))
		Actions.objects.bulk_create(actions)
		return HttpResponse(json.dumps(response_data))
	else:
		return HttpResponse(json.dumps("GET"))

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
		scientific_name = request.POST['scientificName']
# 		species = request.POST['species']
# 		variety = request.POST['variety']
# 		subspecies = request.POST['subspecies']
# 		cultivar = request.POST['cultivar']
		common_name = request.POST['commonName']
		family = request.POST['family']
		family_common_name = request.POST['familyCommonName']
		endemic_status_text = request.POST['endemicStatus_text']
		if endemic_status_text == '0' or '---' in endemic_status_text:
			endemic_status_text = None

		
		if int(request.POST['scientificName_flag']) == 1:

			genus = ''
			species = ''
			variety = ''
			subspecies = ''
			cultivar = ''
			
			# TODO what about var. in scientific name
			if 'spp.' in scientific_name:
				if scientific_name.endswith('spp.'):
					print("spp only, delete transaction")
					transaction.delete() #we need species specific information. When it is across many species, the information is not reliable enough.
				else:
					sciname_bits= scientific_name.split()
					found = False
					for i in sciname_bits:
						if "spp." in i:
							found = True
						if found:
							subspecies = i;
							continue
			if ' x ' in scientific_name:
				sciname_bits= scientific_name.split()
				genus = sciname_bits[0] + " x " + sciname_bits[2]
				species = None
			if "'" in scientific_name:
				sciname_bits= scientific_name.split()
				for i in sciname_bits: #make sure it is not a genus with a cultivar
					if i.startswith("'") and i.endswith("'"):
						cultivar = i
						if i<2 and genus is None:
							genus = sciname_bits[0]
							species = None
			if "Var. " or "var. " in scientific_name:
				sciname_bits= scientific_name.split()
				found = False
				for i in sciname_bits:
					if "Var." or "var." in i:
						found = True
					if found:
						variety = i;
						continue
			if genus is '':
				#genus has not been defined and needs to be defined
				sciname_bits = scientific_name.split()
				genus = sciname_bits[0]
				if len(sciname_bits) > 1:
					species = sciname_bits[1]
				else:
					print("genus only, delete transaction")
					transaction.delete() #contains a genus name only
				
			
			
			genus_id = ScientificName.objects.filter(value='genus').first().id
			actions.append(Actions(transactions=transaction, action_type=trans_type, property='plant_scientific_name', value=genus, scientific_names=genus_id))
			
			if species is not '':
				species_id = ScientificName.objects.filter(value='species').first().id
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='plant_scientific_name', value=species, scientific_names=species_id))
			if variety is not '':
				variety_id = ScientificName.objects.filter(value='variety').first().id
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='plant_scientific_name', value=variety, scientific_names=variety_id))	
			if subspecies is not '':
				subspecies_id = ScientificName.objects.filter(value='subspecies').first().id
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='plant_scientific_name', value=subspecies, scientific_names=subspecies_id))
			if cultivar is not '':
				cultivar_id = ScientificName.objects.filter(value='cultivar').first().id
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='plant_scientific_name', value=cultivar, scientific_names=cultivar_id))

			
		
		
		# if int(request.POST['genus_flag']) == 1:
# 			genus_id = ScientificName.objects.filter(value='genus').first().id
# 			actions.append(Actions(transactions=transaction , action_type=action_type, property='plant_scientific_name', value=genus, scientific_names=genus_id))
# 		if int(request.POST['species_flag']) == 1:
# 			species_id = ScientificName.objects.filter(value='species').first().id
# 			actions.append(Actions(transactions=transaction, action_type=trans_type, property='plant_scientific_name', value=species, scientific_names=species_id))
# 		if int(request.POST['variety_flag']) == 1:
# 			variety_id = ScientificName.objects.filter(value='variety').first().id
# 			actions.append(Actions(transactions=transaction, action_type=trans_type, property='plant_scientific_name', value=variety, scientific_names=variety_id))	
# 		if int(request.POST['subspecies_flag']) == 1:
# 			subspecies_id = ScientificName.objects.filter(value='subspecies').first().id
# 			actions.append(Actions(transactions=transaction, action_type=trans_type, property='plant_scientific_name', value=subspecies, scientific_names=subspecies_id))
# 		if int(request.POST['cultivar_flag']) == 1:
# 			variety_id = ScientificName.objects.filter(value='cultivar').first().id
# 			actions.append(Actions(transactions=transaction, action_type=trans_type, property='plant_scientific_name', value=cultivar, scientific_names=cultivar_id))
# 			
			
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
			response_data = int(transaction_id)
		return HttpResponse(json.dumps(response_data), content_type="application/json")

def updateSelect(request, transaction_id, action_type):
	if request.method == 'POST':
		cls_name = request.POST['class_name']

		form = UpdateAttributeForm(request.POST, class_name=cls_name)
		#form = UpdateAttributeForm(request.POST, class_name='Plant')
		
		if form.is_valid():
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
			response_data = int(transaction_id)
		return HttpResponse(json.dumps(response_data))

def updateMulti(request, transaction_id, action_type):
	if request.method == 'POST':
		cls_name = request.POST['class_name']
		form = UpdateAttributeForm(request.POST, class_name=cls_name)

		if form.is_valid():
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
			response_data = int(transaction_id)
		return HttpResponse(json.dumps(response_data))


#Plant.imageurl_set

def editPlant(request, plantId=None):
	plant = Plant.objects.get(id=plantId)
	result = {'Characteristics':[], 'Needs':[], 'Tolerances':[], 'Behaviors':[], 'Products':[], 'About':[]}
	for field in plant.get_all_fields:
		if field['name'] is 'region':
			if plant.get_region is None:
				height = {'name' : 'height', 'field_type' : 'other', 'value' : None, 'label' : 'height', 'class_name' : 'FIXME'}
				spread = {'name':'spread', 'field_type':'other', 'value':None, 'label':'spread', 'class_name' : 'FIXME'}
				root_depth = {'name':'root_depth', 'field_type':'other', 'value':None, 'label':'root depth', 'class_name' : 'FIXME'}
			else:
				height = {'name' : 'height', 'field_type' : 'other', 'value' : plant.get_region['height'], 'label' : 'height', 'class_name' : 'FIXME'}
				spread = {'name' : 'spread', 'field_type' : 'other', 'value' : plant.get_region['spread'], 'label' : 'spread', 'class_name' : 'FIXME'}
				root_depth = {'name' : 'root_depth', 'field_type' : 'other', 'value' : plant.get_region['root_depth'], 'label' : 'root depth', 'class_name' : 'FIXME'}
			
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
		'userId': request.user.id,
		'transactionId' : 0,
		'result': result,
		'plantId': plantId, 
		'scientific_name': plant.get_scientific_name,
		'common_name' : plant.common_name,
		'family' : plant.family,
		'family_common_name' : plant.family_common_name,
		'endemic_status' : plant.get_endemic_status,
		'images': ImageURL.objects.filter(plants_id=plantId),
		'updatePlantNamesForm' : UpdatePlantNamesForm(),
		'updateAttributeForm' : UpdateAttributeForm(class_name='Plant'),
	}
	return render(request, 'frontend/editplant.html', context)

@login_required
def addPlant(request):
	if request.method == 'POST':
		addPlantForm = AddPlantForm(request.POST)

		if 'add' in request.POST and addPlantForm.is_valid():
			scientificName = str(request.POST["scientificName"])
			commonName = request.POST["commonName"]

			genus = ''
			species = ''
			variety = ''
			subspecies = ''
			cultivar = ''

			if 'spp.' in scientificName:
				if scientificName.endswith('spp.'):
					print("spp only, delete transaction")
					transaction.delete() #we need species specific information. When it is across many species, the information is not reliable enough.
				else:
					sciname_bits= scientificName.split()
					found = False
					for i in sciname_bits:
						if "spp." in i:
							found = True
						if found:
							subspecies = i;
							continue
			if ' x ' in scientificName:
				sciname_bits= scientificName.split()
				genus = sciname_bits[0] + " x " + sciname_bits[2]
				species = None
			if "'" in scientificName:
				sciname_bits= scientificName.split()
				for i in sciname_bits: #make sure it is not a genus with a cultivar
					if i.startswith("'") and i.endswith("'"):
						cultivar = i
						if i<2 and genus is None:
							genus = sciname_bits[0]
							species = None
			if "Var. " or "var. " in scientificName:
				sciname_bits= scientificName.split()
				found = False
				for i in sciname_bits:
					if "Var." or "var." in i:
						found = True
					if found:
						variety = i;
						continue
			if genus is '':
				sciname_bits = scientificName.split()
				genus = sciname_bits[0]
				if len(sciname_bits) > 1:
					species = sciname_bits[1]
				else:
					print("genus only, delete transaction")
					transaction.delete() #contains a genus name only

				

			transaction = Transactions.objects.create(timestamp=datetime.now(), users_id=request.user.id, transaction_type='INSERT', ignore=False)
			transaction.save()
			actions = []

			genus_id = ScientificName.objects.filter(value='genus').first().id
			actions.append(Actions(transactions=transaction, action_type=trans_type, property='plant_scientific_name', value=genus, scientific_names=genus_id))
			
			if species is not '':
				species_id = ScientificName.objects.filter(value='species').first().id
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='plant_scientific_name', value=species, scientific_names=species_id))
			if variety is not '':
				variety_id = ScientificName.objects.filter(value='variety').first().id
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='plant_scientific_name', value=variety, scientific_names=variety_id))	
			if subspecies is not '':
				subspecies_id = ScientificName.objects.filter(value='subspecies').first().id
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='plant_scientific_name', value=subspecies, scientific_names=subspecies_id))
			if cultivar is not '':
				cultivar_id = ScientificName.objects.filter(value='cultivar').first().id
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='plant_scientific_name', value=cultivar, scientific_names=cultivar_id))

			
			if commonName:
				actions.append(Actions(transactions=transaction , action_type='INSERT', property='common_name', value=commonName))
			
			Actions.objects.bulk_create(actions)

			context = {
				'newPlant':{
					'scientific_name': scientificName,
					'common_name': commonName
				},
				'userId': request.user.id,
				'transactionId' : transaction.id,
				'result': EmptyPlant,
				'plantId': 0, 
				'scientific_name' :scientificName,
				'common_name' : commonName,
				'family' : None,
				'family_common_name' : None,
				'endemic_status' : None,
				'updatePlantNamesForm':UpdatePlantNamesForm(),
				'updateAttributeForm' : UpdateAttributeForm(class_name='Plant'),
			}
			return render(request, 'frontend/editplant.html', context)


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
			#'queryResultSet' : plant_list,
			'images': images
		}
		return render(request, 'frontend/cardview.html', context)

def getFilterResults(field, field_type, value):
	if field_type == "other":
		q = Q(**{"%s" % field: value})
	elif field_type == "many_to_many":
		q = Q(**{"%s__value__icontains" % field: value})
	else: 
		q = Q(**{"%s__value__icontains" % field: value})
	return q


def filter(request):
	if request.method == 'GET':
		#account for multi-value filters?
		fieldLabel = request.GET['filter_field_label']
		field = request.GET['filter_field']
		field_type = request.GET['filter_field_type']
		value = request.GET['filter_value']

		if field == 'height' or field == 'spread' or field == 'root_depth':
			q = Q(**{"plantregion__%s" % field : value})
		else:
			q = getFilterResults(field, field_type, value)

		plant_list = Plant.objects.filter(q)		

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
			'filter_by': fieldLabel + " | " + value
		}
		return render(request, 'frontend/cardview.html', context)


#from itertools import chain
def search(request, searchString):
	print(searchString)
		
	plants = Plant.objects

	# layer_results = Plant.objects.filter(layer__in=Layer.objects.filter(value__icontains=searchString))
	# food_results = Plant.objects.filter(food_prod__in=FoodProd.objects.filter(value__icontains=searchString))
	# rawmat_results = Plant.objects.filter(raw_materials_prod__in=RawMaterialsProd.objects.filter(value__icontains=searchString))
	# med_results = Plant.objects.filter(medicinals_prod__in=MedicinalsProd.objects.filter(value__icontains=searchString))
	# biomed_results = Plant.objects.filter(biochemical_material_prod__in=BiochemicalMaterialProd.objects.filter(value__icontains=searchString))
	# # water_results = Plant.objects.filter(water_needs__in=WaterNeeds.objects.filter(value__icontains=searchString))
	# # sun_results = Plant.objects.filter(sun_needs__in=SunNeeds.objects.filter(value__icontains=searchString))
	# # nutrients_results = Plant.objects.filter(fertility_needs__in=NutrientRequirements.objects.filter(value__icontains=searchString))
	# serotiny_results = Plant.objects.filter(serotiny__in=Serotiny.objects.filter(value__icontains=searchString))
	# erosion_results = Plant.objects.filter(erosion_control__in=ErosionControl.objects.filter(value__icontains=searchString))
	# insect_attract_results = Plant.objects.filter(plants_insect_attractor__in=Insects.objects.filter(value__icontains=searchString))
	# insect_reg_results = Plant.objects.filter(plants_insect_regulator__in=Insects.objects.filter(value__icontains=searchString))

	name_matches = Plant.objects.filter(
		Q(get_scientific_name__icontains=searchString) | 
		Q(common_name__icontains=searchString) |
		Q(get_layer__icontains=searchString))
	# results_list = list(chain(name_matches, layer_results, food_results, rawmat_results, med_results, biomed_results, water_results, sun_results, nutrients_results, serotiny_results, erosion_results, insect_attract_results, insect_reg_results))
	# results_list = list(chain(name_matches, layer_results, food_results, rawmat_results, med_results, biomed_results, serotiny_results, erosion_results, insect_attract_results, insect_reg_results))

	results_list = list(name_matches)

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
		'images': images
	}
	return render(request, 'frontend/cardview.html', context)

