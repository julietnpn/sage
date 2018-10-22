from django.core.management.base import BaseCommand, CommandError
from plants.models import *
from frontend.models import Actions, Transactions
from login.models import AuthUser
import csv

#Note, after running restorecsv, you must run process_transactions for changes to reflect in the database.
class Command(BaseCommand):

	def handle(self, *args, **options):
		self.stdout.write("restorecsv!!!")

		print('Flushing actions table...')
		Actions.objects.all().delete()
		print('Flushing transactions table...')
		Transactions.objects.all().delete()



		path1=r'plants/management/csvdata/TEC_for_import.csv'
		#Common Name,Scientific Name,Type of plant,Height range
		path2=r'plants/management/csvdata/usda.orange.for_import.csv'
		#Scientific Name,Common Name,Genus,Family,Family Common Name,Duration,Growth Habit,Fact Sheets,Plant Guides,Characteristics Data,Cultivar Name,Active Growth Period,Bloat,Coppice Potential,Fire Resistance,Flower Color,Flower Conspicuous,Foliage Color,Foliage Porosity Summer,Fruit Color,Fruit Conspicuous,"Height, Mature (feet)",Known Allelopath,Leaf Retention,Lifespan,Nitrogen Fixation,Shape and Orientation,Toxicity,Drought Tolerance,Fertility Requirement,Moisture Use,pH (Minimum),pH (Maximum),Salinity Tolerance,Shade Tolerance,Fruit/Seed Period End,Berry/Nut/Seed Product,Christmas Tree Product,Fodder Product,Fuelwood Product,Lumber Product,Naval Store Product,Post Product,Pulpwood Product,Veneer Product
		path3=r'plants/management/csvdata/plantdb_export_zone10.csv'
		#ID,Name,Scientific name,Plant Type,Height,Spread,Root Depth,Seasonal Interest,Notes,Flower Color,Root Type,Bloom Time,Fruit Time,Texture,Form,Growth Rate,Insect Predation,Disease,Light,Hardiness Zone,Soil Moisture,Soil pH,Ecological Function,Human Use/Crop

		user1 = AuthUser.objects.get(username='TEC_PDC_2014')
		user3 = AuthUser.objects.get(username='Natural_Capital')
		user2 = AuthUser.objects.get(username='USDA')
		
		
		#only import one file at a time so you don't have duplicates
		csv_import1(path1, user1)
		csv_import3(path3, user3)
		csv_import2(path2, user2)

		
	
	
	
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
                     'degree_of_serotiny_id',# add family here?!?!
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
                                ######################################################
#-------------------------------------- TODO should add serotiny and degree of serotiny--------------------------
								######################################################
properties_1_to_many = ['family',
                        'family_common_name',#-----the_family
                        ]
                        #'tags']
properties_scientific_name = [# 'genus', #add _id for foreign keys
#                      		  'species',
#                      		  'subspecies',
#                      		  'variety',
#                      		  'form',
#                      		  'cutivar',
                     		  'scientific_name'
                     		 ]

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
						   

#--------------------------------------The Ecology Center - Plant List-------------
#written by Moin
#updated by Juliet on 7/27/2016
def csv_import1(path1, user):
	print("CSV Import 1")
	with open(path1) as f:
		reader = csv.DictReader(f)    
		for i,plant in enumerate(reader):
			trans_type = 'INSERT'
			# print(transaction.id)
			actions = []
			if not(plant['Scientific Name']):
				continue
			if len(plant['Scientific Name'].split()) < 2:
				continue

			print(i,plant['Scientific Name'])

			# try:
# 				plant_id = Plant.objects.filter(genus=plant['Scientific Name'].split()[0]).first().id
# 				transaction.plants_id=plant_id
# 				transaction.transaction_type = 'UPDATE'
# 				transaction.save()
# 			except AttributeError:
# 				pass
				
			scientific_name = ''
			genus = ''
			species = ''
			variety = ''
			subspecies = ''
			cultivar = ''
			
			scientific_name = plant['Scientific Name']
			# TODO what about var. in scientific name
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
				for i in sciname_bits: #make sure it is not a genus with a cultivar
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
				#genus has not been defined and needs to be defined
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
				transaction = Transactions.objects.create(users_id=user.id, transaction_type=trans_type, parent_transaction=transaction_list[s_index], ignore=False)#because the transactions haven't been processed and Plants haven't been created, we need to keep track of which plant this is an update to. I'm saving the transaction id of the INSERT plant to the parent_transactions of the Update plant. In process_transactions I will use the transaction_id stored in plants_id to look it up.
			else:
				transaction = Transactions.objects.create(users_id=user.id, transaction_type=trans_type, ignore=False)# not always Update
			
			
			scientific_names_list.append(whole_db_scientific_name)
			transaction_list.append(transaction.id)
			
			#genus_id = ScientificName.objects.filter(value='genus').first()
			
			actions.append(Actions(transactions=transaction, action_type=trans_type, property='scientific_name', value=genus, category="genus"))
			
			if species is not '':
				#species_id = ScientificName.objects.filter(value='species').first()
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='scientific_name', value=species, category="species"))
			if variety is not '':
				#variety_id = ScientificName.objects.filter(value='variety').first()
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='scientific_name', value=variety, category="variety"))	
			if subspecies is not '':
				#subspecies_id = ScientificName.objects.filter(value='subspecies').first()
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='scientific_name', value=subspecies, category="subspecies"))
			if cultivar is not '':
				#cultivar_id = ScientificName.objects.filter(value='cultivar').first()
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='scientific_name', value=cultivar, category="cultivar"))

			if plant['Common Name'].strip():
				actions.append(Actions(transactions=transaction , action_type=trans_type, property='common_name', value=plant['Common Name'].strip()))

			Actions.objects.bulk_create(actions)

#---------------------------------------------plantdb_export (zone 10 drought)_2.csv----
#updated by Juliet on 7/26/2016
#written by Moin
def csv_import3(path, user):
	print("CSV Import 3")
	with open(path, 'r') as f:
		reader = csv.DictReader(f)
		for i,plant in enumerate(reader):
			trans_type = 'INSERT'
			# print(i,plant['Name']):
			# print(transaction.id)
			actions = []
			if not(plant['Scientific Name']):
				continue
			#if len(plant['Scientific Name'].split()) < 2:
			#	continue

			
			print(i,plant['Scientific Name'], len(plant['Scientific Name']))

			scientific_name = ''
			genus = ''
			species = ''
			variety = ''
			subspecies = ''
			cultivar = ''
			
			scientific_name = plant['Scientific Name']
			# TODO what about var. in scientific name
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
						if len(sciname_bits)<2 and genus is None:
							genus = sciname_bits[0]
							species = ''
			if 'var. ' in scientific_name:
				sciname_bits= scientific_name.split()
				found = False
				for i in sciname_bits:
					if "Var. " or "var. " in i:
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
					continue
			
			
			#check if this scientific name is already in the database
			#if scientific name has already been added, then this should be an update transaction, not an insert
			whole_db_scientific_name = genus + species + subspecies + variety + cultivar
			if whole_db_scientific_name in scientific_names_list:
				trans_type = 'UPDATE'
				s_index =scientific_names_list.index(whole_db_scientific_name)
				print("index in scientific names list: ", s_index)
				print("transaction id of that index: ", transaction_list[s_index])
				transaction = Transactions.objects.create(users_id=user.id, transaction_type=trans_type, parent_transaction=transaction_list[s_index], ignore=False)#because the transactions haven't been processed and Plants haven't been created, we need to keep track of which plant this is an update to. I'm saving the transaction id of the INSERT plant to the plants_id of the Update plant. In process_transactions I will use the transaction_id stored in plants_id to look it up.
			else:
				transaction = Transactions.objects.create(users_id=user.id, transaction_type=trans_type, ignore=False)# not always Update
			
			
			scientific_names_list.append(whole_db_scientific_name)
			transaction_list.append(transaction.id)
			
			#plant_species_results=PlantScientificName.objects.filter(value=species)
			#plant_variety_results=PlantScientificName.objects.filter(value=variety)
			#plant_subspecies_results=PlantScientificName.objects.filter(value=subspecies)
			#plant_cultivar_results=PlantScientificName.objects.filter(value=cultivar)
			
			
			#genus_id = ScientificName.objects.filter(value='genus').first()
			actions.append(Actions(transactions=transaction, action_type=trans_type, property='scientific_name', value=genus, category="genus"))

			
			if species is not '':
				#species_id = ScientificName.objects.filter(value='species').first()
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='scientific_name', value=species, category="species"))
			if variety is not '':
				#variety_id = ScientificName.objects.filter(value='variety').first()
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='scientific_name', value=variety, category="variety"))	
			if subspecies is not '':
				#subspecies_id = ScientificName.objects.filter(value='subspecies').first()
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='scientific_name', value=subspecies, category="subspecies"))
			if cultivar is not '':
				#cultivar_id = ScientificName.objects.filter(value='cultivar').first()
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='scientific_name', value=cultivar, category="cultivar"))



			if plant['Common Name'].strip():
				actions.append(Actions(transactions=transaction , action_type=trans_type, property='common_name', value=plant['Common Name'].strip()))

			if plant['Plant Type'].strip(): # assuming we don't have multiple layers/duration/leaf_retention in one entry
				#def layer, duration, leaf_retention = False
				if plant['Plant Type']=='Deciduous Shrub':
					layer = 'shrub'
					duration = 'perennial'
					leaf_retention = 'deciduous'
				elif plant['Plant Type']=='Evergreen Tree':
					layer = 'climax'
					duration = 'perennial'
					leaf_retention = 'evergreen'
				elif plant['Plant Type']=='Perennial':
					duration = 'perennial'
				elif plant['Plant Type']=='Evergreen Shrub':
					layer = 'shrub'
					duration = 'perennial'
					leaf_retention = 'evergreen'
				elif plant['Plant Type']=='Annual':
					duration = 'annual'
				elif plant['Plant Type']=='Deciduous Tree':
					layer = 'climax'
				elif plant['Plant Type']=='Grass':
					layer = 'ground cover'
				elif plant['Plant Type']=='Vine':
					layer = 'climber'
				elif plant['Plant Type']=='Fern':
					layer = 'shrub'
				elif plant['Plant Type']=='Biennial':
					duration = 'biennial'
				elif plant['Plant Type']=='Aquatic':
					layer = 'aquatic'
				else:
					raise ValueError('Can not recognize Plant Type = ' + plant['Plant Type'])

				try:
					leaf_retention_id = LeafRetention.objects.filter(value=leaf_retention).first().id
					actions.append(Actions(transactions=transaction, action_type=trans_type, property='leaf_retention', value=leaf_retention_id))
				except UnboundLocalError:
					pass
				try:
					layer_id = Layer.objects.filter(value=layer).first().id
					actions.append(Actions(transactions=transaction, action_type=trans_type, property='layer', value=layer_id))
				except (UnboundLocalError, AttributeError) as e:
					pass
				try:
					duration_id = Duration.objects.filter(value=duration).first().id
					actions.append(Actions(transactions=transaction, action_type=trans_type, property='duration', value=duration_id))
				except UnboundLocalError:
					pass	

			if plant['Height'].strip():
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='height', value=float(plant['Height'].strip())))
			if plant['Spread'].strip():
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='spread', value=float(plant['Spread'].strip())))
			if plant['Root Depth'].strip():
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='root_depth', value=float(plant['Root Depth'].strip())))
			if plant['Flower Color'].strip():
				colors=plant['Flower Color'].split(',')
				for color in colors:
					flower_color_id = FlowerColor.objects.filter(value=color.strip().lower()).first().id
					actions.append(Actions(transactions=transaction, action_type=trans_type, property='flower_color', value=flower_color_id))

			if plant['Fruit Time'].strip():
				seasons = []
				harvest_periods = plant['Fruit Time'].strip().lower()
				if 'fall'in harvest_periods or 'autumn' in harvest_periods:
					seasons.append('autumn')
				if 'winter' in harvest_periods:
					seasons.append('winter')
				if 'spring' in harvest_periods:
					seasons.append('spring')
				if 'summer' in harvest_periods:
					seasons.append('summer')
				# if plant['Fruit/Seed Period End'].strip() == 'Year Round':# or All Year
				# 	seasons.append('autumn')
				# 	seasons.append('winter')
				# 	seasons.append('spring')
				# 	seasons.append('summer')
				# else:
				# 	print(plant['Fruit/Seed Period End'].strip())
				# 	# raise ValueError('Need to add handling for Fruit/Seed Period End = ' + plant['Fruit/Seed Period End'].strip())

				for season in seasons:
					harvest_period_id = HarvestPeriod.objects.filter(value=season).first().id
					actions.append(Actions(transactions=transaction, action_type=trans_type, property='harvest_period', value=harvest_period_id))

			if plant['Light']:
				lights = plant['Light'].strip()
				if 'Full_Sun' in lights:
					sun_need_id = SunNeeds.objects.filter(value='full sun').first().id
					actions.append(Actions(transactions=transaction, action_type=trans_type, property='sun_needs', value=sun_need_id))
				if 'Partial_Shade' in lights:
					shade_tol_id = ShadeTol.objects.filter(value='partial shade').first().id
					actions.append(Actions(transactions=transaction, action_type=trans_type, property='shade_tol', value=shade_tol_id))
				if 'Shade' in lights:
					shade_tol_id = ShadeTol.objects.filter(value='permanent shade').first().id
					actions.append(Actions(transactions=transaction, action_type=trans_type, property='shade_tol', value=shade_tol_id))

			if plant['Soil Moisture']:
				soils = plant['Soil Moisture'].strip()
				if 'Wet' in soils:
					soil_drainage_tol_id = SoilDrainageTol.objects.filter(value='poor-drainage tolerant').first().id
					actions.append(Actions(transactions=transaction, action_type=trans_type, property='soil_drainage_tol', value=soil_drainage_tol_id))
				if 'Moderate' in soils:
					soil_drainage_tol_id = SoilDrainageTol.objects.filter(value='moderate-drainage tolerant').first().id
					actions.append(Actions(transactions=transaction, action_type=trans_type, property='soil_drainage_tol', value=soil_drainage_tol_id))
				if 'Dry' in soils:
					soil_drainage_tol_id = SoilDrainageTol.objects.filter(value='excessively-drained tolerant').first().id
					actions.append(Actions(transactions=transaction, action_type=trans_type, property='soil_drainage_tol', value=soil_drainage_tol_id))

			if plant['Soil pH']:
				actions.append(Actions(transactions=transaction , action_type=trans_type, property='pH_min', value=float(plant['Soil pH'].strip()[:3])))
				actions.append(Actions(transactions=transaction , action_type=trans_type, property='pH_max', value=float(plant['Soil pH'].strip()[6:])))

			if plant['Ecological Function']:
				ecos = plant['Ecological Function'].strip()#.lower()
				barrier_ids = []
				if 'Chemical Barrier' in ecos:
					barrier_ids += [Barrier.objects.filter(value='chemical').first().id]
				if 'Hedge' in ecos:
					barrier_ids += [Barrier.objects.filter(value='hedge').first().id]
				if 'Windbreak' in ecos:
					barrier_ids += [Barrier.objects.filter(value='windbreak').first().id]
				for barrier_id in barrier_ids:
					actions.append(Actions(transactions=transaction, action_type=trans_type, property='barrier', value=barrier_id))
				
				if 'Erosion Control' in ecos:
					erosion_control_id = ErosionControl.objects.filter(value='medium').first().id
					actions.append(Actions(transactions=transaction, action_type=trans_type, property='erosion_control', value=erosion_control_id))
				if 'Domestic Animal Forage' in ecos:
					animal_food_id = AnimalFood.objects.filter(value='domestic').first().id
					actions.append(Actions(transactions=transaction, action_type=trans_type, property='animal_food', value=animal_food_id))
				if 'Groundcover' in ecos:
					layer_id = Layer.objects.filter(value='ground cover').first().id
					actions.append(Actions(transactions=transaction, action_type=trans_type, property='layer', value=layer_id))
				if 'Wildlife Food' in ecos:
					animal_food_id = AnimalFood.objects.filter(value='wild').first().id
					actions.append(Actions(transactions=transaction, action_type=trans_type, property='animal_food', value=animal_food_id))
				if 'Mulch Maker' in ecos:
					raw_materials_prod_id = RawMaterialsProd.objects.filter(value='biomass').first().id
					actions.append(Actions(transactions=transaction, action_type=trans_type, property='raw_materials_prod', value=raw_materials_prod_id))
				if 'Nitrogen Fixer' in ecos:
					mineral_nutrients_prod_id = MineralNutrientsProd.objects.filter(value='nitrogen').first().id
					actions.append(Actions(transactions=transaction, action_type=trans_type, property='mineral_nutrients_prod', value=mineral_nutrients_prod_id))

			if plant['Human Use/Crop']:
				human_uses = plant['Human Use/Crop'].strip()#.lower()
				if 'Biomass' in human_uses:
					raw_materials_prod_id = RawMaterialsProd.objects.filter(value='biomass').first().id
					actions.append(Actions(transactions=transaction, action_type=trans_type, property='raw_materials_prod', value=raw_materials_prod_id))
				if 'Cleanser/Scourer' in human_uses or 'Soap' in human_uses:
					biochemical_material_prod_id = BiochemicalMaterialProd.objects.filter(value='detergents').first().id
					actions.append(Actions(transactions=transaction, action_type=trans_type, property='biochemical_material_prod', value=biochemical_material_prod_id))
				if 'Cut Flower' in human_uses or 'Ornamental' in human_uses:
					cultural_and_amenity_prod_id = CulturalAndAmenityProd.objects.filter(value='aesthetic').first().id
					actions.append(Actions(transactions=transaction, action_type=trans_type, property='cultural_and_amenity_prod', value=cultural_and_amenity_prod_id))
				if 'Dye' in human_uses:
					raw_materials_prod_id = RawMaterialsProd.objects.filter(value='dye').first().id
					actions.append(Actions(transactions=transaction, action_type=trans_type, property='raw_materials_prod', value=raw_materials_prod_id))
				if 'Essential Oil' in human_uses:
					raw_materials_prod_id = RawMaterialsProd.objects.filter(value='essential oil').first().id
					actions.append(Actions(transactions=transaction, action_type=trans_type, property='raw_materials_prod', value=raw_materials_prod_id))
				if 'Fiber' in human_uses:
					raw_materials_prod_id = RawMaterialsProd.objects.filter(value='fiber').first().id
					actions.append(Actions(transactions=transaction, action_type=trans_type, property='raw_materials_prod', value=raw_materials_prod_id))
				if 'Insect Repellent' in human_uses:
					medicinals_prod_id = MedicinalsProd.objects.filter(value='insect repellent').first().id
					actions.append(Actions(transactions=transaction, action_type=trans_type, property='medicinals_prod', value=medicinals_prod_id))
				if 'Wood' in human_uses:
					raw_materials_prod_id = RawMaterialsProd.objects.filter(value='timber').first().id
					actions.append(Actions(transactions=transaction, action_type=trans_type, property='raw_materials_prod', value=raw_materials_prod_id))

			Actions.objects.bulk_create(actions)

#----------------------------usda.orange.for_import
def csv_import2(path, user):############################serotiny, degree_of_serotiny, allelochemicals######

	print("CSV Import 2")
	with open(path) as f:
		reader = csv.DictReader(f)#csv.reader(f)    
		for i,plant in enumerate(reader):
			# print(i,plant['Name']):
			trans_type = 'INSERT'
			# print(transaction.id)
			actions = []
			if not(plant['Scientific Name']):
				continue
			#if len(plant['Scientific Name'].split()) < 2:
			#	continue

			# try:
# 				plant_id = Plant.objects.filter(genus=plant['Scientific Name'].split()[0]).first().id
# 				transaction.plants_id=plant_id
# 				trans_type = 'UPDATE'
# 				transaction.transaction_type = trans_type
# 				transaction.save()
# 			except AttributeError:
# 				pass
			
			#print(trans_type)
			print(i,plant['Scientific Name'], len(plant['Scientific Name']))

			scientific_name = ''
			genus = ''
			species = ''
			variety = ''
			subspecies = ''
			cultivar = ''
			
			scientific_name = plant['Scientific Name']
			# TODO what about var. in scientific name
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
			if 'var. ' or 'Var. ' in scientific_name:
				sciname_bits= scientific_name.split()
				found = False
				for i in sciname_bits:
					if "Var. " or "var. " in i:
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
					continue
			
			#  Cultivar has its own column in the USDA CSV file
			if plant['Cultivar Name'].strip():
				cultivar = plant['Cultivar Name'].strip()
			
			#check if this scientific name is already in the database
			#if scientific name has already been added, then this should be an update transaction, not an insert
			whole_db_scientific_name = genus + species + subspecies + variety + cultivar
			if whole_db_scientific_name in scientific_names_list:
				trans_type = 'UPDATE'
				s_index =scientific_names_list.index(whole_db_scientific_name)
				print("index in scientific names list: ", s_index)
				print("transaction id of that index: ", transaction_list[s_index])
				transaction = Transactions.objects.create(users_id=user.id, transaction_type=trans_type, parent_transaction=transaction_list[s_index], ignore=False)#because the transactions haven't been processed and Plants haven't been created, we need to keep track of which plant this is an update to. I'm saving the transaction id of the INSERT plant to the parent_transaction of the Update plant. In process_transactions I will use the transaction_id stored in plants_id to look it up.
			else:
				transaction = Transactions.objects.create(users_id=user.id, transaction_type=trans_type, ignore=False)# not always Update
			
			
			scientific_names_list.append(whole_db_scientific_name)
			transaction_list.append(transaction.id)
			
			#genus_id = ScientificName.objects.filter(value='genus').first()
			actions.append(Actions(transactions=transaction, action_type=trans_type, property='scientific_name', value=genus, category="genus"))
			
			if species is not '':
				#species_id = ScientificName.objects.filter(value='species').first()
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='scientific_name', value=species, category="species"))
			if variety is not '':
				#variety_id = ScientificName.objects.filter(value='variety').first()
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='scientific_name', value=variety, category="variety"))	
			if subspecies is not '':
				#subspecies_id = ScientificName.objects.filter(value='subspecies').first()
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='scientific_name', value=subspecies, category="subspecies"))
			if cultivar is not '':
				#cultivar_id = ScientificName.objects.filter(value='cultivar').first()
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='scientific_name', value=cultivar, category="cultivar"))



			if plant['Common Name'].strip():
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='common_name', value=plant['Common Name'].strip()))

# No family common name in this file
# 			3. add field for Family Common Name
# 			what if the name is not in the famile tables... handle it!
# 			if plant['Family Common Name'].strip():
# 				if TheFamilyCommonName.objects.filter(value=plant['Family Common Name'].strip()):
# 					family_common_name_id = TheFamilyCommonName.objects.filter(value=plant['Family Common Name'].strip()).first().id
# 					actions.append(Actions(transactions=transaction, action_type=trans_type, property='family_common_name_id', value=family_common_name_id))
# 				
			# 4. add field for Family
			# what if the name is not in the famile tables... handle it!
			if plant['Family'].strip():
				if TheFamily.objects.filter(value=plant['Family'].strip()):
					family_id = TheFamily.objects.filter(value=plant['Family'].strip()).first().id
					actions.append(Actions(transactions=transaction, action_type=trans_type, property='family_id', value=family_id))

			# 5. duration = duration
			durations = []
			if 'Perennial' in plant['Duration']:
				durations.append('perennial')
			if 'Annual' in plant['Duration']:
				durations.append('annual')
			if 'Biennial' in plant['Duration']:
				durations.append('biennial')
			for duration in durations:
				# s = TheFamily.objects.get(id=415)
				duration_id = Duration.objects.filter(value=duration).first().id #####################
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='duration', value=duration_id))

			# 6. Growth Habit data is mapped to Layer (ALSO IMPLEMENTS #23)
			#    Forb/herb translates to herb
			#    Vine translates to climber
			#    Graminoid translates to ground cover
			#    Tree translates to understory and climax
			#    Subshrub translates to shrub
			growth_habit_map = {'Forb/herb': {'herb'},
					'Vine': {'climber'},
					'Graminoid': {'ground cover'},
					'Tree': {'understory', 'climax'},
					'Shrub': {'shrub'},
					'Subshrub': {'shrub'}}
			shape_and_orientation_map = {'Prostrate': {'ground cover'},
							 'Climbing': {'climber'},
							 'Decumbent': {'ground cover', 'herb'}}
			values_to_store = set() ################################################################TODO
			# if plant['Growth Habit'].strip():
			#    values_to_store.union(growth_habit_map[plant['Growth Habit'].strip()])
			# if plant['Shape and Orientation'].strip():
			#    values_to_store.union(shape_and_orientation_map[plant['Shape and Orientation'].strip()])
			# for value in values_to_store:
			#    layer_id = Layer.objects.filter(value=value).first().id
			#    actions.append(Actions(transactions=transaction, action_type=trans_type, property='layer', value=layer_id))

			# 7. Urls found in Fact Sheets and Plant Guides should be stored into the url tags
			if plant['Fact Sheets'].strip():
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='tags', value=plant['Fact Sheets'].strip()))
			if plant['Plant Guides'].strip():
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='tags', value=plant['Plant Guides'].strip()))

			# 8. You only have to fill in the remaining data for the plant if Characteristics Data = yes
			#    (i.e., you can move on to the next entry if it does not say yes).
			if plant['Characteristics Data'].strip() != 'Yes':#still some doubts about it############
				Actions.objects.bulk_create(actions)
				# db.session.add_all(actions)
				# db.session.commit()
				continue

			# 10. Active growth period maps to active growth period as is.
			seasons = []
			if 'Spring' in plant['Active Growth Period']:
				seasons.append('spring')
			if 'Summer' in plant['Active Growth Period']:
				seasons.append('summer')
			if 'Fall' in plant['Active Growth Period']:
				seasons.append('autumn')
			if 'Winter' in plant['Active Growth Period']:
				seasons.append('winter')

			for season in seasons:
				active_growth_period_id = ActiveGrowthPeriod.objects.filter(value=season).first().id
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='active_growth_period', value=active_growth_period_id))

			# 11. add livestock bloat as a behavior. Values: none, low, medium, high.
			if plant['Bloat'].strip():
				livestock_bloat_id = LivestockBloat.objects.filter(value=plant['Bloat'].strip().lower()).first().id
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='livestock_bloat_id', value=livestock_bloat_id))

			# 12. coppice potential with value yes translates to raw materials = biomass
			if plant['Coppice Potential'].strip() == 'Yes':
				raw_materials_prod_id = RawMaterialsProd.objects.filter(value='biomass').first().id
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='raw_materials_prod', value=raw_materials_prod_id))

			# 13. fire resistance translates with value yes translates to fire tolerance = resistant to fire,
			#     and with value no translates to fire tolerance = not resistant to fire
			if plant['Fire Resistance'].strip():
				fire_resistance_map = {'Yes': 'resistant to fire',# should add accelarets fire
						   'No': 'not resistant to fire'}
				fire_tol_id = FireTol.objects.filter(value=fire_resistance_map[plant['Fire Resistance'].strip()]).first().id
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='fire_tol_id', value=fire_tol_id))

			# 14. add flower color table with values: DONE
			#   Blue
			#   Brown
			#   Green
			#   Orange
			#   Purple
			#   Red
			#   White
			#   Yellow

			# 15. add foliage color table with values: DONE
			#   Dark Green
			#   Green
			#   Gray-Green
			#   Red
			#   White-Gray
			#   Yellow-Green
			#add fruit color table with values: DONE
			#   Black
			#   Blue
			#   Brown
			#   Green
			#   Orange
			#   Purple
			#   Red
			#   White
			#   Yellow

			# 16. flower color, fruit color, and foliage color map to our database exactly
			if plant['Flower Color'].strip():
				flower_color_id = FlowerColor.objects.filter(value=plant['Flower Color'].strip().lower()).first().id
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='flower_color', value=flower_color_id))
			if plant['Fruit Color'].strip():
				fruit_color_id = FruitColor.objects.filter(value=plant['Fruit Color'].strip().lower()).first().id
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='fruit_color', value=fruit_color_id))
			if plant['Foliage Color'].strip():
				foliage_color_id = FoliageColor.objects.filter(value=plant['Foliage Color'].strip().lower()).first().id
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='foliage_color', value=foliage_color_id))

			# 17. if flower conspicuous is yes or fruit conspicuous is yes then put it in our db as cultural and amenity = aesthetic
			if plant['Flower Conspicuous'].strip() == 'Yes' or plant['Fruit Conspicuous'].strip() == 'Yes':
				cultural_and_amenity_prod_id = CulturalAndAmenityProd.objects.filter(value='aesthetic').first().id
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='cultural_and_amenity_prod', value=cultural_and_amenity_prod_id))

			# 18. foliage porosity summer maps to canopy density
			#     porous maps to sparse
			#     moderate maps to moderate
			#     dense maps to dense
			if plant['Foliage Porosity Summer'].strip():
				foliage_porosit_summer_map = {'Porous': 'sparse',
								  'Moderate': 'moderate',
								  'Dense': 'dense'}
				canopy_density_id = CanopyDensity.objects.filter(value=foliage_porosit_summer_map[plant['Foliage Porosity Summer'].strip()]).first().id
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='canopy_density', value=canopy_density_id))

			# 19. Height, mature maps to height at maturity in feet (no unit change)
			if plant['Height, Mature (feet)'].strip():
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='height', value=float(plant['Height, Mature (feet)'].strip())))#property='height'???'

			# 20. leaf retention yes maps to evergreen, leaf retention no maps to deciduous
			if plant['Leaf Retention'].strip():
				leaf_retention_map = {'Yes': 'evergreen',
						   'No': 'deciduous'}
				leaf_retention_id = LeafRetention.objects.filter(value=leaf_retention_map[plant['Leaf Retention'].strip()]).first().id
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='leaf_retention', value=leaf_retention_id))

			# 21. add Allelopathic table with values yes and no
			#     add lifespan table
			#     values: short; moderate; long;
			#     descriptions: less than 100 years;  100 - 250 years; greater than 250 years
			if plant['Known Allelopath'].strip():
				allelopathic_id = Allelopathic.objects.filter(value=plant['Known Allelopath'].strip().lower()).first().id
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='allelopathic_id', value=allelopathic_id))
			# if plant['Lifespan'].strip():
# 				#lifespan_id = Lifespan.objects.filter(value=plant['Lifespan'].strip().lower()).first().id
# 				actions.append(Actions(transactions=transaction, action_type=trans_type, property='life_span', value=float(plant['Lifespan'].strip())))

			# 22. if Nitrogen Fixation is low, medium, or high then it maps to mineral nutrients = nitrogen
			if plant['Nitrogen Fixation'].strip() in ['Low', 'Medium', 'High']:
				mineral_nutrients_prod_id = MineralNutrientsProd.objects.filter(value='nitrogen').first().id
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='mineral_nutrients_prod', value=mineral_nutrients_prod_id))

			# 23. if shape and orientation is: DONE (implemented as part of #6)
			#       prostrate then layer = ground cover
			#       climbing then layer = climber
			#       decumbent = ground cover and herb


			# 24. add toxicity table with values: human and livestock toxicity
			#       none
			#       slight
			#       moderate
			#       severe
			# and map directly with usda toxicity
			if plant['Toxicity'].strip():
				toxicity_id = Toxicity.objects.filter(value=plant['Toxicity'].strip().lower()).first().id
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='toxicity_id', value=toxicity_id))

			# 26. fertility requirement/NutrientRequirements maps directly (NOTE FROM JOHN: 'Medium' needs to be mapped to 'moderate')
			if plant['Fertility Requirement'].strip():
				nutrient_requirement_map = {'Low': 'low',
								 'Medium': 'moderate',
								 'High': 'high'}
				nutrient_requirements_id = NutrientRequirements.objects.filter(value=nutrient_requirement_map[plant['Fertility Requirement'].strip()]).first().id
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='nutrient_requirements', value=nutrient_requirements_id))# fertility needs -> nutrient_req

			# 27. IGNORE

			# 28. moisture use maps to water requirements
			# if plant['Moisture Use'].strip():
# 				moisture_use_map = {'Low': 'low',
# 						'Medium': 'moderate',
# 						'High': 'high'}
# 				water_needs_id = WaterNeeds.objects.filter(value=moisture_use_map[plant['Moisture Use'].strip()]).first().id
# 				actions.append(Actions(transactions=transaction, action_type=trans_type, property='water_needs', value=water_needs_id))

			# 29. ph Maximum and ph Minimum map directly to our db (need to create max and min values though).
			if plant['pH (Minimum)'].strip():
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='pH_min', value=float(plant['pH (Minimum)'].strip())))
			if plant['pH (Maximum)'].strip():
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='pH_max', value=float(plant['pH (Maximum)'].strip())))


			# 30. salinity tolerance maps to salt tolerance
			#     shade tolerance maps like:
			#       intolerant to no shade
			#       intermediate to partial shade and light shade
			#       tolerant to permanent deep shade, permanent shade, partial shade, and light shade
			if plant['Salinity Tolerance'].strip():
				salinity_tolerance_map = {'None': 'not salt-tolerant',
							  'Low': 'slightly salt-tolerant',
							  'Medium': 'moderately salt-tolerant',
							  'High': 'salt-tolerant'}
				salt_tol_id = SaltTol.objects.filter(value=salinity_tolerance_map[plant['Salinity Tolerance'].strip()]).first().id
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='salt_tol_id', value=salt_tol_id))
			if plant['Shade Tolerance'].strip():
				shade_tols = []
			if plant['Shade Tolerance'].strip() == 'Intolerant':
				shade_tols.append('no shade')
			elif plant['Shade Tolerance'].strip() == 'Intermediate':
				shade_tols.append('partial shade')
				shade_tols.append('light shade')
			elif plant['Shade Tolerance'].strip() == 'Tolerant':
				shade_tols.append('permanent deep shade')
				shade_tols.append('permanent shade')
				shade_tols.append('partial shade')
				shade_tols.append('light shade')
			else:
				raise ValueError('Need to add handling for Shade Tolerance = ' + plant['Shade Tolerance'].strip())

			for shade_tol in shade_tols:
				shade_tol_id = ShadeTol.objects.filter(value=shade_tol).first().id
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='shade_tol', value=shade_tol_id))

			# 31. fruit/seed period end maps to harvest period
			#     (year-round = spring, summer, fall and winter)
			if plant['Fruit/Seed Period End'].strip():
				seasons = []
				# print('The error', plant['Fruit/Seed Period End'].strip())#------------------------------
			if plant['Fruit/Seed Period End'].strip() == 'Fall':
				seasons.append('autumn')
			elif plant['Fruit/Seed Period End'].strip() == 'Winter':
				seasons.append('winter')
			elif plant['Fruit/Seed Period End'].strip() == 'Spring':
				seasons.append('spring')
			elif plant['Fruit/Seed Period End'].strip() == 'Summer':
				seasons.append('summer')
			elif plant['Fruit/Seed Period End'].strip() == 'Year Round':
				seasons.append('autumn')
				seasons.append('winter')
				seasons.append('spring')
				seasons.append('summer')
			else:
				print(plant['Fruit/Seed Period End'].strip())
				# raise ValueError('Need to add handling for Fruit/Seed Period End = ' + plant['Fruit/Seed Period End'].strip())

			for season in seasons:
				harvest_period_id = HarvestPeriod.objects.filter(value=season).first().id
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='harvest_period', value=harvest_period_id))

			# 32. berry/nut/seed product as yes maps to food: nuts and fruit
			if plant['Berry/Nut/Seed Product'].strip() == 'Yes':
				food_prod_id = FoodProd.objects.filter(value='nuts').first().id
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='food_prod', value=food_prod_id))
				food_prod_id = FoodProd.objects.filter(value='fruit').first().id
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='food_prod', value=food_prod_id))

			# 33. christmas tree product as yes maps to cultural and amenity : spiritual and religious inspiration
			if plant['Christmas Tree Product'].strip() == 'Yes':
				cultural_and_amenity_prod_id = CulturalAndAmenityProd.objects.filter(value='spiritual and religious inspiration').first().id
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='cultural_and_amenity_prod', value=cultural_and_amenity_prod_id))

			# 34. add fodder as value to raw materials. DONE.
			# 35. fodder product as yes maps to raw materials: fodder
			if plant['Fodder Product'].strip() == 'Yes':
				raw_materials_prod_id = RawMaterialsProd.objects.filter(value='fodder').first().id
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='raw_materials_prod', value=raw_materials_prod_id))

			# 36. fuelwood product as low, medium, or high maps to raw materials: fuel
			if plant['Fuelwood Product'].strip() in ['Low', 'Medium', 'High']:
				raw_materials_prod_id = RawMaterialsProd.objects.filter(value='fuel').first().id
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='raw_materials_prod', value=raw_materials_prod_id))

			# 37. lumber product as yes maps to raw materials: timber
			if plant['Lumber Product'].strip() == 'Yes':
				raw_materials_prod_id = RawMaterialsProd.objects.filter(value='timber').first().id
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='raw_materials_prod', value=raw_materials_prod_id))

			# 38. add naval store as value to raw material. DONE.
			# 39. naval store product as yes maps to raw material: naval store
			if plant['Naval Store Product'].strip() == 'Yes':
				raw_materials_prod_id = RawMaterialsProd.objects.filter(value='naval store').first().id
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='raw_materials_prod', value=raw_materials_prod_id))

			# 40. map yes for post product to raw materials: timber
			if plant['Post Product'].strip() == 'Yes':
				raw_materials_prod_id = RawMaterialsProd.objects.filter(value='timber').first().id
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='raw_materials_prod', value=raw_materials_prod_id))

			# 41. add pulpwood as value to raw materials. DONE.
			# 42. map yes for pulpwood as raw materials: pulpwood
			if plant['Pulpwood Product'].strip() == 'Yes':
				raw_materials_prod_id = RawMaterialsProd.objects.filter(value='pulpwood').first().id
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='raw_materials_prod', value=raw_materials_prod_id))

			# 43. add veneer as value to raw materials. DONE.
			# 44. map yes for veneer as raw materials: veneer
			if plant['Veneer Product'].strip() == 'Yes':
				raw_materials_prod_id = RawMaterialsProd.objects.filter(value='veneer').first().id
				actions.append(Actions(transactions=transaction, action_type=trans_type, property='raw_materials_prod', value=raw_materials_prod_id))

			Actions.objects.bulk_create(actions)
			