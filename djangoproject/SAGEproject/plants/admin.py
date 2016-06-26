from django.contrib import admin
#from .models import * as allModels#Plants#, Reg
from .models import *
import csv

properties_1_to_1 = ['genus', #add _id for foreign keys
                     'species',
                     'common_name',
                     'drought_tol_id',
                     'flood_tol_id',
                     'humidity_tol_id',
                     'salt_tol_id',
                     'toxin_removal_id',
                     'wind_tol_id',
                     'minimum_temperature_tol',
                     'innoculant',
                     'variety',
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
                               'fertility_needs',
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
                           'raw_materials_prod']

	# register((Actions,
 #          ActiveGrowthPeriod,
 #          Allelopathic,
 #          Animals,
 #          BiochemicalMaterialProd,
 #          CanopyDensity,
 #          CulturalAndAmenityProd,
 #          DroughtTol,
 #          EndemicStatus,
 #          ErosionControl,
 #          Family,
 #          FloodTol,
 #          FoodProd,
 #          FlowerColor,
 #          FoliageColor,
 #          FruitColor,
 #          HarvestPeriod,
 #          HumidityTol,
 #          Insects,
 #          Layer,
 #          Lifespan,
 #          LeafRetention,
 #          MedicinalsProd,
 #          MineralNutrientsProd,
 #          Plants,
 #          RawMaterialsProd,
 #          Regions,
 #          SaltTol,
 #          ShadeTol,
 #          SunNeeds,
 #          ToxinRemoval,
 #          Toxicity,
 #          Transactions,
 #          Users,
 #          WaterNeeds,
 #          WindTol))

# Register your models here.

def get_attributes(cls):
	f = False
	attributes = cls.__doc__.split(',')[1:]
	attributes[-1] = attributes[-1][:-1]
	if "regions" in attributes[-1]:
		t = attributes[-1]
		attributes[-1]=attributes[-2]
		attributes[-2]=t
		f= True
	attributes = [i.strip()+'_id' for i in attributes]
	return attributes, f


# class RegInPlant(admin.StackedInline): #using TabularInline instead of StackedInline looks better
#     model = Reg
#     extra = 3

class ViewAdmin(admin.ModelAdmin):

    """
    Custom made change_form template just for viewing purposes
    You need to copy this from /django/contrib/admin/templates/admin/change_form.html
    And then put that in your template folder that is specified in the 
    settings.TEMPLATE_DIR
    """
    change_form_template = 'view_form.html'

    # Remove the delete Admin Action for this Model
    actions = None

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        #Return nothing to make sure user can't update any data
        pass

# Example usage:
class SomeAdmin(ViewAdmin):
	pass
    # put your admin stuff here
    # or use pass

class PlantEndemicStatusByRegionInline(admin.TabularInline):
	model = PlantEndemicStatusByRegion
	extra = 1

class PlantDurationByRegionInline(admin.TabularInline):
	model = PlantDurationByRegion
	extra = 1

# class PlantHeightAtMaturityByRegionInline(admin.TabularInline):
# 	model = PlantHeightAtMaturityByRegion
# 	extra = 1

# class PlantSpreadAtMaturityByRegionInline(admin.TabularInline):
# 	model = PlantSpreadAtMaturityByRegion
# 	extra = 1

class PlantLayerInline(admin.TabularInline):
	model = PlantLayer
	extra = 1

class PlantCanopyDensityByRegionInline(admin.TabularInline):
	model = PlantCanopyDensityByRegion
	extra = 1

class PlantActiveGrowthPeriodByRegionInline(admin.TabularInline):
	model = PlantActiveGrowthPeriodByRegion
	extra = 1

class PlantHarvestPeriodByRegionInline(admin.TabularInline):
	model = PlantHarvestPeriodByRegion
	extra = 1

class PlantLeafRetentionByRegionInline(admin.TabularInline):
	model = PlantLeafRetentionByRegion
	extra = 1

class PlantFlowerColorInline(admin.TabularInline):
	model = PlantFlowerColor
	extra = 1

class PlantFoliageColorInline(admin.TabularInline):
	model = PlantFoliageColor
	extra = 1

class PlantFruitColorInline(admin.TabularInline):
	model = PlantFruitColor
	extra = 1

class PlantShadeTolByRegionInline(admin.TabularInline):
	model = PlantShadeTolByRegion
	extra = 1

class PlantSoilDrainageTolByRegionInline(admin.TabularInline):
	model = PlantSoilDrainageTolByRegion
	extra = 1

class PlantNutrientRequirementsByRegionInline(admin.TabularInline):
	model = PlantNutrientRequirementsByRegion
	extra = 1

class PlantWaterNeedsByRegionInline(admin.TabularInline):
	model = PlantWaterNeedsByRegion
	extra = 1

class PlantSunNeedsByRegionInline(admin.TabularInline):
	model = PlantSunNeedsByRegion
	extra = 1

class PlantFoodProdInline(admin.TabularInline):
	model = PlantFoodProd
	extra = 1

class PlantAnimalFoodInline(admin.TabularInline):
	model = PlantAnimalFood
	extra = 1

class PlantRawMaterialsProdInline(admin.TabularInline):
	model = PlantRawMaterialsProd
	extra = 1

class PlantMedicinalsProdInline(admin.TabularInline):
	model = PlantMedicinalsProd
	extra = 1

class PlantBiochemicalMaterialProdInline(admin.TabularInline):
	model = PlantBiochemicalMaterialProd
	extra = 1

class PlantCulturalAndAmenityProdInline(admin.TabularInline):
	model = PlantCulturalAndAmenityProd
	extra = 1

class PlantMineralNutrientsProdInline(admin.TabularInline):
	model = PlantMineralNutrientsProd
	extra = 1

class PlantErosionControlByRegionInline(admin.TabularInline):
	model = PlantErosionControlByRegion
	extra = 1

class PlantInsectAttractorByRegionInline(admin.TabularInline):
	model = PlantInsectAttractorByRegion
	extra = 1

class PlantInsectRegulatorByRegionInline(admin.TabularInline):
	model = PlantInsectRegulatorByRegion
	extra = 1

class PlantAnimalRegulatorByRegionInline(admin.TabularInline):
	model = PlantAnimalRegulatorByRegion
	extra = 1

class PlantAnimalAttractorByRegionInline(admin.TabularInline):
	model = PlantAnimalAttractorByRegion
	extra = 1

class PlantBarrierInline(admin.TabularInline):
	model = PlantBarrier
	extra = 1

class ReadonlyTabularInline(admin.TabularInline):
    can_delete = False
    extra = 0
    editable_fields = []
    
    def get_readonly_fields(self, request, obj=None):
        fields = []
        for field in self.model._meta.get_all_field_names():
            if (not field == 'id'):
                if (field not in self.editable_fields) and field not in self.exclude:
                    fields.append(field)
        return fields
    
    def has_add_permission(self, request):
        return False

class PlantsAdmin(admin.ModelAdmin):
	list_display = ('id', 'common_name','genus','species')
	#list_filter = ['genus']
	#filter_horizontal = ('water_needs',)
	search_fields = ('id', 'common_name', )
	can_delete = False #ca_delete?
	exclude = ('height','spread')
	#specifies the fields to show for change panel
	#fields = ['genus','species'] 
	
	# fieldsets = [
	#     (None,               {'fields': ['genus']}),
	#     ('Wind Tolerance', {'fields': ['wind_tol'], 'classes': ['collapse']}), #using collapse
	# ]

	# def related_family(self, obj):
	# 	return obj.family
	# related_family.short_description = 'family'
#[PlantEndemicStatusByRegionInline, PlantDurationByRegionInline, PlantHeightAtMaturityByRegionInline, PlantSpreadAtMaturityByRegionInline, PlantLayerInline, PlantCanopyDensityByRegionInline,PlantActiveGrowthPeriodByRegionInline, PlantHarvestPeriodByRegionInline, PlantLeafRetentionByRegionInline, PlantFlowerColorInline, PlantFoliageColorInline, PlantFruitColorInline, PlantShadeTolByRegionInline, PlantSoilDrainageTolByRegionInline, PlantFertilityNeedsByRegionInline, PlantWaterNeedsByRegionInline, PlantSunNeedsByRegionInline, PlantFoodProdInline, PlantAnimalFoodInline, PlantRawMaterialsProdInline, PlantMedicinalsProdInline, PlantBiochemicalMaterialProdInline, PlantCulturalAndAmenityProdInline, PlantMineralNutrientsProdInline, PlantErosionControlByRegionInline, PlantInsectAttractorByRegionInline, PlantInsectRegulatorByRegionInline, PlantAnimalRegulatorByRegionInline, PlantAnimalAttractorByRegionInline]
	inlines = [PlantEndemicStatusByRegionInline, PlantDurationByRegionInline, PlantLayerInline, PlantCanopyDensityByRegionInline,PlantActiveGrowthPeriodByRegionInline, PlantHarvestPeriodByRegionInline, PlantLeafRetentionByRegionInline, PlantFlowerColorInline, PlantFoliageColorInline, PlantFruitColorInline, PlantShadeTolByRegionInline, PlantSoilDrainageTolByRegionInline, PlantNutrientRequirementsByRegionInline, PlantWaterNeedsByRegionInline, PlantSunNeedsByRegionInline, PlantFoodProdInline, PlantAnimalFoodInline, PlantRawMaterialsProdInline, PlantMedicinalsProdInline, PlantBiochemicalMaterialProdInline, PlantCulturalAndAmenityProdInline, PlantMineralNutrientsProdInline, PlantErosionControlByRegionInline, PlantBarrierInline, PlantInsectAttractorByRegionInline, PlantInsectRegulatorByRegionInline, PlantAnimalRegulatorByRegionInline, PlantAnimalAttractorByRegionInline]


class PlantID(Plant):
	class Meta:
		proxy = True

class PlantIDAdmin(admin.ModelAdmin):
	#list_display = ('Family', 'family_common_name', 'genus', 'species', 'variety', 'common_name', 'EndemicStatus', 'tags', 'urltags')
	list_display = ('id', 'family', 'family_common_name', 'genus', 'species', 'variety', 'common_name', 'get_endemic_status', 'tags')
	fields = ['id', 'family', 'family_common_name','genus', 'species', 'variety', 'common_name', 'tags']
	readonly_fields= ('id',)
	search_fields = ('id', 'common_name', )
	exclude = ('height','spread')
	inlines = [PlantEndemicStatusByRegionInline]
	def get_endemic_status(self, obj):
		return ','.join([str(a) for a in obj.endemic_status.all()])
	get_endemic_status.short_description = 'Endemic Status'

class PlantCharacteristic(Plant):
	class Meta:
		proxy = True

class PlantCharacteristicAdmin(admin.ModelAdmin):
	# list_display = ('duration', 'height', 'spread', 'pH', 'layer', 'CanopyDensity', 'ActiveGrowthPeriod', 'HarvestPeriod', 'LeafRetention', 'FlowerColor', 'FoliageColor', 'FruitColor')
	list_display = ('id', 'genus', 'species','get_duration', 'pH_min', 'pH_max', 'get_layer','get_canopy_density', 'get_active_growth_period', 'get_harvest_period', 'get_leaf_retention', 'get_flower_color', 'get_foliage_color', 'get_fruit_color', 'degree_of_serotiny')
	fields = ['id', 'common_name', 'pH_min', 'pH_max', 'degree_of_serotiny']
	readonly_fields= ('id', 'common_name',)
	search_fields = ('id', 'common_name', )
	exclude = ('height','spread')
	# PlantHeightAtMaturityByRegionInline, PlantSpreadAtMaturityByRegionInline, 
	inlines = [PlantDurationByRegionInline, PlantLayerInline, PlantCanopyDensityByRegionInline,PlantActiveGrowthPeriodByRegionInline, PlantHarvestPeriodByRegionInline, PlantLeafRetentionByRegionInline, PlantFlowerColorInline, PlantFoliageColorInline, PlantFruitColorInline]

	def get_duration(self, obj):
		print('get_duration obj.duration: ', obj.duration.all())
		return ','.join([str(a) for a in obj.duration.all()])
	get_duration.short_description = 'Durations'


	# def get_height(self, obj):
	# 	my_list = PlantHeightAtMaturityByRegion.objects.filter(plants=obj.id)
	# 	return ','.join([str(a.height) for a in my_list])
	# get_height.short_description = 'Height At maturity'

	# def get_spread(self, obj):
	# 	my_list = PlantSpreadAtMaturityByRegion.objects.filter(plants=obj.id)
	# 	return ','.join([str(a) for a in my_list])
	# get_spread.short_description = 'Spread At Maturity'



	def get_layer(self, obj):
		return ','.join([str(a) for a in obj.layer.all()])
	get_layer.short_description = 'Layers'

	def get_canopy_density(self, obj):
		return ','.join([str(a) for a in obj.canopy_density.all()])
	get_canopy_density.short_description = 'Canopy Density'

	def get_active_growth_period(self, obj):
		return ','.join([str(a) for a in obj.active_growth_period.all()])
	get_active_growth_period.short_description = 'Active Growth Period'

	def get_harvest_period(self, obj):
		return ','.join([str(a) for a in obj.harvest_period.all()])
	get_harvest_period.short_description = 'Harvest Period'

	def get_leaf_retention(self, obj):
		return ','.join([str(a) for a in obj.leaf_retention.all()])
	get_leaf_retention.short_description = 'Leaf Retention'

	def get_flower_color(self, obj):
		return ','.join([str(a) for a in obj.flower_color.all()])
	get_flower_color.short_description = 'Flower Color'

	def get_foliage_color(self, obj):
		return ','.join([str(a) for a in obj.foliage_color.all()])
	get_foliage_color.short_description = 'Foliage Color'

	def get_fruit_color(self, obj):
		return ','.join([str(a) for a in obj.fruit_color.all()])
	get_fruit_color.short_description = 'Fruit Color'

	# def get_layer(self, obj):
	# 	return '\n'.join([x.layer for x in obj.layer.all()])

class PlantTolerance(Plant):
	class Meta:
		proxy = True

class PlantToleranceAdmin(admin.ModelAdmin):
	# list_display = ('shade_tol', 'salt_tol', 'flood_tol', 'drought_tol', 'humidity_tol', 'wind_tol', 'soil_drainage_tol', 'fire_tol', 'minimum_temperature_tol')
	list_display = ('id', 'genus', 'species', 'get_shade_tol', 'salt_tol', 'flood_tol', 'drought_tol', 'humidity_tol', 'wind_tol', 'get_soil_drainage_tol', 'fire_tol', 'minimum_temperature_tol')
	fields = ['id', 'common_name', 'salt_tol', 'flood_tol', 'drought_tol', 'humidity_tol', 'wind_tol', 'fire_tol', 'minimum_temperature_tol']
	readonly_fields= ('id', 'common_name',)
	search_fields = ('id', 'common_name', )
	exclude = ('height','spread')
	inlines = [PlantShadeTolByRegionInline, PlantSoilDrainageTolByRegionInline]

	def get_shade_tol(self, obj):
		return ','.join([str(a) for a in obj.shade_tol.all()])
	get_shade_tol.short_description = 'Shade Tolerance'

	def get_soil_drainage_tol(self, obj):
		return ','.join([str(a) for a in obj.soil_drainage_tol.all()])
	get_soil_drainage_tol.short_description = 'Soil Drainage Tolerance By Region'

class PlantNeed(Plant):
	class Meta:
		proxy = True

class PlantNeedAdmin(admin.ModelAdmin):
	# list_display = ('FertilityNeeds', 'WaterNeeds', 'innoculant', 'SunNeeds')
	list_display = ('id', 'genus', 'species', 'get_fertility_needs', 'get_water_needs', 'innoculant', 'get_sun_needs', 'serotiny')
	fields = ['id', 'common_name','innoculant', 'serotiny']
	readonly_fields= ('id', 'common_name',)
	search_fields = ('id', 'common_name', )
	exclude = ('height','spread')
	inlines = [PlantNutrientRequirementsByRegionInline, PlantWaterNeedsByRegionInline, PlantSunNeedsByRegionInline]

	def get_fertility_needs(self, obj):
		return ','.join([str(a) for a in obj.fertility_needs.all()])
	get_fertility_needs.short_description = 'Nutrient Requirements' # I may need to change the entire fertility_needs to nutrient_requirements later....!!!!!

	def get_water_needs(self, obj):
		return ','.join([str(a) for a in obj.water_needs.all()])
	get_water_needs.short_description = 'Water Needs'

	def get_sun_needs(self, obj):
		return ','.join([str(a) for a in obj.sun_needs.all()])
	get_sun_needs.short_description = 'Sun Needs'

class PlantProduct(Plant):
	class Meta:
		proxy = True

class PlantProductAdmin(admin.ModelAdmin):
	list_display = ('id', 'genus', 'species', 'get_food_prod', 'get_raw_materials_prod', 'get_medicinals_prod', 'get_biochemical_material_prod', 'get_cultural_and_amenity_prod', 'get_mineral_nutrients_prod', 'allelochemicals')
	fields = ['id', 'common_name', 'allelochemicals']
	readonly_fields= ('id', 'common_name',)
	search_fields = ('id', 'common_name', )
	exclude = ('height','spread')
	inlines = [PlantFoodProdInline, PlantAnimalFoodInline, PlantRawMaterialsProdInline, PlantMedicinalsProdInline, PlantBiochemicalMaterialProdInline, PlantCulturalAndAmenityProdInline, PlantMineralNutrientsProdInline]

	def get_food_prod(self, obj):
		return ','.join([str(a) for a in obj.food_prod.all()])
	get_food_prod.short_description = 'Food'

	def get_raw_materials_prod(self, obj):
		return ','.join([str(a) for a in obj.raw_materials_prod.all()])
	get_raw_materials_prod.short_description = 'Raw Materials'

	def get_medicinals_prod(self, obj):
		return ','.join([str(a) for a in obj.medicinals_prod.all()])
	get_medicinals_prod.short_description = 'Medicinals'

	def get_biochemical_material_prod(self, obj):
		return ','.join([str(a) for a in obj.biochemical_material_prod.all()])
	get_biochemical_material_prod.short_description = 'Biochemical Material'

	def get_cultural_and_amenity_prod(self, obj):
		return ','.join([str(a) for a in obj.cultural_and_amenity_prod.all()])
	get_cultural_and_amenity_prod.short_description = 'Cultural And Amenity'

	def get_mineral_nutrients_prod(self, obj):
		return ','.join([str(a) for a in obj.mineral_nutrients_prod.all()])
	get_mineral_nutrients_prod.short_description = 'Mineral Nutrients'

class PlantBehavior(Plant):
	class Meta:
		proxy = True

class PlantBehaviorAdmin(admin.ModelAdmin):
	# list_display = ('erosion_control', 'insect_attractor', 'insect_regulator', 'animal_attractor', 'animal_regulator','livestock_bloat', 'toxicity')
	list_display = ('id', 'genus', 'species', 'get_erosion_control', 'get_insect_attractor', 'get_insect_regulator', 'get_animal_attractor', 'get_animal_regulator', 'livestock_bloat', 'toxicity')
	fields = ['id', 'common_name', 'livestock_bloat', 'toxicity']
	readonly_fields= ('id', 'common_name',)
	search_fields = ('id', 'common_name', )
	exclude = ('height','spread')
	inlines = [PlantErosionControlByRegionInline, PlantBarrierInline, PlantInsectAttractorByRegionInline, PlantInsectRegulatorByRegionInline, PlantAnimalRegulatorByRegionInline, PlantAnimalAttractorByRegionInline]

	def get_erosion_control(self, obj):
		return ','.join([str(a) for a in obj.erosion_control.all()])
	get_erosion_control.short_description = 'Erosion Control '

	def get_insect_attractor(self, obj):
		return ','.join([str(a) for a in obj.plants_insect_attractor.all()])
	get_insect_attractor.short_description = 'Insect Attractor'

	def get_insect_regulator(self, obj):
		return ','.join([str(a) for a in obj.plants_insect_regulator.all()])
	get_insect_regulator.short_description = 'Insect Regulator'

	def get_animal_attractor(self, obj):
		return ','.join([str(a) for a in obj.plants_animal_attractor.all()])
	get_animal_attractor.short_description = 'Animal Attractor'

	def get_animal_regulator(self, obj):
		return ','.join([str(a) for a in obj.plants_animal_regulator.all()])
	get_animal_regulator.short_description = 'Animal Regulator'



# fcn = FamilyCommonName.objects.all().values_list('value','plants')
# for i in fcn:
# 	p = Plant.objects.get(pk=i[1])
# 	s = TheFamilyCommonName.objects.get(value=i[0])
# 	print(p.id, s.id)
# 	p.family_common_name = s
# 	p.save()


# f = Family.objects.all().values_list('value','plants')[:5]##################
# for i in f:
# 	print('1')
# 	p = Plant.objects.get(pk=i[1])
# 	s = TheFamily.objects.get(id=415)
# 	print(len(str(s.value)), len(str(i[0])))
# 	for j,c in enumerate(i[0]):
# 		print(c, s.value[j], c==s.value[j])
# 	print('3')
# 	# print(s.id)
# 	# p.family = s.id
# 	# p.save()


# obj, created = Person.objects.get_or_create(first_name='John', last_name='Lennon',
#                   defaults={'birthday': date(1940, 10, 9)})


path1=r'C:\Users\Moin\Desktop\CYBERSEES - Initial Plant List.csv'
path12=r'C:\Users\Moin\Desktop\CYBERSEES - Initial Plant List2.csv'
#Common Name,Scientific Name,Type of plant,Height range
path2=r'C:\Users\Moin\Desktop\usda.orange.for_import.csv'
path22=r'C:\Users\Moin\Desktop\usda.orange.for_import2.csv'
#Scientific Name,Common Name,Genus,Family,Family Common Name,Duration,Growth Habit,Fact Sheets,Plant Guides,Characteristics Data,Cultivar Name,Active Growth Period,Bloat,Coppice Potential,Fire Resistance,Flower Color,Flower Conspicuous,Foliage Color,Foliage Porosity Summer,Fruit Color,Fruit Conspicuous,"Height, Mature (feet)",Known Allelopath,Leaf Retention,Lifespan,Nitrogen Fixation,Shape and Orientation,Toxicity,Drought Tolerance,Fertility Requirement,Moisture Use,pH (Minimum),pH (Maximum),Salinity Tolerance,Shade Tolerance,Fruit/Seed Period End,Berry/Nut/Seed Product,Christmas Tree Product,Fodder Product,Fuelwood Product,Lumber Product,Naval Store Product,Post Product,Pulpwood Product,Veneer Product
path3=r'C:\Users\Moin\Desktop\plantdb_export (zone 10 drought)_2.csv'
#ID,Name,Scientific name,Plant Type,Height,Spread,Root Depth,Seasonal Interest,Notes,Flower Color,Root Type,Bloom Time,Fruit Time,Texture,Form,Growth Rate,Insect Predation,Disease,Light,Hardiness Zone,Soil Moisture,Soil pH,Ecological Function,Human Use/Crop

#--------------------------------------CYBERSEES - Initial Plant List-------------
def csv_import1(path1,trans_type):
	with open(path1) as f:
		reader = csv.DictReader(f)#csv.reader(f)    
		for i,row in enumerate(reader):#reader:
			transaction = Transactions.objects.create(users_id=1, transaction_type=trans_type, ignore=False)# not always Update
			# print(transaction.id)
			actions = []
			if not(row['Scientific Name']):
				continue
			if len(row['Scientific Name'].split()) < 2:
				continue

			# TODO what about var. in scientific name
			if 'spp.' in row['Scientific Name'] or 'x' in row['Scientific Name'] or '!' in row['Scientific Name']:
				continue

			print(i,row['Scientific Name'])

			if trans_type=='UPDATE':
				plant_id = Plant.objects.filter(genus=row['Scientific Name'].split()[0]).first().id
				print(plant_id)
				transaction.plants_id=plant_id
				transaction.save()
			actions.append(Actions(transactions=transaction , action_type=trans_type, property='genus', value=row['Scientific Name'].split()[0]))
			actions.append(Actions(transactions=transaction , action_type=trans_type, property='species', value=row['Scientific Name'].split()[1]))

			if row['Common Name'].strip():
				actions.append(Actions(transactions=transaction , action_type=trans_type, property='common_name', value=row['Common Name'].strip()))

			Actions.objects.bulk_create(actions)

#---------------------------------------------plantdb_export (zone 10 drought)_2.csv----
def csv_import3(path,trans_type):
	with open(path) as f:
		reader = csv.DictReader(f)
		for i,plant in enumerate(reader):
			# print(i,plant['Name']):
			transactions = Transactions.objects.create(users_id=1, transaction_type=trans_type, ignore=False)# not always Update
			# print(transaction.id)
			actions = []
			if not(plant['Scientific Name']):
				continue
			if len(plant['Scientific Name'].split()) < 2:
				continue

			# TODO what about var. in scientific name
			if 'spp.' in plant['Scientific Name'] or 'x' in plant['Scientific Name'] or '!' in plant['Scientific Name']:
				continue

			if trans_type=='UPDATE':
				plant_id = Plant.objects.filter(genus=plant['Scientific Name'].split()[0]).first().id
				print(plant_id)
				transactions.plants_id=plant_id
				transactions.save()

			print(i,plant['Scientific Name'], len(plant['Scientific Name']))

			actions.append(Actions(transactions=transactions, action_type=trans_type, property='genus', value=plant['Scientific Name'].split()[0]))
			actions.append(Actions(transactions=transactions, action_type=trans_type, property='species', value=plant['Scientific Name'].split()[1]))
			if len(plant['Scientific Name'].split()) > 2:
				variety = ''.join([c for c in ' '.join(plant['Scientific Name'].strip().split()[2:]) if c.isalpha() or c==' '])
				print('variety:', variety)
				actions.append(Actions(transactions=transactions, action_type=trans_type, property='variety', value=variety))

			if plant['Common Name'].strip():
				actions.append(Actions(transactions=transactions , action_type=trans_type, property='common_name', value=plant['Common Name'].strip()))

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
					actions.append(Actions(transactions=transactions, action_type=trans_type, property='leaf_retention', value=leaf_retention_id))
				if layer:
					layer_id = Layer.objects.filter(value=layer).first().id
					actions.append(Actions(transactions=transactions, action_type=trans_type, property='layer', value=layer_id))
				if duration:
					duration_id = Duration.objects.filter(value=duration).first().id
					actions.append(Actions(transactions=transactions, action_type=trans_type, property='duration', value=duration_id))

			if plant['Height'].strip():
				actions.append(Actions(transactions=transactions, action_type=trans_type, property='height', value=float(plant['Height'].strip())))
			if plant['Spread'].strip():
				actions.append(Actions(transactions=transactions, action_type=trans_type, property='spread', value=float(plant['Spread'].strip())))
			if plant['Root Depth'].strip():
				actions.append(Actions(transactions=transactions, action_type=trans_type, property='root_depth', value=float(plant['Root Depth'].strip())))
			if plant['Flower Color'].strip():
				colors=plant['Flower Color'].split(',')
				for color in colors:
					flower_color_id = FlowerColor.objects.filter(value=color.strip().lower()).first().id
					actions.append(Actions(transactions=transactions, action_type=trans_type, property='flower_color', value=flower_color_id))

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
					actions.append(Actions(transactions=transactions, action_type=trans_type, property='harvest_period', value=harvest_period_id))

			if plant['Light']:
				lights = plant['Light'].strip()
				if 'Full_Sun' in lights:
					sun_need_id = SunNeeds.objects.filter(value='full sun').first().id
					actions.append(Actions(transactions=transactions, action_type=trans_type, property='sun_needs', value=sun_need_id))
				if 'Partial_Shade' in lights:
					shade_tol_id = ShadeTol.objects.filter(value='partial shade').first().id
					actions.append(Actions(transactions=transactions, action_type=trans_type, property='shade_tol', value=shade_tol_id))
				if 'Shade' in lights:
					shade_tol_id = ShadeTol.objects.filter(value='permanent shade').first().id
					actions.append(Actions(transactions=transactions, action_type=trans_type, property='shade_tol', value=shade_tol_id))

			if plant['Soil Moisture']:
				soils = plant['Soil Moisture'].strip()
				if 'Wet' in soils:
					soil_drainage_tol_id = SoilDrainageTol.objects.filter(value='poor-drainage tolerant').first().id
					actions.append(Actions(transactions=transactions, action_type=trans_type, property='soil_drainage_tol', value=soil_drainage_tol_id))
				if 'Moderate' in soils:
					soil_drainage_tol_id = SoilDrainageTol.objects.filter(value='moderate-drainage tolerant').first().id
					actions.append(Actions(transactions=transactions, action_type=trans_type, property='soil_drainage_tol', value=soil_drainage_tol_id))
				if 'Dry' in soils:
					soil_drainage_tol_id = SoilDrainageTol.objects.filter(value='excessively-drained tolerance').first().id
					actions.append(Actions(transactions=transactions, action_type=trans_type, property='soil_drainage_tol', value=soil_drainage_tol_id))

			if plant['Soil pH']:
				actions.append(Actions(transactions=transactions , action_type=trans_type, property='pH_min', value=float(plant['Soil pH'].strip()[:3])))
				actions.append(Actions(transactions=transactions , action_type=trans_type, property='pH_max', value=float(plant['Soil pH'].strip()[6:])))

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
					actions.append(Actions(transactions=transactions, action_type=trans_type, property='barrier', value=barrier_id))
				
				if 'Erosion Control' in ecos:
					erosion_control_id = ErosionControl.objects.filter(value='medium').first().id
					actions.append(Actions(transactions=transactions, action_type=trans_type, property='erosion_control', value=erosion_control_id))
				if 'Domestic Animal Forage' in ecos:
					animal_food_id = AnimalFood.objects.filter(value='domestic').first().id
					actions.append(Actions(transactions=transactions, action_type=trans_type, property='animal_food', value=animal_food_id))
				if 'Groundcover' in ecos:
					layer_id = Layer.objects.filter(value='ground cover').first().id
					actions.append(Actions(transactions=transactions, action_type=trans_type, property='layer', value=layer_id))
				if 'Wildlife Food' in ecos:
					animal_food_id = AnimalFood.objects.filter(value='wild').first().id
					actions.append(Actions(transactions=transactions, action_type=trans_type, property='animal_food', value=animal_food_id))
				if 'Mulch Maker' in ecos:
					raw_materials_prod_id = RawMaterialsProd.objects.filter(value='biomass').first().id
					actions.append(Actions(transactions=transactions, action_type=trans_type, property='raw_materials_prod', value=raw_materials_prod_id))
				if 'Nitrogen Fixer' in ecos:
					mineral_nutrients_prod_id = MineralNutrientsProd.objects.filter(value='nitrogen').first().id
					actions.append(Actions(transactions=transactions, action_type=trans_type, property='mineral_nutrients_prod', value=mineral_nutrients_prod_id))

			if plant['Human Use/Crop']:
				human_uses = plant['Human Use/Crop'].strip()#.lower()
				if 'Biomass' in human_uses:
					raw_materials_prod_id = RawMaterialsProd.objects.filter(value='biomass').first().id
					actions.append(Actions(transactions=transactions, action_type=trans_type, property='raw_materials_prod', value=raw_materials_prod_id))
				if 'Cleanser/Scourer' in human_uses or 'Soap' in human_uses:
					biochemical_material_prod_id = BiochemicalMaterialProd.objects.filter(value='detergents').first().id
					actions.append(Actions(transactions=transactions, action_type=trans_type, property='biochemical_material_prod', value=biochemical_material_prod_id))
				if 'Cut Flower' in human_uses or 'Ornamental' in human_uses:
					cultural_and_amenity_prod_id = CulturalAndAmenityProd.objects.filter(value='aesthetic').first().id
					actions.append(Actions(transactions=transactions, action_type=trans_type, property='cultural_and_amenity_prod', value=cultural_and_amenity_prod_id))
				if 'Dye' in human_uses:
					raw_materials_prod_id = RawMaterialsProd.objects.filter(value='dye').first().id
					actions.append(Actions(transactions=transactions, action_type=trans_type, property='raw_materials_prod', value=raw_materials_prod_id))
				if 'Essential Oil' in human_uses:
					raw_materials_prod_id = RawMaterialsProd.objects.filter(value='essential oil').first().id
					actions.append(Actions(transactions=transactions, action_type=trans_type, property='raw_materials_prod', value=raw_materials_prod_id))
				if 'Fiber' in human_uses:
					raw_materials_prod_id = RawMaterialsProd.objects.filter(value='fiber').first().id
					actions.append(Actions(transactions=transactions, action_type=trans_type, property='raw_materials_prod', value=raw_materials_prod_id))
				if 'Insect Repellent' in human_uses:
					medicinals_prod_id = MedicinalsProd.objects.filter(value='insect repellent').first().id
					actions.append(Actions(transactions=transactions, action_type=trans_type, property='medicinals_prod', value=medicinals_prod_id))
				if 'Wood' in human_uses:
					raw_materials_prod_id = RawMaterialsProd.objects.filter(value='timber').first().id
					actions.append(Actions(transactions=transactions, action_type=trans_type, property='raw_materials_prod', value=raw_materials_prod_id))

				Actions.objects.bulk_create(actions)

#----------------------------usda.orange.for_import
def csv_import2(path,trans_type):############################serotiny, degree_of_serotiny, allelochemicals######
	with open(path) as f:
		reader = csv.DictReader(f)#csv.reader(f)    
		for i,plant in enumerate(reader):#reader:
			# if i>30:
			# 	break

			# 1. Don't import the entry if the Scientific Name is one word. (e.g., 'Ambrosia' versus 'Ambrosia acanthicarpa')
			if not(plant['Scientific Name']):
				continue
			if len(plant['Scientific Name'].split()) < 2:
				continue

			# TODO what about var. in scientific name
			if 'spp.' in plant['Scientific Name'] or 'x' in plant['Scientific Name'] or '!' in plant['Scientific Name']:
				continue

			print(i,plant['Scientific Name'], len(plant['Scientific Name']))

			transactions = Transactions.objects.create(users_id=1, transaction_type=trans_type, ignore=False)# not always Update
			actions = []

			if trans_type=='UPDATE':
				plant_id = Plant.objects.filter(genus=plant['Scientific Name'].split()[0]).first().id
				print(plant_id)
				transactions.plants_id=plant_id
				transactions.save()

			# 2. genus = first word in scientific name, species = second word in scientific name
			actions.append(Actions(transactions=transactions, action_type=trans_type, property='genus', value=plant['Scientific Name'].split()[0]))
			actions.append(Actions(transactions=transactions, action_type=trans_type, property='species', value=plant['Scientific Name'].split()[1]))

			if plant['Common Name'].strip():
				actions.append(Actions(transactions=transactions , action_type=trans_type, property='common_name', value=plant['Common Name'].strip()))

			# 3. add field for Family Common Name
			# what if the name is not in the famile tables... handle it!
			if plant['Family Common Name'].strip():
				if TheFamilyCommonName.objects.filter(value=plant['Family Common Name'].strip()):
					family_common_name_id = TheFamilyCommonName.objects.filter(value=plant['Family Common Name'].strip()).first().id
					actions.append(Actions(transactions=transactions, action_type=trans_type, property='family_common_name_id', value=family_common_name_id))
				
			# 4. add field for Family
			# what if the name is not in the famile tables... handle it!
			if plant['Family'].strip():
				if TheFamily.objects.filter(value=plant['Family'].strip()):
					family_id = TheFamily.objects.filter(value=plant['Family'].strip()).first().id
					actions.append(Actions(transactions=transactions, action_type=trans_type, property='family_id', value=family_id))

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
				actions.append(Actions(transactions=transactions, action_type=trans_type, property='duration', value=duration_id))

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
			#    actions.append(Actions(transactions=transactions, action_type=trans_type, property='layer', value=layer_id))

			# 7. Urls found in Fact Sheets and Plant Guides should be stored into the url tags
			if plant['Fact Sheets'].strip():
				actions.append(Actions(transactions=transactions, action_type=trans_type, property='tags', value=plant['Fact Sheets'].strip()))
			if plant['Plant Guides'].strip():
				actions.append(Actions(transactions=transactions, action_type=trans_type, property='tags', value=plant['Plant Guides'].strip()))

			# 8. You only have to fill in the remaining data for the plant if Characteristics Data = yes
			#    (i.e., you can move on to the next entry if it does not say yes).
			if plant['Characteristics Data'].strip() != 'Yes':#still some doubts about it############
				Actions.objects.bulk_create(actions)
				# db.session.add_all(actions)
				# db.session.commit()
				continue


			# 9. Cultivar translates to Variety
			if plant['Cultivar Name'].strip():
				actions.append(Actions(transactions=transactions, action_type=trans_type, property='variety', value=plant['Cultivar Name'].strip()))

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
				actions.append(Actions(transactions=transactions, action_type=trans_type, property='active_growth_period', value=active_growth_period_id))

			# 11. add livestock bloat as a behavior. Values: none, low, medium, high.
			if plant['Bloat'].strip():
				livestock_bloat_id = LivestockBloat.objects.filter(value=plant['Bloat'].strip().lower()).first().id
				actions.append(Actions(transactions=transactions, action_type=trans_type, property='livestock_bloat_id', value=livestock_bloat_id))

			# 12. coppice potential with value yes translates to raw materials = biomass
			if plant['Coppice Potential'].strip() == 'Yes':
				raw_materials_prod_id = RawMaterialsProd.objects.filter(value='biomass').first().id
				actions.append(Actions(transactions=transactions, action_type=trans_type, property='raw_materials_prod', value=raw_materials_prod_id))

			# 13. fire resistance translates with value yes translates to fire tolerance = resistant to fire,
			#     and with value no translates to fire tolerance = not resistant to fire
			if plant['Fire Resistance'].strip():
				fire_resistance_map = {'Yes': 'resistant to fire',# should add accelarets fire
						   'No': 'not resistant to fire'}
				fire_tol_id = FireTol.objects.filter(value=fire_resistance_map[plant['Fire Resistance'].strip()]).first().id
				actions.append(Actions(transactions=transactions, action_type=trans_type, property='fire_tol_id', value=fire_tol_id))

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
				actions.append(Actions(transactions=transactions, action_type=trans_type, property='flower_color', value=flower_color_id))
			if plant['Fruit Color'].strip():
				fruit_color_id = FruitColor.objects.filter(value=plant['Fruit Color'].strip().lower()).first().id
				actions.append(Actions(transactions=transactions, action_type=trans_type, property='fruit_color', value=fruit_color_id))
			if plant['Foliage Color'].strip():
				foliage_color_id = FoliageColor.objects.filter(value=plant['Foliage Color'].strip().lower()).first().id
				actions.append(Actions(transactions=transactions, action_type=trans_type, property='foliage_color', value=foliage_color_id))

			# 17. if flower conspicuous is yes or fruit conspicuous is yes then put it in our db as cultural and amenity = aesthetic
			if plant['Flower Conspicuous'].strip() == 'Yes' or plant['Fruit Conspicuous'].strip() == 'Yes':
				cultural_and_amenity_prod_id = CulturalAndAmenityProd.objects.filter(value='aesthetic').first().id
				actions.append(Actions(transactions=transactions, action_type=trans_type, property='cultural_and_amenity_prod', value=cultural_and_amenity_prod_id))

			# 18. foliage porosity summer maps to canopy density
			#     porous maps to sparse
			#     moderate maps to moderate
			#     dense maps to dense
			if plant['Foliage Porosity Summer'].strip():
				foliage_porosit_summer_map = {'Porous': 'sparse',
								  'Moderate': 'moderate',
								  'Dense': 'dense'}
				canopy_density_id = CanopyDensity.objects.filter(value=foliage_porosit_summer_map[plant['Foliage Porosity Summer'].strip()]).first().id
				actions.append(Actions(transactions=transactions, action_type=trans_type, property='canopy_density', value=canopy_density_id))

			# 19. Height, mature maps to height at maturity in feet (no unit change)
			if plant['Height, Mature (feet)'].strip():
				actions.append(Actions(transactions=transactions, action_type=trans_type, property='height', value=float(plant['Height, Mature (feet)'].strip())))#property='height'???'

			# 20. leaf retention yes maps to evergreen, leaf retention no maps to deciduous
			if plant['Leaf Retention'].strip():
				leaf_retention_map = {'Yes': 'evergreen',
						   'No': 'deciduous'}
				leaf_retention_id = LeafRetention.objects.filter(value=leaf_retention_map[plant['Leaf Retention'].strip()]).first().id
				actions.append(Actions(transactions=transactions, action_type=trans_type, property='leaf_retention', value=leaf_retention_id))

			# 21. add Allelopathic table with values yes and no
			#     add lifespan table
			#     values: short; moderate; long;
			#     descriptions: less than 100 years;  100 - 250 years; greater than 250 years
			if plant['Known Allelopath'].strip():
				allelopathic_id = Allelopathic.objects.filter(value=plant['Known Allelopath'].strip().lower()).first().id
				actions.append(Actions(transactions=transactions, action_type=trans_type, property='allelopathic_id', value=allelopathic_id))
			if plant['Lifespan'].strip():
				lifespan_id = Lifespan.objects.filter(value=plant['Lifespan'].strip().lower()).first().id
				actions.append(Actions(transactions=transactions, action_type=trans_type, property='lifespan_id', value=lifespan_id))

			# 22. if Nitrogen Fixation is low, medium, or high then it maps to mineral nutrients = nitrogen
			if plant['Nitrogen Fixation'].strip() in ['Low', 'Medium', 'High']:
				mineral_nutrients_prod_id = MineralNutrientsProd.objects.filter(value='nitrogen').first().id
				actions.append(Actions(transactions=transactions, action_type=trans_type, property='mineral_nutrients_prod', value=mineral_nutrients_prod_id))

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
				actions.append(Actions(transactions=transactions, action_type=trans_type, property='toxicity_id', value=toxicity_id))

			# 26. fertility requirement/NutrientRequirements maps directly (NOTE FROM JOHN: 'Medium' needs to be mapped to 'moderate')
			if plant['Fertility Requirement'].strip():
				nutrient_requirement_map = {'Low': 'low',
								 'Medium': 'moderate',
								 'High': 'high'}
				nutrient_requirements_id = NutrientRequirements.objects.filter(value=nutrient_requirement_map[plant['Fertility Requirement'].strip()]).first().id
				actions.append(Actions(transactions=transactions, action_type=trans_type, property='fertility_needs', value=nutrient_requirements_id))# fertility needs -> nutrient_req

			# 27. IGNORE

			# 28. moisture use maps to water requirements
			if plant['Moisture Use'].strip():
				moisture_use_map = {'Low': 'low',
						'Medium': 'moderate',
						'High': 'high'}
				water_needs_id = WaterNeeds.objects.filter(value=moisture_use_map[plant['Moisture Use'].strip()]).first().id
				actions.append(Actions(transactions=transactions, action_type=trans_type, property='water_needs', value=water_needs_id))

			# 29. ph Maximum and ph Minimum map directly to our db (need to create max and min values though).
			if plant['pH (Minimum)'].strip():
				actions.append(Actions(transactions=transactions, action_type=trans_type, property='pH_min', value=float(plant['pH (Minimum)'].strip())))
			if plant['pH (Maximum)'].strip():
				actions.append(Actions(transactions=transactions, action_type=trans_type, property='pH_max', value=float(plant['pH (Maximum)'].strip())))


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
				actions.append(Actions(transactions=transactions, action_type=trans_type, property='salt_tol_id', value=salt_tol_id))
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
				actions.append(Actions(transactions=transactions, action_type=trans_type, property='shade_tol', value=shade_tol_id))

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
				actions.append(Actions(transactions=transactions, action_type=trans_type, property='harvest_period', value=harvest_period_id))

			# 32. berry/nut/seed product as yes maps to food: nuts and fruit
			if plant['Berry/Nut/Seed Product'].strip() == 'Yes':
				food_prod_id = FoodProd.objects.filter(value='nuts').first().id
				actions.append(Actions(transactions=transactions, action_type=trans_type, property='food_prod', value=food_prod_id))
				food_prod_id = FoodProd.objects.filter(value='fruit').first().id
				actions.append(Actions(transactions=transactions, action_type=trans_type, property='food_prod', value=food_prod_id))

			# 33. christmas tree product as yes maps to cultural and amenity : spiritual and religious inspiration
			if plant['Christmas Tree Product'].strip() == 'Yes':
				cultural_and_amenity_prod_id = CulturalAndAmenityProd.objects.filter(value='spiritual and religious inspiration').first().id
				actions.append(Actions(transactions=transactions, action_type=trans_type, property='cultural_and_amenity_prod', value=cultural_and_amenity_prod_id))

			# 34. add fodder as value to raw materials. DONE.
			# 35. fodder product as yes maps to raw materials: fodder
			if plant['Fodder Product'].strip() == 'Yes':
				raw_materials_prod_id = RawMaterialsProd.objects.filter(value='fodder').first().id
				actions.append(Actions(transactions=transactions, action_type=trans_type, property='raw_materials_prod', value=raw_materials_prod_id))

			# 36. fuelwood product as low, medium, or high maps to raw materials: fuel
			if plant['Fuelwood Product'].strip() in ['Low', 'Medium', 'High']:
				raw_materials_prod_id = RawMaterialsProd.objects.filter(value='fuel').first().id
				actions.append(Actions(transactions=transactions, action_type=trans_type, property='raw_materials_prod', value=raw_materials_prod_id))

			# 37. lumber product as yes maps to raw materials: timber
			if plant['Lumber Product'].strip() == 'Yes':
				raw_materials_prod_id = RawMaterialsProd.objects.filter(value='timber').first().id
				actions.append(Actions(transactions=transactions, action_type=trans_type, property='raw_materials_prod', value=raw_materials_prod_id))

			# 38. add naval store as value to raw material. DONE.
			# 39. naval store product as yes maps to raw material: naval store
			if plant['Naval Store Product'].strip() == 'Yes':
				raw_materials_prod_id = RawMaterialsProd.objects.filter(value='naval store').first().id
				actions.append(Actions(transactions=transactions, action_type=trans_type, property='raw_materials_prod', value=raw_materials_prod_id))

			# 40. map yes for post product to raw materials: timber
			if plant['Post Product'].strip() == 'Yes':
				raw_materials_prod_id = RawMaterialsProd.objects.filter(value='timber').first().id
				actions.append(Actions(transactions=transactions, action_type=trans_type, property='raw_materials_prod', value=raw_materials_prod_id))

			# 41. add pulpwood as value to raw materials. DONE.
			# 42. map yes for pulpwood as raw materials: pulpwood
			if plant['Pulpwood Product'].strip() == 'Yes':
				raw_materials_prod_id = RawMaterialsProd.objects.filter(value='pulpwood').first().id
				actions.append(Actions(transactions=transactions, action_type=trans_type, property='raw_materials_prod', value=raw_materials_prod_id))

			# 43. add veneer as value to raw materials. DONE.
			# 44. map yes for veneer as raw materials: veneer
			if plant['Veneer Product'].strip() == 'Yes':
				raw_materials_prod_id = RawMaterialsProd.objects.filter(value='veneer').first().id
				actions.append(Actions(transactions=transactions, action_type=trans_type, property='raw_materials_prod', value=raw_materials_prod_id))

			Actions.objects.bulk_create(actions)

def process_updates():

	plants={0:{}}
	for transaction in Transactions.objects.all().filter(ignore=False, transaction_type='UPDATE').order_by('id'): # if same user updates should be filtered out
		print('transaction_type = ' + transaction.transaction_type)
		if not(transaction.plants_id):
			print('No plant_id in transaction UPDATE!')
			continue
		actions={}
		if not(transaction.plants_id in list(plants.keys())):
			plants[transaction.plants_id]={}
		# merging dictionaries so the latest update would be the result
		for action in transaction.actions_set.all():
			# actions[action.property]=[action.value, action.regions_id]
		# for property, value in actions.items():
			plants[transaction.plants_id][action.property]=[action.value, action.regions_id]

		# plants[transaction.plants_id]={**plants[transaction.plants_id],**actions}# saves the last update, not the number of votes
		# print(plants)

	for plant, updates in plants.items():
		for property, value in updates.items():
			if Plant.objects.get(pk=plant):
				the_plant = Plant.objects.get(pk=plant)
			else:
				raise ValueError("Invalid property plant id = " + plant)
			print(property, property=='height', property in 'heightspreadroot_depth')
			if property in 'heightspreadroot_depth':
				if PlantRegion.objects.filter(plants=the_plant.id, regions=value[1]):# TODO check for region Null----------------------------------
					plant_region = PlantRegion.objects.filter(plants=the_plant.id, regions=value[1]).first()#filter(transaction.plants_id, action.regions)
				else:
					plant_region = PlantRegion()
					plant_region.plants = the_plant
					plant_region.regions = value[1]
					plant_region.save()

				# somthing nice to learn------- how to dynamically choose the attribute that we want to set?!
				if property == 'height':
					plant_region.height = float(value[0])
				elif property == 'spread':
					plant_region.spread = float(value[0])
				elif property == 'root_depth':
					plant_region.root_depth = float(value[0])
				else:
					raise ValueError("Invalid property name = " + property)
				plant_region.save()

			elif property in properties_1_to_1:
				print('T_id={0}, property={1}, value={2}'.format(transaction.id, property, value[0]))
				setattr(the_plant, property, value[0]) # pH or ph... not being saved!
				the_plant.save()
			elif property in properties_many_with_region:# TODO PlantBarrierByRegion
				print('T_id={0}, property={1}, region={2}, value={3}'.format(transaction.id, property, value[1], value[0]))
				class_name = 'Plant' + property.title().replace('_', '') + 'ByRegion'
				if class_name=='PlantFertilityNeedsByRegion':
					class_name='PlantNutrientRequirementsByRegion'
				if class_name=='PlantBarrierByRegion':
					class_name='PlantBarrier'
				cls = globals()[class_name]
				attributes, is_region_last = get_attributes(cls)
				filter_args = {attributes[0]:the_plant.id, attributes[2]:value[0], attributes[1]:value[1]}
				cls_instance = cls.objects.filter(**filter_args)# TODO make sure get() works instead of filter().first() which also may carry bugs
				if not(cls_instance):
					cls_instance = cls()
					cls_instance.save()
				else:
					cls_instance = cls_instance.first()
				
				if is_region_last:
					cls_instance = cls(cls_instance.id ,the_plant.id, value[0], value[1])
				else:
					cls_instance = cls(cls_instance.id ,the_plant.id, value[1], value[0])
				cls_instance.save()
			elif property in properties_many_to_many:
				class_name = 'Plant' + property.title().replace('_', '')
				cls = globals()[class_name]
				attributes, f = get_attributes(cls)
				filter_args={attributes[0]:the_plant.id, attributes[1]:value[0]}
				cls_instance = cls.objects.filter(**filter_args)# TODO make sure get works instead of filter().firts() which also may carry bugs
				if not(cls_instance):
					cls_instance = cls()
					cls_instance.save()
				else:
					cls_instance = cls_instance.first()
				cls_instance = cls(cls_instance.id ,the_plant.id, value[0])# make sure that it is rewriting....
				cls_instance.save()
			elif property in properties_1_to_many:
				pass
			else:
				raise ValueError("Invalid property name = " + property)
				pass

def process_transactions():
	for transaction in Transactions.objects.all().filter(ignore=False).order_by('id'):
		print('transaction_type = ' + transaction.transaction_type)
		if transaction.transaction_type == 'INSERT':# get_or_crete????????
			new_plant = Plant()
			new_plant.save()
			transaction.plants_id = new_plant.id
			transaction.save()
			print('plant_id = ' + str(transaction.plants_id))
		elif transaction.transaction_type == 'DELETE':
			if transaction.plant is None:
				print('None objects')
				pass
				# db.session.rollback()
				# raise ValueError("Can't delete plant == None")
			# db.session.delete(transaction.plant)
			Plant.objects.get(pk=transaction.plant).delete()#----------------should be tested-----
			# db.session.commit()
			continue
		elif transaction.transaction_type == 'UPDATE':
			pass
		else:
			print('rollback')
			# db.session.rollback()
			# raise ValueError("Invalid transaction type = " + transaction.transaction_type)

		if len(transaction.actions_set.all())==0:
			print(len(transaction.actions_set.all()))

		for action in transaction.actions_set.all():# transaction.actions:
			the_plant=Plant.objects.get(pk=transaction.plants_id)
			if action.property in 'height spread root_depth':
				if PlantRegion.objects.filter(plants=the_plant.id, regions=action.regions):# TODO check for region Null----------------------------------
					plant_region = PlantRegion.objects.filter(plants=the_plant.id, regions=action.regions).first()#transaction.plants_id
				else:
					plant_region = PlantRegion()
					plant_region.plants = the_plant
					plant_region.regions = action.regions
					plant_region.save()
				# somthing nice to learn------- how to dynamically choose the attribute that we want to set?!
				if action.property == 'height':
					plant_region.height = float(action.value)
				elif action.property == 'spread':
					plant_region.spread = float(action.value)
				elif action.property == 'root_depth':
					plant_region.root_depth = float(action.value)
				else:
					raise ValueError("Invalid property name = " + action.property)

				plant_region.save()

			elif action.property in properties_1_to_1:# TODO check for INSERT DELETE UPDATE??????????????????
													# TODO height
				print('T_id={0}, property={1}, value={2}'.format(transaction.id, action.property, action.value))
				setattr(the_plant, action.property, action.value)# pH or ph... not being saved!
				the_plant.save()
			elif action.property in properties_many_with_region:# TODO height
				print('T_id={0}, property={1}, region={2}, value={3}'.format(transaction.id, action.property, action.regions, action.value))
				class_name = 'Plant' + action.property.title().replace('_', '') + 'ByRegion'
				if class_name=='PlantFertilityNeedsByRegion':
					class_name='PlantNutrientRequirementsByRegion'
				if class_name=='PlantBarrierByRegion':#TODO change renameModel PlantBarrier -> PLnatbarrierByRegion
					class_name='PlantBarrier'
				cls = globals()[class_name]
				attributes, is_region_last = get_attributes(cls)
				if action.action_type == 'INSERT':#CREATE
					# temp = cls.objects.create(the_plant.id, action.regions, action.value)
					cls_instance = cls()
					cls_instance.save()
					print (cls_instance.id ,the_plant.id, action.regions, action.value)
					if is_region_last:
						cls_instance = cls(cls_instance.id ,the_plant.id, action.value, action.regions)# no regions added?
					else:
						cls_instance = cls(cls_instance.id ,the_plant.id, action.regions, action.value)
					cls_instance.save()
			elif action.property in properties_many_to_many:
				class_name = 'Plant' + action.property.title().replace('_', '')
				cls = globals()[class_name]
				if action.action_type == 'INSERT':#CREATE
					# temp = cls.objects.create(the_plant.id, action.value)
					cls_instance = cls()
					cls_instance.save()
					print (cls_instance.id ,the_plant.id, action.value)
					cls_instance = cls(cls_instance.id ,the_plant.id, action.value)
					cls_instance.save()
			elif action.property in properties_1_to_many: # TODO Seortiny
				pass
				# class_name = action.property.title().replace('_', '')
				# cls = globals()[class_name]
				# if action.action_type == 'INSERT':#CREATE
				# 	# temp = cls.objects.create(the_plant.id, action.value)
				# 	cls_instance = cls()
				# 	cls_instance.save()
				# 	print (cls_instance.id ,the_plant.id, action.value)
				# 	cls_instance = cls(cls_instance.id ,the_plant.id, action.value)
				# 	cls_instance.save()
				# temp = cls.objects.create(cls_instance.id ,the_plant.id, action.value)
				# print('calss name',class_name)
				
				# elif action.action_type == 'DELETE':
				# when action_type is DELETE, the action value tells you the ID of the row to delete in the 1-to-many or many-to-many table
					# pass
					# cls_instance = cls.query.get(action.value)
					# db.session.delete(cls_instance)
				# elif action.action_type == 'UPDATE':
					# pass
					# db.session.rollback()
					# raise ValueError("Support for updating values hasn't been implemented yet."
					# + "Either implement updating in the code, or do a delete followed by an insert.")
				# else:
					# db.session.rollback()
					# raise ValueError("Invalid action type = " + action.action_type)
					# pass
			else:
				# db.session.rollback()
				raise ValueError("Invalid property name = " + action.property)
				pass

#---------------------flushing tables---------------------------
# print('Flushing actions table...')
# Actions.objects.all().delete()
# print('Flushing transactions table...')
# Transactions.objects.all().delete()
# print('Flushing plant table...')
# Plant.objects.all().delete()

# csv_import1(path1, 'UPDATE')
# csv_import2(path2, 'UPDATE')
# csv_import3(path3, 'UPDATE')
# csv_import1(path1, 'INSERT')
# csv_import2(path2, 'INSERT')
# csv_import3(path3, 'INSERT')
# process_transactions()
# process_updates()

# a = PlantDurationByRegion()
# print(dir(a))

admin.site.register(Plant, PlantsAdmin)
admin.site.register(PlantID, PlantIDAdmin)
admin.site.register(PlantCharacteristic, PlantCharacteristicAdmin)
admin.site.register(PlantTolerance, PlantToleranceAdmin)
admin.site.register(PlantNeed, PlantNeedAdmin)
admin.site.register(PlantProduct, PlantProductAdmin)
admin.site.register(PlantBehavior, PlantBehaviorAdmin)

#admin.site.register([Actions, ActiveGrowthPeriod, Allelopathic, Animals, BiochemicalMaterialProd, CanopyDensity, CulturalAndAmenityProd, DroughtTol, EndemicStatus, ErosionControl, Family, FloodTol, FoodProd, FlowerColor, FoliageColor, FruitColor, HarvestPeriod, HumidityTol, Insects, Layer, Lifespan, LeafRetention, MedicinalsProd, MineralNutrientsProd, RawMaterialsProd, Region, SaltTol, ShadeTol, SunNeeds, ToxinRemoval, Toxicity, Transactions, Users, WaterNeeds, WindTol])
#admin.site.register([TheFamily, TheFamilyCommonName, FireTol])
# admin.site.register([Actions, Region, Transactions, Users, DjangoAdminLog])

# for name, var in allModels.__dict__.items():
# 	if type(var) is ModelBase:
# 		admin.register(var)