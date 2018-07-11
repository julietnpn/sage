from django.core.management.base import BaseCommand, CommandError
from plants.models import *
from frontend.models import Actions, Transactions
from login.models import AuthUser
import csv

class Command(BaseCommand):
	
	def handle(self, *args, **options):
		path1=r'/Users/matthew/Desktop/programming projects/django/SAGE/sage/plants/management/csvdata/ICS5_2015.csv'
		
		user = AuthUser.objects.get(username='ICS5')
	
		csv_import(path1, user)

scientific_names_list = []
transaction_list = []

properties_1_to_1 = ['common_name',
					 'drought_tol_id',
					 'flood_tol_id',
					 'humidity_tol_id',
					 'salt_tol_id',
					 'toxin_removal_id',
					 'wind_tol_id',
					 'minimum_temperature_tol',
					 'inoculant',
					 'fire_tol_id',
					 'livestock_bloat_id',
					 'pH_min',
					 'pH_max',
					 'toxicity_id',
					 'lifespan_id',
					 'allelopathic_id',
					 'tags',
					 'allelochemicals',
					 'serotiny_id',
					 'degree_of_serotiny_id',
					 'family_id',
					 'family_common_name_id']

properties_many_with_region = ['active_growth_period',
							   'animal_attractor',
							   'animal_regulator',
							   'barrier',
							   'canopy_density',
							   'duration',
							   'endemic_status',
							   'erosion_control',
							   'nutrient_requirements',
							   'harvest_period',
							   'height_at_maturity',
							   'insect_attractor',
							   'insect_regulator',
							   'leaf_retention',
							   'shade_tol',
							   'soil_drainage_tol',
							   'spread_at_maturity',
							   'sun_needs',
							   'water_needs']
								
properties_1_to_many = ['family',
						'family_common_name',
						]

properties_scientific_name = ['scientific_name']

properties_many_to_many = ['biochemical_material_prod',
						   'cultural_and_amenity_prod',
						   'flower_color',
						   'foliage_color',
						   'food_prod',
						   'animal_food',
						   'fruit_color',
						   'layer',
						   'medicinals_prod',
						   'mineral_nutrients_prod',
						   'raw_materials_prod'
						   ]

def csv_import(path, user):
	with open(path) as f:
		reader = csv.DictReader(f)
		for i,plant in enumerate(reader):
			trans_type = 'INSERT'
			actions = []

			if not(plant['Scientific Name']):
				continue
			print(i, plant['Scientific Name'], len(plant['Scientific Name']))

			scientific_name = ''
			genus = ''
			speces = '' 
			variety = ''
			subspecies = ''
			cultivar = ''

			scientific_name = plant['Scientific Name']
			if 'spp.' in scientific_name:
				if scientific_name.endswith('spp.'):
					print("spp only, delete transaction")
					continue
				else:
					sciname_bits= scientific_name.split()
					found = False
					for i in sciname_bits:
						if "spp." in i:
							found = True
						if found:
							subspecies = i
							continue
			if ' x ' in scientific_name:
				sciname_bits= scientific_name.split()
				genus = sciname_bits[0] + " x " + sciname_bits[2]
				species = ''
			if "'" in scientific_name:
				sciname_bits= scientific_name.split()
				for i in sciname_bits:
					if i.startswith("'") and i.endswith("'"):
						cultivar = i
						if i<2 and genus is None:
							genus = sciname_bits[0]
							species = ''
			if 'var. ' in scientific_name:
				sciname_bits= scientific_name.split()
				found = False
				for i in sciname_bits:
					if "Var. " or "var. " in i:
						found = True
					if found:
						variety = i
						continue
			if genus is '':
				sciname_bits = scientific_name.split()
				genus = sciname_bits[0]
				if len(sciname_bits) > 1:
					species = sciname_bits[1]
				else:
					print("genus only, delete transaction")
					continue
			
			#check if this scientific name is already in the database
			#if scientific name has already been added, then this should be an update transaction, not an insert
			whole_db_scientific_name = genus + species + subspecies + variety + cultivar
			if whole_db_scientific_name in scientific_names_list:
				trans_type = 'UPDATE'
				s_index =scientific_names_list.index(whole_db_scientific_name)
				print("index in scientific names list: ", s_index)
				print("transaction id of that index: ", transaction_list[s_index])
				plantobject = next((p for p in Plant.objects.all() if p.getScientificName == whole_db_scientific_name), None)
				transaction = Transactions.objects.create(users_id=user.id, transaction_type=trans_type, plants_id = plantobject.id, ignore=False)#because the transactions haven't been processed and Plants haven't been created, we need to keep track of which plant this is an update to. I'm saving the transaction id of the INSERT plant to the plants_id of the Update plant. In process_transactions I will use the transaction_id stored in plants_id to look it up.
			else:
				transaction = Transactions.objects.create(users_id=user.id, transaction_type=trans_type, ignore=False)# not always Update
			
			scientific_names_list.append(whole_db_scientific_name)
			transaction_list.append(transaction.id)
			
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


			if plant['Family Name'].strip():
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='family', value=plant['Family Name'].strip()))

			if plant['Common Names'].strip():
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='common_name', value=plant['Common Names'].strip()))

			if plant['Endemic status to Southern California'].strip():
				endemic_status_id = EndemicStatus.objects.filter(value=plant['Endemic status to Southern California'].strip().lower()).first().id
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='endemic_status', value=endemic_status_id))

			if plant['Duration of life'].strip():
				duration_id = Duration.objects.filter(value=plant['Duration of life'].strip().lower()).first().id
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='duration', value=duration_id))

			if plant['Layer'].strip():
				layer_id = Layer.objects.filter(value=plant['Layer'].strip()).first().id
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='layer', value=layer_id))

			if plant['Maximum canopy density'].strip():
				canopy_density_id = CanopyDensity.objects.filter(value=plant['Maximum canopy density'].strip()).first().id
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='canopy_density', value=canopy_density_id))

			if plant['Leaf retention'].strip():
				leaf_retention_id = LeafRetention.objects.filter(value=plant['Leaf retention'].strip()).first().id
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='leaf_retention', value=leaf_retention_id))

			if plant['Primary flower color'].strip():
				flower_color_id = FlowerColor.objects.filter(value=plant['Primary flower color'].strip().lower()).first().id
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='flower_color', value=flower_color_id))

			if plant['Foliage color'].strip():
				foliage_color_id = FoliageColor.objects.filter(value=plant['Foliage color'].strip().lower()).first().id
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='foliage_color', value=foliage_color_id))

			if plant['Fruit color (when ripe)'].strip():
				fruit_color_id = FruitColor.objects.filter(value=plant['Fruit color (when ripe)'].strip().lower()).first().id
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='fruit_color', value=fruit_color_id))

			if plant['Degree of serotiny'].strip():
				degree_of_serotiny = plant['Degree of serotiny'].strip()
				if 'strongly serotinous' in degree_of_serotiny:
					degree_of_serotiny_id = DegreeOfSerotiny.objects.filter(value='strongly serotinous').first().id
					actions.append(Actions(transactions=transaction, action_type=trans_type, property='degree_of_serotiny', value=degree_of_serotiny_id))
				elif 'weakly serotinous' in degree_of_serotiny:
					degree_of_serotiny_id = DegreeOfSerotiny.objects.filter(value='weakly serotinous').first().id
					actions.append(Actions(transactions=transaction, action_type=trans_type, property='degree_of_serotiny', value=degree_of_serotiny_id))
				elif 'facultatively serotinous' in degree_of_serotiny:
					degree_of_serotiny_id = DegreeOfSerotiny.objects.filter(value='facultatively serotinous').first().id
					actions.append(Actions(transactions=transaction, action_type=trans_type, property='degree_of_serotiny', value=degree_of_serotiny_id))
				elif 'non-serotinous' in degree_of_serotiny:
					degree_of_serotiny_id = DegreeOfSerotiny.objects.filter(value='non-serotinous').first().id
					actions.append(Actions(transactions=transaction, action_type=trans_type, property='degree_of_serotiny', value=degree_of_serotiny_id))

			if plant['Shade tolerance'].strip():
				shade_tol = plant['Shade tolerance'].split(',')
				for st in shade_tol:
					st_id = ShadeTol.objects.filter(value=st.strip()).first().id
					actions.append(Actions(transactions=transaction, action_type=trans_type, property='shade_tol', value=st_id))

			if plant['Salt tolerance'].strip():
				salt_tol = plant['Salt tolerance'].strip()
				if 'moderately salt-tolerant' in salt_tol:
					salt_told_id = SaltTol.objects.filter(value='moderately salt-tolerant').first().id
					actions.append(Actions(transactions=transaction, action_type=trans_type, property='salt_tol', value=salt_told_id))
				elif 'slightly salt-tolerant' in salt_tol:
					salt_told_id = SaltTol.objects.filter(value='slightly salt-tolerant').first().id
					actions.append(Actions(transactions=transaction, action_type=trans_type, property='salt_tol', value=salt_told_id))
				elif 'not salt-tolerant' in salt_tol:
					salt_told_id = SaltTol.objects.filter(value='not salt-tolerant').first().id
					actions.append(Actions(transactions=transaction, action_type=trans_type, property='salt_tol', value=salt_told_id))
				elif 'salt-tolerant' in salt_tol:
					salt_told_id = SaltTol.objects.filter(value='salt-tolerant').first().id
					actions.append(Actions(transactions=transaction, action_type=trans_type, property='salt_tol', value=salt_told_id))
	
			if plant['Flood tolerance'].strip():
				flood_tol = plant['Flood tolerance'].strip()
				if 'moderately flood-tolerant' in flood_tol:
					flood_tol_id = FloodTol.objects.filter(value='moderately flood-tolerant').first().id
					actions.append(Actions(transactions=transaction, action_type=trans_type, property='flood_tol', value=flood_tol_id))
				elif 'not flood-tolerant' in flood_tol:
					flood_tol_id = FloodTol.objects.filter(value='not flood-tolerant').first().id
					actions.append(Actions(transactions=transaction, action_type=trans_type, property='flood_tol', value=flood_tol_id))
				elif 'flood-tolerant' in flood_tol:
					flood_tol_id = FloodTol.objects.filter(value='flood-tolerant').first().id
					actions.append(Actions(transactions=transaction, action_type=trans_type, property='flood_tol', value=flood_tol_id))

			if plant['Drought tolerance'].strip():
				drought_tol = plant['Drought tolerance'].strip()
				if 'moderately drought-tolerant' in drought_tol:
					drought_tol_id = DroughtTol.objects.filter(value='moderately drought-tolerant').first().id
					actions.append(Actions(transactions=transaction, action_type=trans_type, property='drought_tol', value=drought_tol_id))
				elif 'not drought-tolerant' in drought_tol:
					drought_tol_id = DroughtTol.objects.filter(value='not drought-tolerant').first().id
					actions.append(Actions(transactions=transaction, action_type=trans_type, property='drought_tol', value=drought_tol_id))
				elif 'drought-tolerant' in drought_tol:
					drought_tol_id = DroughtTol.objects.filter(value='drought-tolerant').first().id
					actions.append(Actions(transactions=transaction, action_type=trans_type, property='drought_tol', value=drought_tol_id))

			if plant['Humidity tolerance'].strip():
				humidity_tol = plant['Humidity tolerance'].strip()
				if 'moderately humidity-tolerant' in humidity_tol:
					humidity_tol_id = HumidityTol.objects.filter(value='moderately humidity-tolerant').first().id
					actions.append(Actions(transactions=transaction, action_type=trans_type, property='humidity_tol', value=humidity_tol_id))
				elif 'not humidity-tolerant' in humidity_tol:
					humidity_tol_id = HumidityTol.objects.filter(value='not humidity-tolerant').first().id
					actions.append(Actions(transactions=transaction, action_type=trans_type, property='humidity_tol', value=humidity_tol_id))
				elif 'humidity-tolerant' in humidity_tol:
					humidity_tol_id = HumidityTol.objects.filter(value='humidity-tolerant').first().id
					actions.append(Actions(transactions=transaction, action_type=trans_type, property='humidity_tol', value=humidity_tol_id))
					
			Actions.objects.bulk_create(actions)