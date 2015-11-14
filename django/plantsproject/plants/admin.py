from django.contrib import admin
#from .models import * as allModels#Plants#, Reg
from .models import *

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


# class RegInPlant(admin.StackedInline): #using TabularInline instead of StackedInline looks better
#     model = Reg
#     extra = 3

class PlantsAdmin(admin.ModelAdmin):
	list_display = ('common_name','genus','species')
	list_filter = ['genus']
	#filter_horizontal = ('water_needs',)
	search_fields = ('genus', 'common_name',)
	#specifies the fields to show for change panel
	#fields = ['genus','species'] 
	
	fieldsets = [
	    (None,               {'fields': ['genus']}),
	    ('Wind Tolerance', {'fields': ['wind_tol'], 'classes': ['collapse']}), #using collapse
	]

	# def related_family(self, obj):
	# 	return obj.family
	# related_family.short_description = 'family'

# inlines = [RegInPlant]


class PlantID(Plant):
	class Meta:
		proxy = True

class PlantIDAdmin(admin.ModelAdmin):
	#list_display = ('Family', 'family_common_name', 'genus', 'species', 'variety', 'common_name', 'EndemicStatus', 'tags', 'urltags')
	list_display = ('get_family', 'get_family_common_name', 'genus', 'species', 'variety', 'common_name', 'tags')

class PlantCharacteristic(Plant):
	class Meta:
		proxy = True

class PlantCharacteristicAdmin(admin.ModelAdmin):
	# list_display = ('duration', 'height', 'spread', 'pH', 'layer', 'CanopyDensity', 'ActiveGrowthPeriod', 'HarvestPeriod', 'LeafRetention', 'FlowerColor', 'FoliageColor', 'FruitColor')
	list_display = ('genus', 'species','get_duration', 'get_height', 'get_spread', 'ph_min',)#'get_layer')

	# def get_layer(self, obj):
	# 	return '\n'.join([x.layer for x in obj.layer.all()])

class PlantTolerance(Plant):
	class Meta:
		proxy = True

class PlantToleranceAdmin(admin.ModelAdmin):
	# list_display = ('shade_tol', 'salt_tol', 'flood_tol', 'drought_tol', 'humidity_tol', 'wind_tol', 'soil_drainage_tol', 'fire_tol', 'minimum_temperature_tol')
	list_display = ('genus', 'species', 'get_shade_tol', 'salt_tol', 'flood_tol', 'drought_tol', 'humidity_tol', 'wind_tol', 'get_soil_drainage_tol', 'fire_tol', 'minimum_temperature_tol')


class PlantNeed(Plant):
	class Meta:
		proxy = True

class PlantNeedAdmin(admin.ModelAdmin):
	# list_display = ('FertilityNeeds', 'WaterNeeds', 'innoculant', 'SunNeeds')
	list_display = ('genus', 'species', 'get_fertility_needs', 'get_water_needs', 'innoculant', 'get_sun_needs')


class PlantProduct(Plant):
	class Meta:
		proxy = True

class PlantProductAdmin(admin.ModelAdmin):
	list_display = ('genus', 'species', 'get_food_prod', 'get_raw_materials_prod', 'get_medicinals_prod', 'get_biochemical_material_prod', 'get_cultural_and_amenity_prod', 'get_mineral_nutrients_prod')
	pass

class PlantBehavior(Plant):
	class Meta:
		proxy = True

class PlantBehaviorAdmin(admin.ModelAdmin):
	# list_display = ('erosion_control', 'insect_attractor', 'insect_regulator', 'animal_attractor', 'animal_regulator','livestock_bloat', 'toxicity')
	list_display = ('genus', 'species', 'livestock_bloat', 'toxicity')
	
#admin.site.register(Layer)
admin.site.register(Plant, PlantsAdmin)
admin.site.register(PlantID, PlantIDAdmin)
admin.site.register(PlantCharacteristic, PlantCharacteristicAdmin)
admin.site.register(PlantTolerance, PlantToleranceAdmin)
admin.site.register(PlantNeed, PlantNeedAdmin)
admin.site.register(PlantProduct, PlantProductAdmin)
admin.site.register(PlantBehavior, PlantBehaviorAdmin)

#admin.site.register([Actions, ActiveGrowthPeriod, Allelopathic, Animals, BiochemicalMaterialProd, CanopyDensity, CulturalAndAmenityProd, DroughtTol, EndemicStatus, ErosionControl, Family, FloodTol, FoodProd, FlowerColor, FoliageColor, FruitColor, HarvestPeriod, HumidityTol, Insects, Layer, Lifespan, LeafRetention, MedicinalsProd, MineralNutrientsProd, RawMaterialsProd, Region, SaltTol, ShadeTol, SunNeeds, ToxinRemoval, Toxicity, Transactions, Users, WaterNeeds, WindTol])

#admin.site.register([Actions, Animals, Family, Region, Transactions, Users])

# for name, var in allModels.__dict__.items():
# 	if type(var) is ModelBase:
# 		admin.register(var)