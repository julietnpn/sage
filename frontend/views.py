from django.http import *
from django.shortcuts import render, redirect #, render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from datetime import datetime
from plants.models import *
from login. models import *
from .models import Actions, Transactions
from django.contrib.auth.models import User
from django.apps import apps
from .forms import AddPlantForm, UpdateAttributeForm, UpdatePlantNamesForm #, UpdateTextForm, UpdateSelectForm, UpdateMultiForm
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
import pdb
from django.views.generic import View
import csv



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
        {'name':'life_span', 'field_type':'other', 'value':None, 'label':'life span in years', 'class_name':'temp'},
        {'name':'height', 'field_type':'other', 'value':None, 'label':'height', 'class_name':'temp'},
        {'name':'spread', 'field_type':'other', 'value':None, 'label':'spread', 'class_name':'temp'},
        {'name':'root_depth', 'field_type':'other', 'value':None, 'label':'root depth', 'class_name':'temp'},
        {'name':'layer', 'field_type':'many_to_many', 'value':None, 'label':'layer', 'class_name':'Layer'},
        {'name':'canopy_density', 'field_type':'many_to_many', 'value':None, 'label':'canopy density', 'class_name':'CanopyDensity'},
        {'name':'active_growth_period', 'field_type':'many_to_many', 'value':None, 'label':'active growth period', 'class_name':'ActiveGrowthPeriod'},
        {'name':'harvest_period', 'field_type':'many_to_many', 'value':None, 'label':'harvest period', 'class_name':'HarvestPeriod'},
        {'name':'time_to_first_harvest', 'field_type':'other', 'value':None, 'label':'time to first harvest in months', 'class_name':'temp'},
        {'name':'leaf_retention', 'field_type':'many_to_many', 'value':None, 'label':'leaf retention', 'class_name':'LeafRetention'},
        {'name':'flower_color', 'field_type':'many_to_many', 'value':None, 'label':'flower color', 'class_name':'FlowerColor'},
        {'name':'foliage_color', 'field_type':'many_to_many', 'value':None, 'label':'foliage color', 'class_name':'FoliageColor'},
        {'name':'fruit_color', 'field_type':'many_to_many', 'value':None, 'label':'fruit color', 'class_name':'FruitColor'}
    ],
    'Needs':[
        {'name':'inoculant', 'field_type':'other', 'value':None, 'label':'inoculant', 'class_name':'temp'},
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
        {'name':'heat_tol', 'field_type':'other', 'value':None, 'label':'heat tol', 'class_name':'temp'},
        
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
    'duration', 'life_span', 'pH_min', 'pH_max', 'layer', 'canopy_density', 'active_growth_period', 'harvest_period', 'time_to_first_harvest', 'leaf_retention', 'flower_color',
    'foliage_color', 'fruit_color', 'degree_of_serotiny', 
]
Needs = [
    'fertility_needs', 'water_needs', 'inoculant', 'sun_needs', 'serotiny'
]
Behaviors = [
    'erosion_control', 'plants_insect_attractor', 'plants_insect_regulator', 'plants_animal_attractor', 'plants_animal_regulator', 'livestock_bloat', 'toxicity',
]
Tolerances = [
    'shade_tol', 'salt_tol', 'flood_tol', 'drought_tol', 'humidity_tol', 'wind_tol', 'soil_drainage_tol', 'fire_tol', 'minimum_temperature_tol', 'heat_tol'
]
Products = [
    'allelochemicals', 'food_prod', 'animal_food', 'raw_materials_prod', 'medicinals_prod', 'biochemical_material_prod', 'cultural_and_amenity_prod', 'mineral_nutrients_prod',
]

PropertyToClassName={
    ### Characteristics ###
    'duration':'Duration', #was multiselect but should be only one
    'life_span' : 'fixthis', 
    'height':'PlantHeightAtMaturityByRegion', #didnt work
    'spread':'PlantSpreadAtMaturityByRegion', #didnt work
    'pH_min': 'fixthis', 
    'pH_max' :'fixthis', 
    'region':'fixthis',
    'layer' : 'Layer', 
    'canopy_density' : 'CanopyDensity', #was multiselect but should be only one
    'active_growth_period' : 'ActiveGrowthPeriod', 
    'harvest_period' : 'HarvestPeriod', 
    'time_to_first_harvest' : 'fixthis',
    'leaf_retention' : 'LeafRetention', #was multiselect but should be only one
    'flower_color' : 'FlowerColor',
    'foliage_color' : 'FoliageColor', 
    'fruit_color' : 'FruitColor', 
    'degree_of_serotiny'  : 'DegreeOfSerotiny', #didnt work

    ### Needs ###
    'fertility_needs':'NutrientRequirements', #didnt work
    'water_needs':'WaterNeeds', #was multiselect but should be only one
    'inoculant':'fixthis', #didnt work
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
    'heat_tol' : 'fixthis',

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
    print("in reload attribute")
    if "insect" in className.lower() or "animal" in className.lower():
        if "insect" in className.lower():
            choices = Insects.objects.all()
        if "animal" in className.lower():
            choices = Animals.objects.all()
        for i in range(0, len(choices)):
            if choices[i].value in defaults:
                response_data['defaultIds'].append(choices[i].id)
            p = dict(id=choices[i].id, text = choices[i].value)
            response_data['dropdownvals'].append(p)
            return HttpResponse(json.dumps(response_data), content_type="application/json")
    if "waterunits" in className.lower():
        units_choices= WaterUnits.objects.all()
        print(units_choices)
        for i in range(0, len(units_choices)):
            if units_choices[i].value in defaults:
                response_data['defaultIds'].append(units_choices[i].id)
            p = dict(id=units_choices[i].id, text = units_choices[i].value)
            print("has units")
            response_data['dropdownvals'].append(p)
            return HttpResponse(json.dumps(response_data), content_type="application/json")
    if "waterfrequency" in className.lower():
        frequency_choices= WaterFrequency.objects.all()
        print(frequency_choices)
        for i in range(0, len(frequency_choices)):
            if frequency_choices[i].value in defaults:
                response_data['defaultIds'].append(frequency_choices[i].id)
            p = dict(id=frequency_choices[i].id, text = frequency_choices[i].value)
            print("has frequency")
            response_data['dropdownvals'].append(p)
            return HttpResponse(json.dumps(response_data), content_type="application/json")
            
    if "waterseason" in className.lower():
        season_choices= WaterSeason.objects.all()
        print(season_choices)
        for i in range(0, len(season_choices)):
            if season_choices[i].value in defaults:
                response_data['defaultIds'].append(season_choices[i].id)
            p = dict(id=season_choices[i].id, text = season_choices[i].value)
            print("has season")
            response_data['dropdownvals'].append(p)
        return HttpResponse(json.dumps(response_data), content_type="application/json")


    # if "insect" in className.lower():
    #   insects = Insects.objects.all()
    #   for i in range(0, len(insects)):
    #       if insects[i].value in defaults: ## THE WAY THIS IS EVALUATED NEEDS TO BE CHANGED EX. AMBROSIA BEETLE
    #           response_data['defaultIds'].append(insects[i].id)
    #       p = dict(id=insects[i].id, text = insects[i].value)
    #       response_data['dropdownvals'].append(p)
    #   return HttpResponse(json.dumps(response_data), content_type="application/json")
    # elif "animal" in className.lower():
    #   animals = Animals.objects.all()
    #   for i in range(0, len(animals)):
    #       if animals[i].value in defaults: ## THE WAY THIS IS EVALUATED NEEDS TO BE CHANGED EX. AMBROSIA BEETLE
    #           response_data['defaultIds'].append(animals[i].id)
    #       p = dict(id=animals[i].id, text = animals[i].value)
    #       response_data['dropdownvals'].append(p)
    #   return HttpResponse(json.dumps(response_data), content_type="application/json")
    
    print("not animal, or insect")
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
            transaction = Transactions.objects.create(timestamp=datetime.now(), users_id=request.user.id, plants_id=plantId, transaction_type='UPDATE', parent_transaction = parent_transactions(plantId), ignore=False)
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
            transaction = Transactions.objects.create(timestamp=datetime.now(), users_id=request.user.id, plants_id=plantId, transaction_type=action_type, parent_transaction = parent_transactions(plantId), ignore=False)
            transaction.save()
        else:
            transaction = Transactions.objects.get(id=transaction_id)

        actions = []
        
        #pdb.set_trace()
        scientific_name = request.POST['scientificName']
#       species = request.POST['species']
#       variety = request.POST['variety']
#       subspecies = request.POST['subspecies']
#       cultivar = request.POST['cultivar']
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
                species = ''
            if "'" in scientific_name:
                sciname_bits= scientific_name.split()
                for i in sciname_bits: #make sure it is not a genus with a cultivar
                    if i.startswith("'") and i.endswith("'"):
                        cultivar = i
                        if i<2 and genus is None:
                            genus = sciname_bits[0]
                            species = ''
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
                
            
            trans_type = 'UPDATE'
            genus_id = ScientificName.objects.filter(value='genus').first()
            actions.append(Actions(transactions=transaction, action_type=trans_type, property='scientific_name', value=genus, scientific_names=genus_id))
            
            if species is not '':
                species_id = ScientificName.objects.filter(value='species').first()
                actions.append(Actions(transactions=transaction, action_type=trans_type, property='scientific_name', value=species, scientific_names=species_id))
            if variety is not '':
                variety_id = ScientificName.objects.filter(value='variety').first()
                actions.append(Actions(transactions=transaction, action_type=trans_type, property='scientific_name', value=variety, scientific_names=variety_id))   
            if subspecies is not '':
                subspecies_id = ScientificName.objects.filter(value='subspecies').first()
                actions.append(Actions(transactions=transaction, action_type=trans_type, property='scientific_name', value=subspecies, scientific_names=subspecies_id))
            if cultivar is not '':
                cultivar_id = ScientificName.objects.filter(value='cultivar').first()
                actions.append(Actions(transactions=transaction, action_type=trans_type, property='scientific_name', value=cultivar, scientific_names=cultivar_id))

            
        
        
        # if int(request.POST['genus_flag']) == 1:
#           genus_id = ScientificName.objects.filter(value='genus').first().id
#           actions.append(Actions(transactions=transaction , action_type=action_type, property='plant_scientific_name', value=genus, scientific_names=genus_id))
#       if int(request.POST['species_flag']) == 1:
#           species_id = ScientificName.objects.filter(value='species').first().id
#           actions.append(Actions(transactions=transaction, action_type=trans_type, property='plant_scientific_name', value=species, scientific_names=species_id))
#       if int(request.POST['variety_flag']) == 1:
#           variety_id = ScientificName.objects.filter(value='variety').first().id
#           actions.append(Actions(transactions=transaction, action_type=trans_type, property='plant_scientific_name', value=variety, scientific_names=variety_id)) 
#       if int(request.POST['subspecies_flag']) == 1:
#           subspecies_id = ScientificName.objects.filter(value='subspecies').first().id
#           actions.append(Actions(transactions=transaction, action_type=trans_type, property='plant_scientific_name', value=subspecies, scientific_names=subspecies_id))
#       if int(request.POST['cultivar_flag']) == 1:
#           variety_id = ScientificName.objects.filter(value='cultivar').first().id
#           actions.append(Actions(transactions=transaction, action_type=trans_type, property='plant_scientific_name', value=cultivar, scientific_names=cultivar_id))
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
            reference = request.POST['reference']

            if int(transaction_id) == 0:
                #transaction = Transactions.objects.create(timestamp=datetime.now(), users_id=1, plants_id=plantId, transaction_type='UPDATE', ignore=False)
                transaction = Transactions.objects.create(timestamp=datetime.now(), users_id=request.user.id, plants_id=plantId, transaction_type='UPDATE', parent_transaction = parent_transactions(plantId), ignore=False)
                transaction.save()
            else:
                transaction = Transactions.objects.get(id = transaction_id)
            actions = []
            actions.append(Actions(transactions=transaction , action_type=action_type, property=property, value=value, reference=reference))
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
            reference = request.POST['reference']

            if int(transaction_id) == 0:
                #transaction = Transactions.objects.create(timestamp=datetime.now(), users_id=1, plants_id=plantId, transaction_type='UPDATE', ignore=False)
                transaction = Transactions.objects.create(timestamp=datetime.now(), users_id=request.user.id, plants_id=plantId, transaction_type='UPDATE', parent_transaction = parent_transactions(plantId), ignore=False)
                transaction.save()
            else:
                transaction = Transactions.objects.get(id = transaction_id)
            actions = []
            actions.append(Actions(transactions=transaction , action_type=action_type, property=property, value=value , reference=reference))
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
            reference = request.POST['reference']
            # oldVals = request.POST['old_vals']
            # oldVals = oldVals.split(",") WHY WAS THIS HERE

            if int(transaction_id) == 0: 
                transaction = Transactions.objects.create(timestamp=datetime.now(), users_id=request.user.id, plants_id=plantId, transaction_type='UPDATE', parent_transaction = parent_transactions(plantId), ignore=False)
                #transaction = Transactions.objects.create(timestamp=datetime.now(), users_id=1, plants_id=plantId, transaction_type='UPDATE', ignore=False)
                transaction.save()
            else:
                transaction = Transactions.objects.get(id = transaction_id)
            actions = []

            for i in range(0, len(values)):
                actions.append(Actions(transactions=transaction , action_type=action_type , property=property, value=values[i], reference=reference))
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
        'plant': plant,
        'plantId': plantId, 
        'scientific_name': plant.get_scientific_name,
        'common_name' : plant.common_name,
        'family' : plant.family,
        'family_common_name' : plant.family_common_name,
        'endemic_status' : plant.get_endemic_status,
        'images': ImageURL.objects.filter(plants_id=plantId),
        'updatePlantNamesForm' : UpdatePlantNamesForm(),
        'updateAttributeForm' : UpdateAttributeForm(class_name='Plant'),
        'contributors' : getContributors(plantId),
        'activity': getActivity(plantId)
    }
    return render(request, 'frontend/editplant.html', context)

def getContributors(plantID):

    #get list of unique users associated with that ID - this returns a query set of user ids
    contributorIDs_qs = Transactions.objects.filter(plants_id = plantID).values_list('users',flat = True).distinct()
    #make list of user ids and usernames
    # contributorIDs = []
#     contributorUserNames = []
    contributors = []
    for c in contributorIDs_qs:
        # contributorIDs.append(c)
#         contributorUserNames.append(User.objects.get(id = c).username)
        contributor = {
            "userID" : c, 
            "userName":User.objects.get(id = c).username}
        contributors.append(contributor)
    
    
    print(contributors)
    return contributors

def getActivity(plantId):
    transactionIDs_qs = Transactions.objects.filter(plants_id = plantId)

    activities = []
    for t in transactionIDs_qs:

        actions = Actions.objects.filter(transactions_id = t.id)
        for a in actions:
            try:
                property_model = next((m for m in apps.get_models() if m._meta.db_table == a.property), None)
                value = property_model.objects.get(id = a.value).value 
            except:
                value = a.value
        
            activity = {
                "activityID" : a.id,
                "activityType" : a.action_type,
                "activityProperty" : a.property,
                "activityValue" : value,
                "userID" : User.objects.get(id = Transactions.objects.get(id = a.transactions_id).users_id).username,
                "reference" : a.reference
            }
            activities.append(activity)

    return activities

@login_required
def addPlant(request):
    if request.method == 'POST':
        addPlantForm = AddPlantForm(request.POST)

        if 'add' in request.POST and addPlantForm.is_valid():
            scientificName = str(request.POST["scientificName"])
            commonName = request.POST["commonName"]

            name = ''
            genus = ''
            species = ''
            variety = ''
            subspecies = ''
            cultivar = ''
            delete = False
            response = ''
            
#First check that we can create a true name
            if 'spp.' in scientificName:
                if scientificName.endswith('spp.'):
                    print("spp only, delete transaction")
                    delete = True
                    response = 'You did not enter a valid name'
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
                species = ''
            if "'" in scientificName:
                sciname_bits= scientificName.split()
                for i in sciname_bits: #make sure it is not a genus with a cultivar
                    if i.startswith("'") and i.endswith("'"):
                        cultivar = i
                        if i<2 and genus is None:
                            genus = sciname_bits[0]
                            species = ''
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
                    print("genus only, do not create transaction")
                    delete = True
                    response = 'You did not enter a valid name'
            
            name = genus + species + subspecies + variety + cultivar

                
#Confirm the plant doesn't already exist in the database
            all_plants = Plant.objects.all()
            for p in all_plants:
                try:
                    ps = PlantScientificName.objects.filter(plants=p.id)
                except PlantScientificName.DoesNotExist:
                    print('Plant Scientific Name Does not Exist for plant' + str(p.id))
                    
                pname = ''
                pgenus = ''
                pspecies = ''
                pvariety = ''
                psubspecies = ''
                pcultivar = ''

                for a in ps:
                    sc = a.scientific_name
                    if sc.value in 'genus':
                        pgenus = a.value
                    elif sc.value in 'species':
                        pspecies = a.value
                    elif sc.value in 'subspecies':
                        psubspecies = a.value
                    elif sc.value in 'variety':
                        pvariety = a.value
                    elif sc.value in 'variety':
                        pcultivar = a.value + "'"
                        
                pname = pgenus + pspecies+ psubspecies + pvariety + pcultivar
                
                if pname in name:
                    delete = True  # don't want to add a plant already in the database
                    response = 'Plant is already in the database'

#Add the plant to the database
            if delete is not True:
                transaction = Transactions.objects.create(timestamp=datetime.now(), users_id=request.user.id, transaction_type='INSERT', ignore=False)
                transaction.save()
                actions = []
                trans_type = 'INSERT'

                genus_id = ScientificName.objects.filter(value='genus').first()
                actions.append(Actions(transactions=transaction, action_type=trans_type, property='scientific_name', value=genus, scientific_names=genus_id))
                
                if species is not '':
                    species_id = ScientificName.objects.filter(value='species').first()
                    actions.append(Actions(transactions=transaction, action_type=trans_type, property='scientific_name', value=species, scientific_names=species_id))
                if variety is not '':
                    variety_id = ScientificName.objects.filter(value='variety').first()
                    actions.append(Actions(transactions=transaction, action_type=trans_type, property='scientific_name', value=variety, scientific_names=variety_id))   
                if subspecies is not '':
                    subspecies_id = ScientificName.objects.filter(value='subspecies').first()
                    actions.append(Actions(transactions=transaction, action_type=trans_type, property='scientific_name', value=subspecies, scientific_names=subspecies_id))
                if cultivar is not '':
                    cultivar_id = ScientificName.objects.filter(value='cultivar').first()
                    actions.append(Actions(transactions=transaction, action_type=trans_type, property='scientific_name', value=cultivar, scientific_names=cultivar_id))

                
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
            else:
                return JsonResponse({'error':response},status=400)


def viewPlants(request):
    if request.method == 'GET':
        plant_list = Plant.objects.all().order_by('common_name')
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


from itertools import chain
plant_search_results = {}
def search(request, searchString):
    #print(searchString)
    
    if not searchString:
        return redirect("/")
    
    plants = Plant.objects.all()
    full_scientific_name_results = []
    for p in plants:
        if p.get_scientific_name == searchString:
            full_scientific_name_results.append (p)

    layer_results = plants.filter(layer__in=Layer.objects.filter(value__icontains=searchString))
    food_results = plants.filter(food_prod__in=FoodProd.objects.filter(value__icontains=searchString))
    rawmat_results = plants.filter(raw_materials_prod__in=RawMaterialsProd.objects.filter(value__icontains=searchString))
    med_results = plants.filter(medicinals_prod__in=MedicinalsProd.objects.filter(value__icontains=searchString))
    biomed_results = plants.filter(biochemical_material_prod__in=BiochemicalMaterialProd.objects.filter(value__icontains=searchString))
    water_results = plants.filter(water_needs__in=WaterNeeds.objects.filter(value__icontains=searchString))
    sun_results = plants.filter(sun_needs__in=SunNeeds.objects.filter(value__icontains=searchString))
    nutrients_results = plants.filter(nutrient_requirements__in=NutrientRequirements.objects.filter(value__icontains=searchString))
    serotiny_results = plants.filter(serotiny__in=Serotiny.objects.filter(value__icontains=searchString))
    erosion_results = plants.filter(erosion_control__in=ErosionControl.objects.filter(value__icontains=searchString))
    insect_attract_results = plants.filter(plants_insect_attractor__in=Insects.objects.filter(value__icontains=searchString))
    insect_reg_results = plants.filter(plants_insect_regulator__in=Insects.objects.filter(value__icontains=searchString))
    
    
    common_name_results = plants.filter(common_name__icontains=searchString)

    #check to see if part of the search string matches part of the scientific name (to get similar results)
    results_list = list(chain(full_scientific_name_results, common_name_results, layer_results, food_results, rawmat_results, med_results, biomed_results, water_results, sun_results, nutrients_results, serotiny_results, erosion_results, insect_attract_results, insect_reg_results))

    searchStringSegments = searchString.split(" ")
    for s in searchStringSegments:
        #print(s)
        plant_scientific_name_results = PlantScientificName.objects.filter(value=s)
        #print("search results for sci name")
        for p in plant_scientific_name_results:
            #print(p.value)
            splants = Plant.objects.filter(id=p.plants.id)
            #print(splants)
            results_list = list(chain(results_list, splants))
            
    results_list = list(set(results_list))
    plant_search_results['plants'] = results_list

    print(len(results_list))
    # else:
#       results_list = list(chain(layer_results, food_results, rawmat_results, med_results, biomed_results, water_results, sun_results, nutrients_results, serotiny_results, erosion_results, insect_attract_results, insect_reg_results, common_name_results))
    #results_list = list(chain(layer_results, food_results, rawmat_results, med_results, biomed_results, serotiny_results, erosion_results, insect_attract_results, insect_reg_results))

    #results_list = list(name_matches)

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


def about(request):
    return render(request, 'frontend/about.html', {})


def dbstructure(request):
    return render(request, 'frontend/dbstructure.html', {})

def parent_transactions(p_id):
    # find the most recent transcations associated with the plant ID, and return the transaction ID of the transaction
    last_transaction = Transactions.objects.filter(plants_id = p_id).last()
    return last_transaction.id

def export_plant_data(request):
    # create a HttpResponse object
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Dispostion'] = 'attachment; filename = "export_plant_data.csv"'

    writer = csv.writer(response)

    writer.writerow(['Scientific Name', 'Family Name', 'Common Names', 'Endemic status to Southern California', 
                    'Duration of life', 'Height at maturity', 'Spread at maturity', 'pH range', 'Layer', 'Maximum canopy density', 
                    'Active growth period', 'Harvest period', 'Leaf retention', 'Primary flower color', 'Foliage color', 'Fruit Color', 
                    'Degree of serotiny', 'Shade tolerance', 'Salt tolerance', 'Flood tolerance', 'Drought tolerance', 'Humidity tolerance', 
                    'Wind tolerance', 'Soil drainage tolerance', 'Fire tolerance', 'Minimum temperature (ºF) tolerance', 'Nutrient requirements',
                    'Water requirements', 'Sun light requirements', 'Innoculant', 'Serotiny', 'Human food', 'Raw materials', 'Medicinal', 
                    'Biochemical material', 'Cultural and amenity', 'Nutrients added to soil', 'Allelochemicals', 'Erosion Control', 
                    'Insect attractor', 'Insect regulator', 'Animal attractor', 'Animal regulator', 'Toxicity to human and livestock'])	

    if plant_search_results == {}:
        all_plants = Plant.objects.all()
        for p in all_plants:
            height, spread = "", ""
            region = p.get_region
            if region is not None:
                height = region['height']
                spread = region['spread']

            pH_range = ""
            if p.pH_min != None and p.pH_max != None:
                pH_range += str(p.pH_min) + '-' + str(p.pH_max)

            writer.writerow([p.get_scientific_name, p.family, p.common_name, p.get_endemic_status, 
                             p.get_duration, height, spread, pH_range, p.get_layer, p.get_canopy_density, 
                             p.get_active_growth_period, p.get_harvest_period, p.get_leaf_retention, p.get_flower_color, p.get_foliage_color, p.get_fruit_color,
                             p.degree_of_serotiny, p.get_shade_tol, p.salt_tol, p.flood_tol, p.drought_tol, p.humidity_tol,
                             p.wind_tol, p.get_soil_drainage_tol, p.fire_tol, p.minimum_temperature_tol, p.get_nutrient_requirements,
                             p.get_water_needs, p.get_sun_needs, p.inoculant, p.serotiny, p.get_food_prod, p.get_raw_materials_prod, p.get_medicinals_prod,
                             p.get_biochemical_material_prod, p.get_cultural_and_amenity_prod, p.get_mineral_nutrients_prod, p.allelopathic, p.get_erosion_control,
                             p.get_plants_insect_attractor, p.get_plants_insect_regulator, p.get_plants_animal_attractor,  p.get_plants_animal_regulator, p.toxicity])
        
    else:
        for p in plant_search_results['plants']:
            height, spread = "", ""
            region = p.get_region
            if region is not None:
                height = region['height']
                spread = region['spread']

            pH_range = ""
            if p.pH_min != None and p.pH_max != None:
                pH_range += str(p.pH_min) + '-' + str(p.pH_max)

            writer.writerow([p.get_scientific_name, p.family, p.common_name, p.get_endemic_status, 
                             p.get_duration, height, spread, pH_range, p.get_layer, p.get_canopy_density, 
                             p.get_active_growth_period, p.get_harvest_period, p.get_leaf_retention, p.get_flower_color, p.get_foliage_color, p.get_fruit_color,
                             p.degree_of_serotiny, p.get_shade_tol, p.salt_tol, p.flood_tol, p.drought_tol, p.humidity_tol,
                             p.wind_tol, p.get_soil_drainage_tol, p.fire_tol, p.minimum_temperature_tol, p.get_nutrient_requirements,
                             p.get_water_needs, p.get_sun_needs, p.inoculant, p.serotiny, p.get_food_prod, p.get_raw_materials_prod, p.get_medicinals_prod,
                             p.get_biochemical_material_prod, p.get_cultural_and_amenity_prod, p.get_mineral_nutrients_prod, p.allelopathic, p.get_erosion_control,
                             p.get_plants_insect_attractor, p.get_plants_insect_regulator, p.get_plants_animal_attractor,  p.get_plants_animal_regulator, p.toxicity])
        
        plant_search_results.clear()
    return response