from django.contrib import admin
#from .models import * as allModels#Plants#, Reg
from .models import *
import csv



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

class PlantBarrierByRegionInline(admin.TabularInline):
	model = PlantBarrierByRegion
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
	list_display = ('id', 'common_name','get_scientific_name')
	#list_filter = ['genus']
	#filter_horizontal = ('water_needs',)
	search_fields = ('id', 'common_name', 'get_scientific_name')
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
	inlines = [PlantEndemicStatusByRegionInline, PlantDurationByRegionInline, PlantLayerInline, PlantCanopyDensityByRegionInline,PlantActiveGrowthPeriodByRegionInline, PlantHarvestPeriodByRegionInline, PlantLeafRetentionByRegionInline, PlantFlowerColorInline, PlantFoliageColorInline, PlantFruitColorInline, PlantShadeTolByRegionInline, PlantSoilDrainageTolByRegionInline, PlantNutrientRequirementsByRegionInline, PlantWaterNeedsByRegionInline, PlantSunNeedsByRegionInline, PlantFoodProdInline, PlantAnimalFoodInline, PlantRawMaterialsProdInline, PlantMedicinalsProdInline, PlantBiochemicalMaterialProdInline, PlantCulturalAndAmenityProdInline, PlantMineralNutrientsProdInline, PlantErosionControlByRegionInline, PlantBarrierByRegionInline, PlantInsectAttractorByRegionInline, PlantInsectRegulatorByRegionInline, PlantAnimalRegulatorByRegionInline, PlantAnimalAttractorByRegionInline]


class PlantID(Plant):
	class Meta:
		proxy = True

class PlantIDAdmin(admin.ModelAdmin):
	#list_display = ('Family', 'family_common_name', 'genus', 'species', 'variety', 'common_name', 'EndemicStatus', 'tags', 'urltags')
	list_display = ('id', 'family', 'family_common_name', 'get_scientific_name', 'common_name', 'get_endemic_status', 'tags')
	fields = ['id', 'family', 'family_common_name', 'get_scientific_name', 'common_name', 'tags']
	readonly_fields= ('id',)
	search_fields = ('id', 'common_name', 'get_scientific_name')
	exclude = ('height','spread')
	inlines = [PlantEndemicStatusByRegionInline]
	def get_endemic_status(self, obj):
		return ','.join([str(a) for a in obj.endemic_status.all()])
	get_endemic_status.short_description = 'Endemic Status'
	def get_scientific_name(self, obj):
		return ' '.join ([str(a) for a in plants_scientific_name.all()])

class PlantCharacteristic(Plant):
	class Meta:
		proxy = True

class PlantCharacteristicAdmin(admin.ModelAdmin):
	# list_display = ('duration', 'height', 'spread', 'pH', 'layer', 'CanopyDensity', 'ActiveGrowthPeriod', 'HarvestPeriod', 'LeafRetention', 'FlowerColor', 'FoliageColor', 'FruitColor')
	list_display = ('id', 'get_scientific_name','get_duration', 'pH_min', 'pH_max', 'get_layer','get_canopy_density', 'get_active_growth_period', 'get_harvest_period', 'get_leaf_retention', 'get_flower_color', 'get_foliage_color', 'get_fruit_color', 'degree_of_serotiny')
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
	list_display = ('id', 'get_scientific_name', 'get_shade_tol', 'salt_tol', 'flood_tol', 'drought_tol', 'humidity_tol', 'wind_tol', 'get_soil_drainage_tol', 'fire_tol', 'minimum_temperature_tol')
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
	list_display = ('id', 'get_scientific_name', 'get_fertility_needs', 'get_water_needs', 'innoculant', 'get_sun_needs', 'serotiny')
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
	list_display = ('id', 'get_scientific_name', 'get_food_prod', 'get_raw_materials_prod', 'get_medicinals_prod', 'get_biochemical_material_prod', 'get_cultural_and_amenity_prod', 'get_mineral_nutrients_prod', 'allelochemicals')
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
	list_display = ('id', 'get_scientific_name', 'get_erosion_control', 'get_insect_attractor', 'get_insect_regulator', 'get_animal_attractor', 'get_animal_regulator', 'livestock_bloat', 'toxicity')
	fields = ['id', 'common_name', 'livestock_bloat', 'toxicity']
	readonly_fields= ('id', 'common_name',)
	search_fields = ('id', 'common_name', )
	exclude = ('height','spread')
	inlines = [PlantErosionControlByRegionInline, PlantBarrierByRegionInline, PlantInsectAttractorByRegionInline, PlantInsectRegulatorByRegionInline, PlantAnimalRegulatorByRegionInline, PlantAnimalAttractorByRegionInline]

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
#admin.site.register([Actions, Region, Transactions, Users, DjangoAdminLog])

# for name, var in allModels.__dict__.items():
# 	if type(var) is ModelBase:
# 		admin.register(var)