def csv_import1(path1):
	with open(path1) as f:
		reader = csv.DictReader(f)#csv.reader(f)    
		for i,row in enumerate(reader):#reader:
			print(i,row['Scientific Name'])
			transactions = Transactions.objects.create(users_id=1, transaction_type='UPDATE', ignore=False)# not always Update
			# print(transaction.id)
			actions = []
			if len(row['Scientific Name'].split()) < 2:
				continue

			if row['Scientific Name'].split()[1] in 'spp.x?!':
				continue

			actions.append(Actions(transactions=transactions , action_type="UPDATE", property='genus', value=row['Scientific Name'].split()[0]))
			actions.append(Actions(transactions=transactions , action_type="UPDATE", property='species', value=row['Scientific Name'].split()[1]))

			if row['Common Name'].strip():
				actions.append(Actions(transactions=transactions , action_type="UPDATE", property='common_name', value=row['Common Name'].strip()))

			Actions.objects.bulk_create(actions)

#---------------------------------------------plantdb_export (zone 10 drought)_2.csv----
def csv_import3(path):
	with open(path) as f:
		reader = csv.DictReader(f)
		for i,plant in enumerate(reader):
			# print(i,plant['Name']):
			print(i,plant['Scientific Name'])
			transactions = Transactions.objects.create(users_id=1, transaction_type='UPDATE', ignore=False)# not always Update
			# print(transaction.id)
			actions = []
			if len(plant['Scientific Name'].split()) < 2:
				continue

			if plant['Scientific Name'].split()[1] in 'spp.x?!':
				continue

			actions.append(Actions(transactions=transactions, action_type="UPDATE", property='genus', value=plant['Scientific Name'].split()[0]))
			actions.append(Actions(transactions=transactions, action_type="UPDATE", property='species', value=plant['Scientific Name'].split()[1]))
			if len(plant['Scientific Name'].split()) < 2:
				print('variety:', plant['Cultivar Name'].strip()[3:])
				# actions.append(Actions(transactions=transactions, action_type="UPDATE", property='variety', value=plant['Cultivar Name'].strip()[3]))

			if plant['Common Name'].strip():
				actions.append(Actions(transactions=transactions , action_type="UPDATE", property='common_name', value=plant['Common Name'].strip()))

			if plant['Plant Type'].strip(): # assuming we don't have multiple layers/duration/leaf_retention in one entry
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
				else:
					raise ValueError('Can not recognize Plant Type = ' + plant['Plant Type'])

				if leaf_retention:
					leaf_retention_id = LeafRetention.objects.filter(value=leaf_retention).first().id
					actions.append(Actions(transactions=transactions, action_type="UPDATE", property='leaf_retention', value=leaf_retention_id))
				if layer:
					layer_id = Layer.objects.filter(value=layer).first().id
					actions.append(Actions(transactions=transactions, action_type="UPDATE", property='layer', value=layer_id))
				if duration:
					duration_id = Duration.objects.filter(value=duration).first().id
					actions.append(Actions(transactions=transactions, action_type="UPDATE", property='duration', value=duration_id))

			if plant['Height'].strip():
				actions.append(Actions(transactions=transactions, action_type="UPDATE", property='height', value=float(plant['Height'].strip())))
			if plant['Spread'].strip():
				actions.append(Actions(transactions=transactions, action_type="UPDATE", property='spread', value=float(plant['Spread'].strip())))

			# if plant['Root Depth'].strip():
			# 	actions.append(Actions(transactions=transactions, action_type="UPDATE", property='root_depth', value=float(plant['Root Depth'].strip())))
			if plant['Flower Color'].strip():
				colors=plant['Flower Color'].split(',')
				for color in colors:
					if color.strip().lower()in'pink cream lavender rose rust gray': # fix: Should I add these colors to the flower_color table? automatically/manually?
						continue
					flower_color_id = FlowerColor.objects.filter(value=color.strip().lower()).first().id
					actions.append(Actions(transactions=transactions, action_type="UPDATE", property='flower_color', value=flower_color_id))

			if plant['Fruit Time'].strip():# late summer, Early spring? shoud I add them?
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
					actions.append(Actions(transactions=transactions, action_type="UPDATE", property='harvest_period', value=harvest_period_id))

			if plant['Light']:
				lights = plant['Light'].strip()
				if 'Full_Sun' in lights:
					sun_need_id = SunNeeds.objects.filter(value='full sun').first().id
					actions.append(Actions(transactions=transactions, action_type="UPDATE", property='sun_needs', value=sun_need_id))
				if 'Partial_Shade' in lights:
					shade_tol_id = ShadeTol.objects.filter(value='partial shade').first().id
					actions.append(Actions(transactions=transactions, action_type="UPDATE", property='shade_tol', value=shade_tol_id))
				if 'Shade' in lights:
					shade_tol_id = ShadeTol.objects.filter(value='permanent shade').first().id
					actions.append(Actions(transactions=transactions, action_type="UPDATE", property='shade_tol', value=shade_tol_id))

			if plant['Soil Moisture']:
				soils = plant['Soil Moisture'].strip()
				if 'Wet' in soils:
					soil_drainage_tol_id = SoilDrainageTol.objects.filter(value='poor-drainage tolerant').first().id
					actions.append(Actions(transactions=transactions, action_type="UPDATE", property='soil_drainage_tol', value=soil_drainage_tol_id))
				if 'Moderate' in soils:
					soil_drainage_tol_id = SoilDrainageTol.objects.filter(value='moderate-drainage tolerant').first().id
					actions.append(Actions(transactions=transactions, action_type="UPDATE", property='soil_drainage_tol', value=soil_drainage_tol_id))
				if 'Dry' in soils:
					soil_drainage_tol_id = SoilDrainageTol.objects.filter(value='excessively-drained tolerance').first().id
					actions.append(Actions(transactions=transactions, action_type="UPDATE", property='soil_drainage_tol', value=soil_drainage_tol_id))

			if plant['Soil pH']:
				actions.append(Actions(transactions=transactions , action_type="UPDATE", property='pH_min', value=float(plant['Soil pH'].strip()[:3])))
				actions.append(Actions(transactions=transactions , action_type="UPDATE", property='pH_min', value=float(plant['Soil pH'].strip()[6:])))

			if plant['Ecological Function']:
				ecos = plant['Ecological Function'].strip()#.lower()
				if 'Chemical Barrier' in ecos:
					#barrier
					pass
				if 'Hedge' in ecos:
					#barrier
					pass
				if 'Windbreak' in ecos:
					#barrier
					pass
				if 'Erosion Control' in ecos:
					erosion_control_id = ErosionControl.objects.filter(value='medium').first().id
					actions.append(Actions(transactions=transactions, action_type="UPDATE", property='erosion_control', value=erosion_control_id))
				if 'Domestic Animal Forage' in ecos:
					# animal food? domestic
					pass
				if 'Groundcover' in ecos:
					layer_id = Layer.objects.filter(value='ground cover').first().id
					actions.append(Actions(transactions=transactions, action_type="UPDATE", property='layer', value=layer_id))
				if 'Wildlife Food' in ecos:
					# animal food? wild
					pass
				if 'Mulch Maker' in ecos:
					raw_materials_prod_id = RawMaterialsProd.objects.filter(value='biomass').first().id
					actions.append(Actions(transactions=transactions, action_type="UPDATE", property='raw_materials_prod', value=raw_materials_prod_id))
				if 'Nitrogen Fixer' in ecos:
					mineral_nutrients_prod_id = MineralNutrientsProd.objects.filter(value='nitrogen').first().id
					actions.append(Actions(transactions=transactions, action_type="UPDATE", property='mineral_nutrients_prod', value=mineral_nutrients_prod_id))

			if plant['Human Use/Crop']:
				human_uses = plant['Human Use/Crop'].strip()#.lower()
				if 'Biomass' in human_uses:
					raw_materials_prod_id = RawMaterialsProd.objects.filter(value='biomass').first().id
					actions.append(Actions(transactions=transactions, action_type="UPDATE", property='raw_materials_prod', value=raw_materials_prod_id))
				if 'Cleanser/Scourer' in human_uses or 'Soap' in human_uses:
					biochemical_material_prod_id = BiochemicalMaterialProd.objects.filter(value='detergents').first().id
					actions.append(Actions(transactions=transactions, action_type="UPDATE", property='biochemical_material_prod', value=biochemical_material_prod_id))
				if 'Cut Flower' in human_uses or 'Ornamental' in human_uses:
					cultural_and_amenity_prod_id = CulturalAndAmenityProd.objects.filter(value='aesthetic').first().id
					actions.append(Actions(transactions=transactions, action_type="UPDATE", property='cultural_and_amenity_prod', value=cultural_and_amenity_prod_id))
				if 'Dye' in human_uses:# TODO add dye to rawMaterial table?
					pass
					# raw_materials_prod_id = RawMaterialsProd.objects.filter(value='dye').first().id
					# actions.append(Actions(transactions=transactions, action_type="UPDATE", property='raw_materials_prod', value=raw_materials_prod_id))
				if 'Essential Oil' in human_uses: #TODO oil and essential oil the same? should I add essential oil to rawMat table?
					raw_materials_prod_id = RawMaterialsProd.objects.filter(value='oil').first().id
					actions.append(Actions(transactions=transactions, action_type="UPDATE", property='raw_materials_prod', value=raw_materials_prod_id))
				if 'Fiber' in human_uses:
					raw_materials_prod_id = RawMaterialsProd.objects.filter(value='fiber').first().id
					actions.append(Actions(transactions=transactions, action_type="UPDATE", property='raw_materials_prod', value=raw_materials_prod_id))
				if 'Insect Repellent' in human_uses:# TODO should I add insect repellant to medicin table?
					pass
					# medicinals_prod_id = MedicinalsProd.objects.filter(value='insect repellent').first().id
					# actions.append(Actions(transactions=transactions, action_type="UPDATE", property='medicinals_prod', value=medicinals_prod_id))
				if 'Wood' in human_uses:
					raw_materials_prod_id = RawMaterialsProd.objects.filter(value='timber').first().id
					actions.append(Actions(transactions=transactions, action_type="UPDATE", property='raw_materials_prod', value=raw_materials_prod_id))

				Actions.objects.bulk_create(actions)

#----------------------------usda.orange.for_import
def csv_import2(path):############################serotiny, degree_of_serotiny, allelochemicals######
	with open(path) as f:
		reader = csv.DictReader(f)#csv.reader(f)    
		for i,plant in enumerate(reader):#reader:
			print(i,plant['Scientific Name'])
			
			# 1. Don't import the entry if the Scientific Name is one word. (e.g., 'Ambrosia' versus 'Ambrosia acanthicarpa')
			if len(plant['Scientific Name'].split()) < 2:
				print('Scientific Name is one word')
				continue

			transactions = Transactions.objects.create(users_id=1, transaction_type='UPDATE', ignore=False)# not always Update
			actions = []

			# 2. genus = first word in scientific name, species = second word in scientific name
			actions.append(Actions(transactions=transactions, action_type="UPDATE", property='genus', value=plant['Scientific Name'].split()[0]))
			actions.append(Actions(transactions=transactions, action_type="UPDATE", property='species', value=plant['Scientific Name'].split()[1]))

			if plant['Common Name'].strip():
				actions.append(Actions(transactions=transactions , action_type="UPDATE", property='common_name', value=plant['Common Name'].strip()))

			# 3. add field for Family Common Name
			# what if the name is not in the famile tables... handle it!
			if plant['Family Common Name'].strip():
				family_common_name_id = TheFamilyCommonName.objects.filter(value=plant['Family Common Name'].strip()).first().id
				actions.append(Actions(transactions=transactions, action_type="UPDATE", property='family_common_name_id', value=family_common_name_id))
				
			# 4. add field for Family
			# what if the name is not in the famile tables... handle it!
			if plant['Family'].strip():
				family_id = TheFamily.objects.filter(value=plant['Family'].strip()).first().id
				actions.append(Actions(transactions=transactions, action_type="UPDATE", property='family_id', value=family_id))

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
				actions.append(Actions(transactions=transactions, action_type="UPDATE", property='duration', value=duration_id))

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
			values_to_store = set() ################################################################
			if plant['Growth Habit'].strip():
			   values_to_store.union(growth_habit_map[plant['Growth Habit'].strip()])
			if plant['Shape and Orientation'].strip():
			   values_to_store.union(shape_and_orientation_map[plant['Shape and Orientation'].strip()])
			for value in values_to_store:
			   layer_id = Layer.objects.filter(value=value).first().id
			   actions.append(Actions(transactions=transactions, action_type="UPDATE", property='layer', value=layer_id))

			# 7. Urls found in Fact Sheets and Plant Guides should be stored into the url tags
			if plant['Fact Sheets'].strip():
				actions.append(Actions(transactions=transactions, action_type="UPDATE", property='tags', value=plant['Fact Sheets'].strip()))
			if plant['Plant Guides'].strip():
				actions.append(Actions(transactions=transactions, action_type="UPDATE", property='tags', value=plant['Plant Guides'].strip()))

			# 8. You only have to fill in the remaining data for the plant if Characteristics Data = yes
			#    (i.e., you can move on to the next entry if it does not say yes).
			if plant['Characteristics Data'].strip() != 'Yes':#still some doubts about it############
				Actions.objects.bulk_create(actions)
				# db.session.add_all(actions)
				# db.session.commit()
				continue


			# 9. Cultivar translates to Variety
			if plant['Cultivar Name'].strip():
				actions.append(Actions(transactions=transactions, action_type="UPDATE", property='variety', value=plant['Cultivar Name'].strip()))

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
				actions.append(Actions(transactions=transactions, action_type="UPDATE", property='active_growth_period', value=active_growth_period_id))

			# 11. add livestock bloat as a behavior. Values: none, low, medium, high.
			if plant['Bloat'].strip():
				livestock_bloat_id = LivestockBloat.objects.filter(value=plant['Bloat'].strip().lower()).first().id
				actions.append(Actions(transactions=transactions, action_type="UPDATE", property='livestock_bloat_id', value=livestock_bloat_id))

			# 12. coppice potential with value yes translates to raw materials = biomass
			if plant['Coppice Potential'].strip() == 'Yes':
				raw_materials_prod_id = RawMaterialsProd.objects.filter(value='biomass').first().id
				actions.append(Actions(transactions=transactions, action_type="UPDATE", property='raw_materials_prod', value=raw_materials_prod_id))

			# 13. fire resistance translates with value yes translates to fire tolerance = resistant to fire,
			#     and with value no translates to fire tolerance = not resistant to fire
			if plant['Fire Resistance'].strip():
				fire_resistance_map = {'Yes': 'resistant to fire',# should add accelarets fire
						   'No': 'not resistant to fire'}
				fire_tol_id = FireTol.objects.filter(value=fire_resistance_map[plant['Fire Resistance'].strip()]).first().id
				actions.append(Actions(transactions=transactions, action_type="UPDATE", property='fire_tol_id', value=fire_tol_id))

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
				actions.append(Actions(transactions=transactions, action_type="UPDATE", property='flower_color', value=flower_color_id))
			if plant['Fruit Color'].strip():
				fruit_color_id = FruitColor.objects.filter(value=plant['Fruit Color'].strip().lower()).first().id
				actions.append(Actions(transactions=transactions, action_type="UPDATE", property='fruit_color', value=fruit_color_id))
			if plant['Foliage Color'].strip():
				foliage_color_id = FoliageColor.objects.filter(value=plant['Foliage Color'].strip().lower()).first().id
				actions.append(Actions(transactions=transactions, action_type="UPDATE", property='foliage_color', value=foliage_color_id))

			# 17. if flower conspicuous is yes or fruit conspicuous is yes then put it in our db as cultural and amenity = aesthetic
			if plant['Flower Conspicuous'].strip() == 'Yes' or plant['Fruit Conspicuous'].strip() == 'Yes':
				cultural_and_amenity_prod_id = CulturalAndAmenityProd.objects.filter(value='aesthetic').first().id
				actions.append(Actions(transactions=transactions, action_type="UPDATE", property='cultural_and_amenity_prod', value=cultural_and_amenity_prod_id))

			# 18. foliage porosity summer maps to canopy density
			#     porous maps to sparse
			#     moderate maps to moderate
			#     dense maps to dense
			if plant['Foliage Porosity Summer'].strip():
				foliage_porosit_summer_map = {'Porous': 'sparse',
								  'Moderate': 'moderate',
								  'Dense': 'dense'}
				canopy_density_id = CanopyDensity.objects.filter(value=foliage_porosit_summer_map[plant['Foliage Porosity Summer'].strip()]).first().id
				actions.append(Actions(transactions=transactions, action_type="UPDATE", property='canopy_density', value=canopy_density_id))

			# 19. Height, mature maps to height at maturity in feet (no unit change)
			if plant['Height, Mature (feet)'].strip():
				actions.append(Actions(transactions=transactions, action_type="UPDATE", property='height', value=float(plant['Height, Mature (feet)'].strip())))#property='height'???'

			# 20. leaf retention yes maps to evergreen, leaf retention no maps to deciduous
			if plant['Leaf Retention'].strip():
				leaf_retention_map = {'Yes': 'evergreen',
						   'No': 'deciduous'}
				leaf_retention_id = LeafRetention.objects.filter(value=leaf_retention_map[plant['Leaf Retention'].strip()]).first().id
				actions.append(Actions(transactions=transactions, action_type="UPDATE", property='leaf_retention', value=leaf_retention_id))

			# 21. add Allelopathic table with values yes and no
			#     add lifespan table
			#     values: short; moderate; long;
			#     descriptions: less than 100 years;  100 - 250 years; greater than 250 years
			if plant['Known Allelopath'].strip():
				allelopathic_id = Allelopathic.objects.filter(value=plant['Known Allelopath'].strip().lower()).first().id
				actions.append(Actions(transactions=transactions, action_type="UPDATE", property='allelopathic_id', value=allelopathic_id))
			if plant['Lifespan'].strip():
				lifespan_id = Lifespan.objects.filter(value=plant['Lifespan'].strip().lower()).first().id
				actions.append(Actions(transactions=transactions, action_type="UPDATE", property='lifespan_id', value=lifespan_id))

			# 22. if Nitrogen Fixation is low, medium, or high then it maps to mineral nutrients = nitrogen
			if plant['Nitrogen Fixation'].strip() in ['Low', 'Medium', 'High']:
				mineral_nutrients_prod_id = MineralNutrientsProd.objects.filter(value='nitrogen').first().id
				actions.append(Actions(transactions=transactions, action_type="UPDATE", property='mineral_nutrients_prod', value=mineral_nutrients_prod_id))

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
				actions.append(Actions(transactions=transactions, action_type="UPDATE", property='toxicity_id', value=toxicity_id))

			# 26. fertility requirement/NutrientRquirements maps directly (NOTE FROM JOHN: 'Medium' needs to be mapped to 'moderate')
			if plant['Fertility Requirement'].strip():
				nutrient_requirement_map = {'Low': 'low',
								 'Medium': 'moderate',
								 'High': 'high'}
				nutrient_requirements_id = NutrientRquirements.objects.filter(value=nutrient_requirement_map[plant['Fertility Requirement'].strip()]).first().id
				actions.append(Actions(transactions=transactions, action_type="UPDATE", property='fertility_needs', value=nutrient_requirements_id))# fertility needs -> nutrient_req

			# 27. IGNORE

			# 28. moisture use maps to water requirements
			if plant['Moisture Use'].strip():
				moisture_use_map = {'Low': 'low',
						'Medium': 'moderate',
						'High': 'high'}
				water_needs_id = WaterNeeds.objects.filter(value=moisture_use_map[plant['Moisture Use'].strip()]).first().id
				actions.append(Actions(transactions=transactions, action_type="UPDATE", property='water_needs', value=water_needs_id))

			# 29. ph Maximum and ph Minimum map directly to our db (need to create max and min values though).
			if plant['pH (Minimum)'].strip():
				actions.append(Actions(transactions=transactions, action_type="UPDATE", property='pH_min', value=float(plant['pH (Minimum)'].strip())))
			if plant['pH (Maximum)'].strip():
				actions.append(Actions(transactions=transactions, action_type="UPDATE", property='pH_max', value=float(plant['pH (Maximum)'].strip())))


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
				actions.append(Actions(transactions=transactions, action_type="UPDATE", property='salt_tol_id', value=salt_tol_id))
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
				actions.append(Actions(transactions=transactions, action_type="UPDATE", property='shade_tol', value=shade_tol_id))

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
				actions.append(Actions(transactions=transactions, action_type="UPDATE", property='harvest_period', value=harvest_period_id))

			# 32. berry/nut/seed product as yes maps to food: nuts and fruit
			if plant['Berry/Nut/Seed Product'].strip() == 'Yes':
				food_prod_id = FoodProd.objects.filter(value='nuts').first().id
				actions.append(Actions(transactions=transactions, action_type="UPDATE", property='food_prod', value=food_prod_id))
				food_prod_id = FoodProd.objects.filter(value='fruit').first().id
				actions.append(Actions(transactions=transactions, action_type="UPDATE", property='food_prod', value=food_prod_id))

			# 33. christmas tree product as yes maps to cultural and amenity : spiritual and religious inspiration
			if plant['Christmas Tree Product'].strip() == 'Yes':
				cultural_and_amenity_prod_id = CulturalAndAmenityProd.objects.filter(value='spiritual and religious inspiration').first().id
				actions.append(Actions(transactions=transactions, action_type="UPDATE", property='cultural_and_amenity_prod', value=cultural_and_amenity_prod_id))

			# 34. add fodder as value to raw materials. DONE.
			# 35. fodder product as yes maps to raw materials: fodder
			if plant['Fodder Product'].strip() == 'Yes':
				raw_materials_prod_id = RawMaterialsProd.objects.filter(value='fodder').first().id
				actions.append(Actions(transactions=transactions, action_type="UPDATE", property='raw_materials_prod', value=raw_materials_prod_id))

			# 36. fuelwood product as low, medium, or high maps to raw materials: fuel
			if plant['Fuelwood Product'].strip() in ['Low', 'Medium', 'High']:
				raw_materials_prod_id = RawMaterialsProd.objects.filter(value='fuel').first().id
				actions.append(Actions(transactions=transactions, action_type="UPDATE", property='raw_materials_prod', value=raw_materials_prod_id))

			# 37. lumber product as yes maps to raw materials: timber
			if plant['Lumber Product'].strip() == 'Yes':
				raw_materials_prod_id = RawMaterialsProd.objects.filter(value='timber').first().id
				actions.append(Actions(transactions=transactions, action_type="UPDATE", property='raw_materials_prod', value=raw_materials_prod_id))

			# 38. add naval store as value to raw material. DONE.
			# 39. naval store product as yes maps to raw material: naval store
			if plant['Naval Store Product'].strip() == 'Yes':
				raw_materials_prod_id = RawMaterialsProd.objects.filter(value='naval store').first().id
				actions.append(Actions(transactions=transactions, action_type="UPDATE", property='raw_materials_prod', value=raw_materials_prod_id))

			# 40. map yes for post product to raw materials: timber
			if plant['Post Product'].strip() == 'Yes':
				raw_materials_prod_id = RawMaterialsProd.objects.filter(value='timber').first().id
				actions.append(Actions(transactions=transactions, action_type="UPDATE", property='raw_materials_prod', value=raw_materials_prod_id))

			# 41. add pulpwood as value to raw materials. DONE.
			# 42. map yes for pulpwood as raw materials: pulpwood
			if plant['Pulpwood Product'].strip() == 'Yes':
				raw_materials_prod_id = RawMaterialsProd.objects.filter(value='pulpwood').first().id
				actions.append(Actions(transactions=transactions, action_type="UPDATE", property='raw_materials_prod', value=raw_materials_prod_id))

			# 43. add veneer as value to raw materials. DONE.
			# 44. map yes for veneer as raw materials: veneer
			if plant['Veneer Product'].strip() == 'Yes':
				raw_materials_prod_id = RawMaterialsProd.objects.filter(value='veneer').first().id
				actions.append(Actions(transactions=transactions, action_type="UPDATE", property='raw_materials_prod', value=raw_materials_prod_id))

			Actions.objects.bulk_create(actions)

