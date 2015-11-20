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

class PlantHeightAtMaturityByRegionInline(admin.TabularInline):
	model = PlantHeightAtMaturityByRegion
	extra = 1

class PlantSpreadAtMaturityByRegionInline(admin.TabularInline):
	model = PlantSpreadAtMaturityByRegion
	extra = 1

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

class PlantFertilityNeedsByRegionInline(admin.TabularInline):
	model = PlantFertilityNeedsByRegion
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
	list_display = ('common_name','genus','species')
	#list_filter = ['genus']
	#filter_horizontal = ('water_needs',)
	search_fields = ('genus', 'common_name',)
	ca_delete = False
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
#[PlantEndemicStatusByRegionInline, PlantDurationByRegionInline, PlantHeightAtMaturityByRegionInline, PlantSpreadAtMaturityByRegionInline, PlantLayerInline, PlantCanopyDensityByRegionInline,PlantActiveGrowthPeriodByRegionInline, PlantHarvestPeriodByRegionInline, PlantLeafRetentionByRegionInline, PlantFlowerColorInline, PlantFoliageColorInline, PlantFruitColorInline, PlantShadeTolByRegionInline, PlantSoilDrainageTolByRegionInline, PlantFertilityNeedsByRegionInline, PlantWaterNeedsByRegionInline, PlantSunNeedsByRegionInline, PlantFoodProdInline, PlantRawMaterialsProdInline, PlantMedicinalsProdInline, PlantBiochemicalMaterialProdInline, PlantCulturalAndAmenityProdInline, PlantMineralNutrientsProdInline, PlantErosionControlByRegionInline, PlantInsectAttractorByRegionInline, PlantInsectRegulatorByRegionInline, PlantAnimalRegulatorByRegionInline, PlantAnimalAttractorByRegionInline]
	inlines = [PlantEndemicStatusByRegionInline, PlantDurationByRegionInline, PlantHeightAtMaturityByRegionInline, PlantSpreadAtMaturityByRegionInline, PlantLayerInline, PlantCanopyDensityByRegionInline,PlantActiveGrowthPeriodByRegionInline, PlantHarvestPeriodByRegionInline, PlantLeafRetentionByRegionInline, PlantFlowerColorInline, PlantFoliageColorInline, PlantFruitColorInline, PlantShadeTolByRegionInline, PlantSoilDrainageTolByRegionInline, PlantFertilityNeedsByRegionInline, PlantWaterNeedsByRegionInline, PlantSunNeedsByRegionInline, PlantFoodProdInline, PlantRawMaterialsProdInline, PlantMedicinalsProdInline, PlantBiochemicalMaterialProdInline, PlantCulturalAndAmenityProdInline, PlantMineralNutrientsProdInline, PlantErosionControlByRegionInline, PlantInsectAttractorByRegionInline, PlantInsectRegulatorByRegionInline, PlantAnimalRegulatorByRegionInline, PlantAnimalAttractorByRegionInline]


class PlantID(Plant):
	class Meta:
		proxy = True

class PlantIDAdmin(admin.ModelAdmin):
	#list_display = ('Family', 'family_common_name', 'genus', 'species', 'variety', 'common_name', 'EndemicStatus', 'tags', 'urltags')
	list_display = ('genus', 'species', 'variety', 'common_name', 'get_endemic_status', 'tags')
	exclude = ('height','spread')
	inlines = [PlantEndemicStatusByRegionInline]

	def get_family(self, obj):
		return obj.family
	get_family.short_description = 'Family'
	#get_family.admin_order_field = 'family__value'

class PlantCharacteristic(Plant):
	class Meta:
		proxy = True

class PlantCharacteristicAdmin(admin.ModelAdmin):
	# list_display = ('duration', 'height', 'spread', 'pH', 'layer', 'CanopyDensity', 'ActiveGrowthPeriod', 'HarvestPeriod', 'LeafRetention', 'FlowerColor', 'FoliageColor', 'FruitColor')
	list_display = ('genus', 'species','get_duration', 'get_height', 'get_spread', 'ph_min', 'ph_max', 'get_layer', 'get_canopy_density', 'get_active_growth_period', 'get_harvest_period', 'get_leaf_retention', 'get_flower_color', 'get_foliage_color', 'get_fruit_color')
	exclude = ('height','spread')
	inlines = [PlantDurationByRegionInline, PlantHeightAtMaturityByRegionInline, PlantSpreadAtMaturityByRegionInline, PlantLayerInline, PlantCanopyDensityByRegionInline,PlantActiveGrowthPeriodByRegionInline, PlantHarvestPeriodByRegionInline, PlantLeafRetentionByRegionInline, PlantFlowerColorInline, PlantFoliageColorInline, PlantFruitColorInline]

	# def get_layer(self, obj):
	# 	return '\n'.join([x.layer for x in obj.layer.all()])

class PlantTolerance(Plant):
	class Meta:
		proxy = True

class PlantToleranceAdmin(admin.ModelAdmin):
	# list_display = ('shade_tol', 'salt_tol', 'flood_tol', 'drought_tol', 'humidity_tol', 'wind_tol', 'soil_drainage_tol', 'fire_tol', 'minimum_temperature_tol')
	list_display = ('genus', 'species', 'get_shade_tol', 'salt_tol', 'flood_tol', 'drought_tol', 'humidity_tol', 'wind_tol', 'get_soil_drainage_tol', 'fire_tol', 'minimum_temperature_tol')
	exclude = ('height','spread')
	inlines = [PlantShadeTolByRegionInline, PlantSoilDrainageTolByRegionInline]


class PlantNeed(Plant):
	class Meta:
		proxy = True

class PlantNeedAdmin(admin.ModelAdmin):
	# list_display = ('FertilityNeeds', 'WaterNeeds', 'innoculant', 'SunNeeds')
	list_display = ('genus', 'species', 'get_fertility_needs', 'get_water_needs', 'innoculant', 'get_sun_needs')
	exclude = ('height','spread')
	inlines = [PlantFertilityNeedsByRegionInline, PlantWaterNeedsByRegionInline, PlantSunNeedsByRegionInline]


class PlantProduct(Plant):
	class Meta:
		proxy = True

class PlantProductAdmin(admin.ModelAdmin):
	list_display = ('genus', 'species', 'get_food_prod', 'get_raw_materials_prod', 'get_medicinals_prod', 'get_biochemical_material_prod', 'get_cultural_and_amenity_prod', 'get_mineral_nutrients_prod')
	exclude = ('height','spread')
	inlines = [PlantFoodProdInline, PlantRawMaterialsProdInline, PlantMedicinalsProdInline, PlantBiochemicalMaterialProdInline, PlantCulturalAndAmenityProdInline, PlantMineralNutrientsProdInline]

class PlantBehavior(Plant):
	class Meta:
		proxy = True

class PlantBehaviorAdmin(admin.ModelAdmin):
	# list_display = ('erosion_control', 'insect_attractor', 'insect_regulator', 'animal_attractor', 'animal_regulator','livestock_bloat', 'toxicity')
	list_display = ('genus', 'species', 'get_erosion_control', 'get_insect_attractor', 'get_insect_regulator', 'get_animal_attractor', 'get_animal_regulator', 'livestock_bloat', 'toxicity')
	exclude = ('height','spread')
	inlines = [PlantErosionControlByRegionInline, PlantInsectAttractorByRegionInline, PlantInsectRegulatorByRegionInline, PlantAnimalRegulatorByRegionInline, PlantAnimalAttractorByRegionInline]

#admin.site.register(Layer)
admin.site.register(Plant, PlantsAdmin)
admin.site.register(PlantID, PlantIDAdmin)
admin.site.register(PlantCharacteristic, PlantCharacteristicAdmin)
admin.site.register(PlantTolerance, PlantToleranceAdmin)
admin.site.register(PlantNeed, PlantNeedAdmin)
admin.site.register(PlantProduct, PlantProductAdmin)
admin.site.register(PlantBehavior, PlantBehaviorAdmin)

#admin.site.register([Actions, ActiveGrowthPeriod, Allelopathic, Animals, BiochemicalMaterialProd, CanopyDensity, CulturalAndAmenityProd, DroughtTol, EndemicStatus, ErosionControl, Family, FloodTol, FoodProd, FlowerColor, FoliageColor, FruitColor, HarvestPeriod, HumidityTol, Insects, Layer, Lifespan, LeafRetention, MedicinalsProd, MineralNutrientsProd, RawMaterialsProd, Region, SaltTol, ShadeTol, SunNeeds, ToxinRemoval, Toxicity, Transactions, Users, WaterNeeds, WindTol])

#admin.site.register([Actions, Animals, Family, Region, Transactions, Users, DjangoAdminLog])

# for name, var in allModels.__dict__.items():
# 	if type(var) is ModelBase:
# 		admin.register(var)