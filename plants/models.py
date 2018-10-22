# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Q
import json



# class Actions(models.Model):
#     transactions = models.ForeignKey('Transactions', on_delete=models.CASCADE, blank=True, null=True)
#     action_type = models.TextField()
#     regions = models.ForeignKey('Region', on_delete=models.CASCADE, blank=True, null=True)
#     property = models.TextField()
#     value = models.TextField(blank=True, null=True)
#     citation = models.TextField(blank=True, null=True)
# 
#     class Meta:
#         managed = True
#         db_table = 'actions'
# 
#     def __str__(self):
#         return self.value




class ActiveGrowthPeriod(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'active_growth_period'

    def __str__(self):
        return self.value


class Allelopathic(models.Model):
    value = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'allelopathic'

    def __str__(self):
        return self.value


class Animals(models.Model):
    value = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'animals'

    def __str__(self):
        return self.value


class Barrier(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'barrier'

    def __str__(self):
        return self.value
        

class BiochemicalMaterialProd(models.Model):
    id = models.IntegerField(primary_key=True)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'biochemical_material_prod'

    def __str__(self):
        return self.value


class CanopyDensity(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'canopy_density'

    def __str__(self):
        return self.value


class CulturalAndAmenityProd(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cultural_and_amenity_prod'

    def __str__(self):
        return self.value


class DroughtTol(models.Model):
    value = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'drought_tol'

    def __str__(self):
        return self.value


class Duration(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'duration'

    def __str__(self):
        return self.value


class EndemicStatus(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'endemic_status'

    def __str__(self):
        return self.value


class ErosionControl(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'erosion_control'

    def __str__(self):
        return self.value


class TheFamily(models.Model):
    value = models.CharField(max_length=160, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'the_family'

    def __str__(self):
        return self.value


class TheFamilyCommonName(models.Model):
    value = models.CharField(max_length=160, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'the_family_common_name'

    def __str__(self):
        return self.value


class NutrientRequirements(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'nutrient_requirements'

    def __str__(self):
        return self.value


class FireTol(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'fire_tol'

    def __str__(self):
        return self.value


class FloodTol(models.Model):
    value = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'flood_tol'

    def __str__(self):
        return self.value


class FlowerColor(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'flower_color'

    def __str__(self):
        return self.value


class FoliageColor(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'foliage_color'

    def __str__(self):
        return self.value


class FoodProd(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'food_prod'

    def __str__(self):
        return self.value

class AnimalFood(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'animal_food'

    def __str__(self):
        return self.value

class FruitColor(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'fruit_color'

    def __str__(self):
        return self.value


class HarvestPeriod(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'harvest_period'

    def __str__(self):
        return self.value


class HumidityTol(models.Model):
    value = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'humidity_tol'

    def __str__(self):
        return self.value


class Insects(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'insects'

    def __str__(self):
        return self.value


class Layer(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'layer'

    def __str__(self):
        return self.value


class LeafRetention(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'leaf_retention'

    def __str__(self):
        return self.value


# class life_span(models.Model):
#     value = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
# 
#     class Meta:
#         managed = True
#         db_table = 'life_span'
# 
#     def __str__(self):
#         return self.value


class LivestockBloat(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'livestock_bloat'

    def __str__(self):
        return self.value


class MedicinalsProd(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'medicinals_prod'

    def __str__(self):
        return self.value


class MineralNutrientsProd(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mineral_nutrients_prod'

    def __str__(self):
        return self.value
        



class PlantActiveGrowthPeriodByRegion(models.Model):
    plants = models.ForeignKey('Plant', blank=True, null=True, on_delete=models.CASCADE)
    active_growth_period = models.ForeignKey(ActiveGrowthPeriod, blank=True, null=True, on_delete=models.CASCADE)
    regions = models.ForeignKey('Region', blank=True, null=True, on_delete=models.CASCADE)
    reference = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'plants_active_growth_period_by_region'


class PlantAnimalAttractorByRegion(models.Model):
    plants = models.ForeignKey('Plant', blank=True, null=True, on_delete=models.CASCADE)
    animals = models.ForeignKey(Animals, blank=True, null=True, on_delete=models.CASCADE)
    regions = models.ForeignKey('Region', blank=True, null=True, on_delete=models.CASCADE)
    reference = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'plants_animal_attractor_by_region'


class PlantAnimalRegulatorByRegion(models.Model):
    plants = models.ForeignKey('Plant', blank=True, null=True, on_delete=models.CASCADE)
    animals = models.ForeignKey(Animals, blank=True, null=True, on_delete=models.CASCADE)
    regions = models.ForeignKey('Region', blank=True, null=True, on_delete=models.CASCADE)
    reference = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'plants_animal_regulator_by_region'


class PlantBiochemicalMaterialProd(models.Model):
    plants = models.ForeignKey('Plant', blank=True, null=True, on_delete=models.CASCADE)
    biochemical_material_prod = models.ForeignKey(BiochemicalMaterialProd, on_delete=models.CASCADE, blank=True, null=True)
    reference = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'plants_biochemical_material_prod'


class PlantCanopyDensityByRegion(models.Model):
    plants = models.ForeignKey('Plant', blank=True, null=True, on_delete=models.CASCADE)
    regions = models.ForeignKey('Region', blank=True, null=True, on_delete=models.CASCADE)
    canopy_density = models.ForeignKey(CanopyDensity, blank=True, null=True, on_delete=models.CASCADE)
    reference = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'plants_canopy_density_by_region'
        unique_together = (('plants', 'regions'),)


class PlantCulturalAndAmenityProd(models.Model):
    plants = models.ForeignKey('Plant', on_delete=models.CASCADE, blank=True, null=True)
    cultural_and_amenity_prod = models.ForeignKey(CulturalAndAmenityProd, on_delete=models.CASCADE, blank=True, null=True)
    reference = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'plants_cultural_and_amenity_prod'


class PlantDurationByRegion(models.Model):
    plants = models.ForeignKey('Plant', on_delete=models.CASCADE, blank=True, null=True)
    regions = models.ForeignKey('Region', on_delete=models.CASCADE, blank=True, null=True)
    duration = models.ForeignKey(Duration, on_delete=models.CASCADE, blank=True, null=True)
    reference = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'plants_duration_by_region'
        unique_together = (('plants', 'regions'),)


class PlantEndemicStatusByRegion(models.Model):
    plants = models.ForeignKey('Plant', on_delete=models.CASCADE, blank=True, null=True)
    endemic_status = models.ForeignKey(EndemicStatus, on_delete=models.CASCADE, blank=True, null=True)
    regions = models.ForeignKey('Region', on_delete=models.CASCADE, blank=True, null=True)
    reference = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'plants_endemic_status_by_region'

class PlantErosionControlByRegion(models.Model):
    plants = models.ForeignKey('Plant', on_delete=models.CASCADE, blank=True, null=True)
    regions = models.ForeignKey('Region', on_delete=models.CASCADE, blank=True, null=True)
    erosion_control = models.ForeignKey(ErosionControl, on_delete=models.CASCADE, blank=True, null=True)
    reference = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'plants_erosion_control_by_region'
        unique_together = (('plants', 'regions'),)

class PlantBarrierByRegion(models.Model):# BarrierByRegion
    plants = models.ForeignKey('Plant', on_delete=models.CASCADE, blank=True, null=True)
    regions = models.ForeignKey('Region', on_delete=models.CASCADE, blank=True, null=True)
    barrier = models.ForeignKey('Barrier', on_delete=models.CASCADE, blank=True, null=True)
    reference = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'plants_barrier_by_region' # TODO
        unique_together = (('plants', 'regions'),)

class PlantNutrientRequirementsByRegion(models.Model):
    plants = models.ForeignKey('Plant', on_delete=models.CASCADE, blank=True, null=True)
    regions = models.ForeignKey('Region', on_delete=models.CASCADE, blank=True, null=True)
    nutrient_requirements = models.ForeignKey(NutrientRequirements, on_delete=models.CASCADE, blank=True, null=True) #####
    reference = models.TextField(blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'plants_nutrient_requirements_by_region'
        unique_together = (('plants', 'regions'),)


class PlantFlowerColor(models.Model):
    plants = models.ForeignKey('Plant', on_delete=models.CASCADE, blank=True, null=True)
    flower_color = models.ForeignKey(FlowerColor, on_delete=models.CASCADE, blank=True, null=True)
    reference = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'plants_flower_color'


class PlantFoliageColor(models.Model):
    plants = models.ForeignKey('Plant', on_delete=models.CASCADE, blank=True, null=True)
    foliage_color = models.ForeignKey(FoliageColor, on_delete=models.CASCADE, blank=True, null=True)
    reference = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'plants_foliage_color'


class PlantFoodProd(models.Model):
    plants = models.ForeignKey('Plant', on_delete=models.CASCADE, blank=True, null=True)
    food_prod = models.ForeignKey(FoodProd, on_delete=models.CASCADE, blank=True, null=True)
    reference = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'plants_food_prod'

class PlantAnimalFood(models.Model):
    plants = models.ForeignKey('Plant', on_delete=models.CASCADE, blank=True, null=True)
    animal_food = models.ForeignKey(AnimalFood, on_delete=models.CASCADE, blank=True, null=True)
    reference = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'plants_animal_food'

class PlantFruitColor(models.Model):
    plants = models.ForeignKey('Plant', on_delete=models.CASCADE, blank=True, null=True)
    fruit_color = models.ForeignKey(FruitColor, on_delete=models.CASCADE, blank=True, null=True)
    reference = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'plants_fruit_color'


class PlantHarvestPeriodByRegion(models.Model):
    plants = models.ForeignKey('Plant', on_delete=models.CASCADE, blank=True, null=True)
    harvest_period = models.ForeignKey(HarvestPeriod, on_delete=models.CASCADE, blank=True, null=True)
    regions = models.ForeignKey('Region', on_delete=models.CASCADE, blank=True, null=True)
    reference = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'plants_harvest_period_by_region'


class PlantInsectAttractorByRegion(models.Model):
    plants = models.ForeignKey('Plant', on_delete=models.CASCADE, blank=True, null=True)
    insects = models.ForeignKey(Insects, on_delete=models.CASCADE, blank=True, null=True)
    regions = models.ForeignKey('Region', on_delete=models.CASCADE, blank=True, null=True)
    reference = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'plants_insect_attractor_by_region'

    # def __str__(self):
    #     return self.insects


class PlantInsectRegulatorByRegion(models.Model):
    plants = models.ForeignKey('Plant', on_delete=models.CASCADE, blank=True, null=True)
    insects = models.ForeignKey(Insects, on_delete=models.CASCADE, blank=True, null=True)
    regions = models.ForeignKey('Region', on_delete=models.CASCADE, blank=True, null=True)
    reference = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'plants_insect_regulator_by_region'


class PlantLayer(models.Model):
    plants = models.ForeignKey('Plant', on_delete=models.CASCADE, blank=True, null=True)
    layer = models.ForeignKey(Layer, on_delete=models.CASCADE, blank=True, null=True)
    reference = models.TextField(blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'plants_layer'

    def __str__(self):
        return str(self.plants)


class PlantLeafRetentionByRegion(models.Model):
    plants = models.ForeignKey('Plant', on_delete=models.CASCADE, blank=True, null=True)
    regions = models.ForeignKey('Region', on_delete=models.CASCADE, blank=True, null=True)
    leaf_retention = models.ForeignKey(LeafRetention, on_delete=models.CASCADE, blank=True, null=True)
    reference = models.TextField(blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'plants_leaf_retention_by_region'
        unique_together = (('plants', 'regions'),)


class PlantMedicinalsProd(models.Model):
    plants = models.ForeignKey('Plant', on_delete=models.CASCADE, blank=True, null=True)
    medicinals_prod = models.ForeignKey(MedicinalsProd, on_delete=models.CASCADE, blank=True, null=True)
    reference = models.TextField(blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'plants_medicinals_prod'


class PlantMineralNutrientsProd(models.Model):
    plants = models.ForeignKey('Plant', on_delete=models.CASCADE, blank=True, null=True)
    mineral_nutrients_prod = models.ForeignKey(MineralNutrientsProd, on_delete=models.CASCADE, blank=True, null=True)
    reference = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'plants_mineral_nutrients_prod'

class PlantRawMaterialsProd(models.Model):
    plants = models.ForeignKey('Plant', on_delete=models.CASCADE, blank=True, null=True)
    raw_materials_prod = models.ForeignKey('RawMaterialsProd', on_delete=models.CASCADE, blank=True, null=True)
    reference = models.TextField(blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'plants_raw_materials_prod'

class PlantScientificName(models.Model):
    plants = models.ForeignKey('Plant', on_delete=models.CASCADE, blank=True, null=True)
    scientific_name = models.ForeignKey('ScientificName', on_delete=models.CASCADE, blank=True, null=True)
    category = models.TextField(blank=True, null=True) #"genus", "species", "cultivar", "variety", "subspecies" only
    reference = models.TextField(blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'plants_scientific_name'

class PlantShadeTolByRegion(models.Model):
    plants = models.ForeignKey('Plant', on_delete=models.CASCADE, blank=True, null=True)
    shade_tol = models.ForeignKey('ShadeTol', on_delete=models.CASCADE, blank=True, null=True)
    regions = models.ForeignKey('Region', on_delete=models.CASCADE, blank=True, null=True)
    reference = models.TextField(blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'plants_shade_tol_by_region'

class PlantSoilDrainageTolByRegion(models.Model):
    plants = models.ForeignKey('Plant', on_delete=models.CASCADE, blank=True, null=True)
    soil_drainage_tol = models.ForeignKey('SoilDrainageTol', on_delete=models.CASCADE, blank=True, null=True)
    regions = models.ForeignKey('Region', on_delete=models.CASCADE, blank=True, null=True)
    reference = models.TextField(blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'plants_soil_drainage_tol_by_region'


# class PlantSpreadAtMaturityByRegion(models.Model):
#     plants = models.ForeignKey('Plant', blank=True, null=True)
#     regions = models.ForeignKey('Region', blank=True, null=True)
#     spread = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

#     class Meta:
#         managed = True
#         db_table = 'plants_spread_at_maturity_by_region'
#         unique_together = (('plants', 'regions'),)

#     def __str__(self):
#         return str(self.spread)


# class PlantRootDepthAtMaturityByRegion(models.Model):
#     plants = models.ForeignKey('Plant', blank=True, null=True)
#     regions = models.ForeignKey('Region', blank=True, null=True)
#     root_depth = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

#     class Meta:
#         managed = True
#         db_table = 'plants_root_depth_at_maturity_by_region'
#         unique_together = (('plants', 'regions'),)

#     def __str__(self):
#         return str(self.spread)

class PlantSunNeedsByRegion(models.Model):
    plants = models.ForeignKey('Plant', on_delete=models.CASCADE, blank=True, null=True)
    regions = models.ForeignKey('Region', on_delete=models.CASCADE, blank=True, null=True)
    sun_needs = models.ForeignKey('SunNeeds', on_delete=models.CASCADE, blank=True, null=True)
    reference = models.TextField(blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'plants_sun_needs_by_region'
        unique_together = (('plants', 'regions'),)


class PlantWaterNeedsByRegion(models.Model):
    plants = models.ForeignKey('Plant', on_delete=models.CASCADE, blank=True, null=True)
    regions = models.ForeignKey('Region', on_delete=models.CASCADE, blank=True, null=True)
    water_needs = models.ForeignKey('WaterNeeds', on_delete=models.CASCADE, blank=True, null=True)
    reference = models.TextField(blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'plants_water_needs_by_region'
        unique_together = (('plants', 'regions'),)


class RawMaterialsProd(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'raw_materials_prod'

    def __str__(self):
        return self.value


class Region(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'regions'

    def __str__(self):
        return self.value


class SaltTol(models.Model):
    value = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'salt_tol'

    def __str__(self):
        return self.value

class ScientificName(models.Model):
    value = models.TextField(blank=True, null=True) #scientific name component (e.g., "Aloe" or "vera" but not "Aloe" "vera")

    class Meta:
        managed = True
        db_table = 'scientific_name'

    def __str__(self):
        return self.value

class Serotiny(models.Model):
    value = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'serotiny'

    def __str__(self):
        return self.value

class DegreeOfSerotiny(models.Model):
    value = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'degree_of_serotiny'

    def __str__(self):
        return self.value

class ImageURL(models.Model):
    plants = models.ForeignKey('Plant', on_delete=models.CASCADE, blank=True, null=True)
    value = models.URLField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'image_urls'

    def __str__(self):
        return self.value

class ShadeTol(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'shade_tol'

    def __str__(self):
        return self.value


class SoilDrainageTol(models.Model):
    value = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'soil_drainage_tol'

    def __str__(self):
        return self.value


class SunNeeds(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sun_needs'

    def __str__(self):
        return self.value


class Toxicity(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'toxicity'

    def __str__(self):
        return self.value


class ToxinRemoval(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'toxin_removal'

    def __str__(self):
        return self.value


# class Transactions(models.Model):
#     timestamp = models.DateTimeField(auto_now=True)
#     #timestamp_add = models.DateTimeField(auto_now_add=True)
#     users = models.ForeignKey('AuthUser')#Users
#     transaction_type = models.TextField(blank=True, null=True)
#     plants_id = models.IntegerField(blank=True, null=True)
#     ignore = models.BooleanField()
# 
#     class Meta:
#         managed = True
#         db_table = 'transactions'
# 
#     def __str__(self):
#         return str(self.plants_id)


class UrlTags(models.Model):
    value = models.TextField(blank=True, null=True)
    plants = models.ForeignKey('Plant', on_delete=models.CASCADE, blank=True, null=True)# related_name='Plants_plant_url_tags_related',

    class Meta:
        managed = True
        db_table = 'url_tags'
        unique_together = (('value', 'plants'),)

    def __str__(self):
        return self.value

#---------------should use django user table--------------------
# class Users(models.Model):
#     username = models.TextField()
#     creation_timestamp = models.DateTimeField()
#     email = models.TextField()
#     enabled = models.BooleanField()
#     real_name = models.TextField()

#     class Meta:
#         managed = True
#         db_table = 'users'

#     def __str__(self):
#         return self.username

class WaterNeeds(models.Model):
    value = models.DecimalField(blank=True, null=True, max_digits=4, decimal_places=2, validators=[MinValueValidator(0, message='amount of water should be more than 0')]) #amount
    units = models.ForeignKey('WaterUnits', on_delete=models.CASCADE, blank=True, null=True)
    frequency = models.ForeignKey('WaterFrequency', on_delete=models.CASCADE, blank=True, null=True)
    season = models.ForeignKey('WaterSeason', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'water_needs'

    def __str__(self):
        return self.value

class WaterUnits(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'water_units'

    def __str__(self):
        return self.value

class WaterFrequency(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'water_frequency'

    def __str__(self):
        return self.value

class WaterSeason(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'water_season'

    def __str__(self):
        return self.value

class WindTol(models.Model):
    value = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'wind_tol'

    def __str__(self):
        return self.value

class PlantRegion(models.Model):
    plants = models.ForeignKey('Plant', on_delete=models.CASCADE, blank=True, null=True)
    regions = models.ForeignKey('Region', on_delete=models.CASCADE, blank=True, null=True)
    height = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    spread = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    root_depth = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    reference = models.TextField(blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'plants_region'
        unique_together = (('plants', 'regions'),)


class Plant(models.Model):
    #-----------------------------id-----------------------------
    # family = models.ForeignKey('Family', on_delete=models.CASCADE, blank=True, null=True) # why foreign keys? why not columns?
    # def get_family(self):
    #     return ','.join([str(a) for a in self.plants_plant_related.all()])
    # family_common_name = models.ForeignKey('FamilyCommonName', on_delete=models.CASCADE, blank=True, null=True) # why foreign keys? why not columns?
    # def get_family_common_name(self):
    #     return ','.join([str(a) for a in self.plants_plant_family_common_name_related.all()])

    family = models.ForeignKey('TheFamily', on_delete=models.CASCADE, blank=True, null=True)
    family_common_name = models.ForeignKey('TheFamilyCommonName', on_delete=models.CASCADE, blank=True, null=True)
    
#     food_prod = models.ManyToManyField(FoodProd, through=PlantFoodProd)
#     @property
#     def get_food_prod(self):
#         return ', '.join([str(a) for a in self.food_prod.all()])
    
    scientific_name = models.ManyToManyField(ScientificName, through=PlantScientificName)
    @property
    def get_scientific_name(self):
        #genus = self.plant_scientific_name.filter(name_component='genus')
        #genus
        #name = all_names
        
        try:
            namecomponents = PlantScientificName.objects.filter(plants=self.id)
        except PlantScientificName.DoesNotExist:
            print('Plant Scientific Name Does not Exist for plant' + str(self.id))
            return None
            
            
        name = ''
        genus = ''
        species = ''
        variety = ''
        subspecies = ''
        cultivar = ''
        for c in namecomponents:
            try:
                if c.category in 'genus':
                    genus = c.scientific_name.value
                elif c.category in 'species':
                    species = c.scientific_name.value
                elif c.category in 'subspecies':
                    subspecies = 'spp. ' + c.scientific_name.value
                elif c.category in 'variety':
                    variety = 'var. ' + c.scientific_name.value
                elif c.category in 'cultivar':
                    subspecies = "cultivar. '" + c.scientific_name.value + "'"
            except:
                print("name object for category " + c.category + " is not in the database.")
                print (c)
                #print(c.category + "  " + c.scientific_name.value)
                
        
        
        if genus is not '':
            name = genus
        if species is not '' or None:
            name = name + " " + species
        if subspecies is not '':
            name = name + " " + subspecies
        if variety is not '':
            name = name + " " + variety
        if cultivar is not '':
            name = name + " " + cultivar
        
        return name
        
    # genus = models.CharField(max_length=160, blank=True, null=True)
    # species = models.CharField(max_length=160, blank=True, null=True)
    # variety = models.CharField(max_length=160, blank=True, null=True)
    common_name = models.CharField(max_length=300, blank=True, null=True)
    #endemic_status
    endemic_status = models.ManyToManyField(EndemicStatus, through=PlantEndemicStatusByRegion)
    @property
    def get_endemic_status(self):
        return ', '.join([str(a) for a in self.endemic_status.all()])

    tags = models.URLField(max_length=160, blank=True, null=True)# CharField
    # urltags = models.ForeignKey('UrlTags', on_delete=models.CASCADE, blank=True, null=True)

    #--------------------------characteristic------------------------
    #duration
    duration = models.ManyToManyField(Duration, through=PlantDurationByRegion)
    @property
    def get_duration(self):
        return ', '.join([str(a) for a in self.duration.all()])

    # 5/2/2017 made life_span into a column on the plant because it doesn't need its own table, added time_to_first_harvest and heattolerance
    life_span = models.DecimalField(db_column='life_span', max_digits=6, decimal_places=2, blank=True, null=True)
    time_to_first_harvest = models.DecimalField(db_column='time_to_first_harvest', max_digits=6, decimal_places=2, blank=True, null=True)


    region = models.ManyToManyField(Region, through=PlantRegion)
    @property
    def get_region(self):
        try:
            pr = PlantRegion.objects.get(plants_id=self.id)
        except PlantRegion.DoesNotExist:
            print('Plant Region Does not Exist for plant' + str(self.id))
            return None

        if pr.height is not None:
            height = float(json.dumps(str(pr.height)).strip('"'));
        else:
            height = None
        if pr.spread is not None:
            spread = float(json.dumps(str(pr.spread)).strip('"'));
        else:
            spread = None
        if pr.root_depth is not None:
            root_depth = float(json.dumps(str(pr.root_depth)).strip('"'));
        else:
            root_depth = None

        return {'height': height, 'spread': spread, 'root_depth': root_depth}
        #return ', '.join([str(a) for a in self.region.all()])

    pH_min = models.DecimalField(db_column='ph_min', max_digits=4, decimal_places=2, blank=True, null=True, validators=[MaxValueValidator(14, message='pH should be in range 0-14')])#, validators=[MinValueValidator(0, message='ph should be in range 0-14')])  # Field name made lowercase. #
    pH_max = models.DecimalField(db_column='ph_max', max_digits=4, decimal_places=2, blank=True, null=True, validators=[MaxValueValidator(14, message='pH should be in range 0-14')])#, validators=[MinValueValidator(0, message='ph should be in range 0-14')])  # Field name made lowercase.
    
    #Layer
    layer = models.ManyToManyField(Layer, through=PlantLayer)#, blank=True, null=True) #not sure testing
    @property
    def get_layer(self):
      return ', '.join([str(a) for a in self.layer.all()])
    #CanopyDensity
    canopy_density = models.ManyToManyField(CanopyDensity, through=PlantCanopyDensityByRegion)
    @property
    def get_canopy_density(self):
        return ', '.join([str(a) for a in self.canopy_density.all()])
    #ActiveGrowthPeriod
    active_growth_period = models.ManyToManyField(ActiveGrowthPeriod, through=PlantActiveGrowthPeriodByRegion)
    @property
    def get_active_growth_period(self):
        return ', '.join([str(a) for a in self.active_growth_period.all()])
    #HarvestPeriod
    harvest_period = models.ManyToManyField(HarvestPeriod, through=PlantHarvestPeriodByRegion)
    @property
    def get_harvest_period(self):
        return ', '.join([str(a) for a in self.harvest_period.all()])
    #LeafRetention
    leaf_retention = models.ManyToManyField(LeafRetention, through=PlantLeafRetentionByRegion)
    @property
    def get_leaf_retention(self):
        return ', '.join([str(a) for a in self.leaf_retention.all()])
    #FlowerColor
    flower_color = models.ManyToManyField(FlowerColor, through=PlantFlowerColor)
    @property
    def get_flower_color(self):
        return ', '.join([str(a) for a in self.flower_color.all()])
    #FoliageColor
    foliage_color = models.ManyToManyField(FoliageColor, through=PlantFoliageColor)
    @property
    def get_foliage_color(self):
        return ', '.join([str(a) for a in self.foliage_color.all()])
    #FruitColor
    fruit_color = models.ManyToManyField(FruitColor, through=PlantFruitColor)
    @property
    def get_fruit_color(self):
        return ', '.join([str(a) for a in self.fruit_color.all()])
    #DegreeofSeritony
    degree_of_serotiny = models.ForeignKey(DegreeOfSerotiny, on_delete=models.CASCADE, blank=True, null=True)

    #--------------------------Tolerance-----------------------------
    #shade_tol
    shade_tol = models.ManyToManyField(ShadeTol, through=PlantShadeTolByRegion)
    @property
    def get_shade_tol(self):
        return ', '.join([str(a) for a in self.shade_tol.all()])
    salt_tol = models.ForeignKey(SaltTol, on_delete=models.CASCADE, blank=True, null=True)
    flood_tol = models.ForeignKey(FloodTol, on_delete=models.CASCADE, blank=True, null=True)
    drought_tol = models.ForeignKey(DroughtTol, on_delete=models.CASCADE, blank=True, null=True)
    humidity_tol = models.ForeignKey(HumidityTol, on_delete=models.CASCADE, blank=True, null=True)
    wind_tol = models.ForeignKey(WindTol, on_delete=models.CASCADE, blank=True, null=True)
    #soil_drainage_tol
    soil_drainage_tol = models.ManyToManyField(SoilDrainageTol, through=PlantSoilDrainageTolByRegion)
    @property
    def get_soil_drainage_tol(self):
        return ', '.join([str(a) for a in self.soil_drainage_tol.all()])

    fire_tol = models.ForeignKey(FireTol, on_delete=models.CASCADE, blank=True, null=True)
    minimum_temperature_tol = models.IntegerField(blank=True, null=True)
    heat_tol = models.IntegerField(blank=True, null=True)

    #-------------------------needs--------------------------------
    #nutrientRequirements
    nutrient_requirements = models.ManyToManyField(NutrientRequirements, through=PlantNutrientRequirementsByRegion, verbose_name='nutrient requirements')
    @property
    def get_nutrient_requirements(self):
        return ',' .join([str(a) for a in self.nutrient_requirements.all()])
    #WaterNeeds
    water_needs = models.ManyToManyField(WaterNeeds, through=PlantWaterNeedsByRegion)
    @property
    def get_water_needs(self):
        return ', '.join([str(a) for a in self.water_needs.all()])

    inoculant = models.CharField(max_length=160, blank=True, null=True)
    #SunNeeds
    sun_needs = models.ManyToManyField(SunNeeds, through=PlantSunNeedsByRegion)
    @property
    def get_sun_needs(self):
        return ', '.join([str(a) for a in self.sun_needs.all()])

    serotiny = models.ForeignKey(Serotiny, on_delete=models.CASCADE, blank=True, null=True)

    #-------------------------products----------------------------
    allelochemicals = models.CharField(max_length=160, blank=True, null=True)
    #FoodProd
    food_prod = models.ManyToManyField(FoodProd, through=PlantFoodProd)
    @property
    def get_food_prod(self):
        return ', '.join([str(a) for a in self.food_prod.all()])
    #AnimalFood
    animal_food = models.ManyToManyField(AnimalFood, through=PlantAnimalFood, verbose_name='animal food')
    @property
    def get_animal_food(self):
        return ','.join([str(a) for a in self.animal_food.all()])
    #RawMaterialsProd
    raw_materials_prod = models.ManyToManyField(RawMaterialsProd, through=PlantRawMaterialsProd, verbose_name='raw materials')
    @property
    def get_raw_materials_prod(self):
        return ', '.join([str(a) for a in self.raw_materials_prod.all()])
    #MedicinalsProd
    medicinals_prod = models.ManyToManyField(MedicinalsProd, through=PlantMedicinalsProd, verbose_name='medicinals')
    @property
    def get_medicinals_prod(self):
        return ', '.join([str(a) for a in self.medicinals_prod.all()])
    #BiochemicalMaterialProd
    biochemical_material_prod = models.ManyToManyField(BiochemicalMaterialProd, through=PlantBiochemicalMaterialProd, verbose_name='biochemical materials')
    @property
    def get_biochemical_material_prod(self):
        return ', '.join([str(a) for a in self.biochemical_material_prod.all()])
    #CulturalAndAmenityProd
    cultural_and_amenity_prod = models.ManyToManyField(CulturalAndAmenityProd, through=PlantCulturalAndAmenityProd, verbose_name='cultrual and amenity')
    @property
    def get_cultural_and_amenity_prod(self):
        return ', '.join([str(a) for a in self.cultural_and_amenity_prod.all()])
    #MineralNutrientsProd
    mineral_nutrients_prod = models.ManyToManyField(MineralNutrientsProd, through=PlantMineralNutrientsProd, verbose_name='mineral nutrients')
    
    @property
    def get_mineral_nutrients_prod(self):
        return ', '.join([str(a) for a in self.mineral_nutrients_prod.all()])

    #------------------------behavior---------------------------
    #barrier
    barrier = models.ManyToManyField(Barrier, through=PlantBarrierByRegion)#ByRegion
    @property
    def get_barrier(self):
        return ','.join([str(a) for a in self.barrier.all()])
    #erosion_control
    erosion_control = models.ManyToManyField(ErosionControl, through=PlantErosionControlByRegion)
    @property
    def get_erosion_control(self):
        return ', '.join([str(a) for a in self.erosion_control.all()])
    #plants_insect_attractor
    plants_insect_attractor = models.ManyToManyField(Insects, through=PlantInsectAttractorByRegion, related_name='a_plants_insect_attractor_related')
    @property
    def get_plants_insect_attractor(self):
        return ', '.join([str(a) for a in self.plants_insect_attractor.all()])
    #plants_insect_regulator
    plants_insect_regulator = models.ManyToManyField(Insects, through=PlantInsectRegulatorByRegion)
    @property
    def get_plants_insect_regulator(self):
        return ', '.join([str(a) for a in self.plants_insect_regulator.all()])
    #plants_animal_regulator
    plants_animal_regulator = models.ManyToManyField(Animals, through=PlantAnimalRegulatorByRegion)
    @property
    def get_plants_animal_regulator(self):
        return ', '.join([str(a) for a in self.plants_animal_regulator.all()])
    #plants_animal_attractor
    plants_animal_attractor = models.ManyToManyField(Animals, through=PlantAnimalAttractorByRegion, related_name='a_plants_animal_attractor_related')
    @property
    def get_plants_animal_attractor(self):
        return ', '.join([str(a) for a in self.plants_animal_attractor.all()])

    livestock_bloat = models.ForeignKey(LivestockBloat, on_delete=models.CASCADE, blank=True, null=True)
    toxicity = models.ForeignKey('Toxicity', on_delete=models.CASCADE, blank=True, null=True)


    toxin_removal = models.ForeignKey(ToxinRemoval, on_delete=models.CASCADE, blank=True, null=True)
    #life_span = models.ForeignKey(life_span, on_delete=models.CASCADE, blank=True, null=True)
    allelopathic = models.ForeignKey(Allelopathic, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'plants'

    def __str__(self):
        if self.common_name:
            return self.common_name
        else:
            return self.get_scientific_name
    @property
    def get_all_fields(self):
        fields = []

        for f in self._meta.get_fields():
            fname = f.name
            get_choice = 'get_' + fname 
            # if hasattr(self, get_choice)():
            #    value = getattr(self, get_choice)()
            # else:
            #     try:
            #         value = getattr(self, fname)
            #     except User.DoesNotExist:
            #         value = None
            if hasattr(self, get_choice):
                value = getattr(self, get_choice)
            else:
                try:
                    value = getattr(self, fname)
                except:
                    value = "DOESNT HAVE"

            if f.many_to_many:
                
                fields.append({'label':f.verbose_name, 'name':f.name, 'value':value, 'field_type':'many_to_many',})
            elif f.many_to_one:
                fields.append({'label':f.verbose_name, 'name':f.name, 'value':value, 'field_type':'many_to_one'})
            #many to many fields are repeated with one_to_many fields
            #elif f.one_to_many:
            #    fields.append({'label':'onetomany', 'name':f.name, 'value':'test', 'field_type':'one_to_many'})
            #elif f.one_to_one:
            #    fields.append({'label':'onetoone', 'name':f.name, 'value':value, 'field_type':'one_to_one'})
            elif not f.one_to_many:
                fields.append({'label':f.verbose_name, 'name':f.name, 'value':value,'field_type':'other'})
            
            
            # fields.append({'label':f.vebose_name, 'name':f.name, 'value':value,})
        return fields

    def get_absolute_url(self):
        return "/edit/%i/" % self.id