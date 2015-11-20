# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Actions(models.Model):
    transactions = models.ForeignKey('Transactions', blank=True, null=True)
    action_type = models.TextField()
    regions = models.ForeignKey('Region', blank=True, null=True)
    property = models.TextField()
    value = models.TextField(blank=True, null=True)
    citation = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actions'

    def __str__(self):
        return self.value


class ActiveGrowthPeriod(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'active_growth_period'

    def __str__(self):
        return self.value


class Allelopathic(models.Model):
    value = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'allelopathic'

    def __str__(self):
        return self.value


class Animals(models.Model):
    value = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'animals'

    def __str__(self):
        return self.value


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BiochemicalMaterialProd(models.Model):
    id = models.IntegerField(primary_key=True)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'biochemical_material_prod'

    def __str__(self):
        return self.value


class CanopyDensity(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'canopy_density'

    def __str__(self):
        return self.value


class CulturalAndAmenityProd(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cultural_and_amenity_prod'

    def __str__(self):
        return self.value


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DroughtTol(models.Model):
    value = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'drought_tol'

    def __str__(self):
    	return self.value


class Duration(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'duration'

    def __str__(self):
    	return self.value


class EndemicStatus(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'endemic_status'

    def __str__(self):
    	return self.value


class ErosionControl(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'erosion_control'

    def __str__(self):
    	return self.value


class Family(models.Model):
    value = models.CharField(max_length=160, blank=True, null=True)
    plants = models.ForeignKey('Plant', related_name='plants_plant_related',blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'family'
        #unique_together = (('value', 'plants'),)

    def __str__(self):
    	return self.value


class FamilyCommonName(models.Model):
    value = models.CharField(max_length=160, blank=True, null=True)
    plants = models.ForeignKey('Plant', related_name='plants_plant_family_common_name_related',blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'family_common_name'
        unique_together = (('value', 'plants'),)

    def __str__(self):
    	return self.value


class FertilityNeeds(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fertility_needs'

    def __str__(self):
    	return self.value


class FireTol(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fire_tol'

    def __str__(self):
    	return self.value


class FloodTol(models.Model):
    value = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flood_tol'

    def __str__(self):
    	return self.value


class FlowerColor(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flower_color'

    def __str__(self):
    	return self.value


class FoliageColor(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'foliage_color'

    def __str__(self):
    	return self.value


class FoodProd(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'food_prod'

    def __str__(self):
    	return self.value


class FruitColor(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fruit_color'

    def __str__(self):
    	return self.value


class HarvestPeriod(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'harvest_period'

    def __str__(self):
    	return self.value


class HumidityTol(models.Model):
    value = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'humidity_tol'

    def __str__(self):
    	return self.value


class Insects(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'insects'

    def __str__(self):
    	return self.value


class Layer(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'layer'

    def __str__(self):
    	return self.value


class LeafRetention(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leaf_retention'

    def __str__(self):
    	return self.value


class Lifespan(models.Model):
    value = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lifespan'

    def __str__(self):
    	return self.value


class LivestockBloat(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'livestock_bloat'

    def __str__(self):
    	return self.value


class MedicinalsProd(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medicinals_prod'

    def __str__(self):
    	return self.value


class MineralNutrientsProd(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mineral_nutrients_prod'

    def __str__(self):
    	return self.value


class Plant(models.Model):
    #-----------------------------id-----------------------------
    # family = models.ForeignKey('Family', blank=True, null=True) # why foreign keys? why not columns?
    # def get_family(self):
    #     return ','.join([str(a) for a in self.plants_plant_related.all()])
    # family_common_name = models.ForeignKey('FamilyCommonName', blank=True, null=True) # why foreign keys? why not columns?
    # def get_family_common_name(self):
    #     return ','.join([str(a) for a in self.plants_plant_family_common_name_related.all()])
    genus = models.CharField(max_length=160, blank=True, null=True)
    species = models.CharField(max_length=160, blank=True, null=True)
    variety = models.CharField(max_length=160, blank=True, null=True)
    common_name = models.CharField(max_length=160, blank=True, null=True)
    #endemic_status
    endemic_status = models.ManyToManyField(EndemicStatus, through='PlantEndemicStatusByRegion')
    def get_endemic_status(self):
        return ','.join([str(a) for a in self.endemic_status.all()])

    tags = models.CharField(max_length=160, blank=True, null=True)
    # urltags = models.ForeignKey('UrlTags', blank=True, null=True)

    #--------------------------characteristic------------------------
    #duration
    duration = models.ManyToManyField('Duration', through='PlantDurationByRegion')
    def get_duration(self):
        return ','.join([str(a) for a in self.duration.all()])
    #height
    height = models.ManyToManyField('PlantHeightAtMaturityByRegion')
    def get_height(self):
        return ','.join([str(a) for a in self.height.all()])# ???????????????????????????
    #spread
    spread = models.ManyToManyField('PlantSpreadAtMaturityByRegion')
    def get_spread(self):
        return ','.join([str(a) for a in self.spread.all()])# ???????????????????????????

    ph_min = models.DecimalField(db_column='pH_min', max_digits=6, decimal_places=4, blank=True, null=True, validators=[MaxValueValidator(14, message='pH should be in range 0-14')])#, validators=[MinValueValidator(0, message='pH should be in range 0-14')])  # Field name made lowercase. #
    ph_max = models.DecimalField(db_column='pH_max', max_digits=6, decimal_places=4, blank=True, null=True, validators=[MaxValueValidator(14, message='pH should be in range 0-14')])#, validators=[MinValueValidator(0, message='pH should be in range 0-14')])  # Field name made lowercase.
    layer = models.ManyToManyField(Layer, through='PlantLayer')#, blank=True, null=True) #not sure testing
    def get_layer(self):
    	return ','.join([str(a) for a in self.layer.all()])
    #CanopyDensity
    canopy_density = models.ManyToManyField(CanopyDensity, through='PlantCanopyDensityByRegion')
    def get_canopy_density(self):
        return ','.join([str(a) for a in self.canopy_density.all()])
    #ActiveGrowthPeriod
    active_growth_period = models.ManyToManyField(ActiveGrowthPeriod, through='PlantActiveGrowthPeriodByRegion')
    def get_active_growth_period(self):
        return ','.join([str(a) for a in self.active_growth_period.all()])
    #HarvestPeriod
    harvest_period = models.ManyToManyField(HarvestPeriod, through='PlantHarvestPeriodByRegion')
    def get_harvest_period(self):
        return ','.join([str(a) for a in self.harvest_period.all()])
    #LeafRetention
    leaf_retention = models.ManyToManyField(LeafRetention, through='PlantLeafRetentionByRegion')
    def get_leaf_retention(self):
        return ','.join([str(a) for a in self.leaf_retention.all()])
    #FlowerColor
    flower_color = models.ManyToManyField(FlowerColor, through='PlantFlowerColor')
    def get_flower_color(self):
        return ','.join([str(a) for a in self.flower_color.all()])
    #FoliageColor
    foliage_color = models.ManyToManyField(FoliageColor, through='PlantFoliageColor')
    def get_foliage_color(self):
        return ','.join([str(a) for a in self.foliage_color.all()])
    #FruitColor
    fruit_color = models.ManyToManyField(FruitColor, through='PlantFruitColor')
    def get_fruit_color(self):
        return ','.join([str(a) for a in self.fruit_color.all()])

    #--------------------------Tolerance-----------------------------
    #shade_tol
    shade_tol = models.ManyToManyField('ShadeTol', through='PlantShadeTolByRegion')
    def get_shade_tol(self):
        return ','.join([str(a) for a in self.shade_tol.all()])
    salt_tol = models.ForeignKey('SaltTol', blank=True, null=True)
    flood_tol = models.ForeignKey('FloodTol', blank=True, null=True)
    drought_tol = models.ForeignKey('DroughtTol', blank=True, null=True)
    humidity_tol = models.ForeignKey('HumidityTol', blank=True, null=True)
    wind_tol = models.ForeignKey('WindTol', blank=True, null=True)
    #soil_drainage_tol
    soil_drainage_tol = models.ManyToManyField('SoilDrainageTol', through='PlantSoilDrainageTolByRegion')
    def get_soil_drainage_tol(self):
        return ','.join([str(a) for a in self.soil_drainage_tol.all()])

    fire_tol = models.ForeignKey('FireTol', blank=True, null=True)
    minimum_temperature_tol = models.IntegerField(blank=True, null=True)

    #-------------------------needs--------------------------------
    #FertilityNeeds
    fertility_needs = models.ManyToManyField(FertilityNeeds, through='PlantFertilityNeedsByRegion')
    def get_fertility_needs(self):
        return ','.join([str(a) for a in self.fertility_needs.all()])
    #WaterNeeds
    water_needs = models.ManyToManyField('WaterNeeds', through='PlantWaterNeedsByRegion')
    def get_water_needs(self):
        return ','.join([str(a) for a in self.water_needs.all()])

    innoculant = models.CharField(max_length=160, blank=True, null=True)
    #SunNeeds
    sun_needs = models.ManyToManyField('SunNeeds', through='PlantSunNeedsByRegion')
    def get_sun_needs(self):
        return ','.join([str(a) for a in self.sun_needs.all()])

    #-------------------------products----------------------------
    #FoodProd
    food_prod = models.ManyToManyField(FoodProd, through='PlantFoodProd')
    def get_food_prod(self):
        return ','.join([str(a) for a in self.food_prod.all()])
    #RawMaterialsProd
    raw_materials_prod = models.ManyToManyField('RawMaterialsProd', through='PlantRawMaterialsProd')
    def get_raw_materials_prod(self):
        return ','.join([str(a) for a in self.raw_materials_prod.all()])
    #MedicinalsProd
    medicinals_prod = models.ManyToManyField(MedicinalsProd, through='PlantMedicinalsProd')
    def get_medicinals_prod(self):
        return ','.join([str(a) for a in self.medicinals_prod.all()])
    #BiochemicalMaterialProd
    biochemical_material_prod = models.ManyToManyField(BiochemicalMaterialProd, through='PlantBiochemicalMaterialProd')
    def get_biochemical_material_prod(self):
        return ','.join([str(a) for a in self.biochemical_material_prod.all()])
    #CulturalAndAmenityProd
    cultural_and_amenity_prod = models.ManyToManyField(CulturalAndAmenityProd, through='PlantCulturalAndAmenityProd')
    def get_cultural_and_amenity_prod(self):
        return ','.join([str(a) for a in self.cultural_and_amenity_prod.all()])
    #MineralNutrientsProd
    mineral_nutrients_prod = models.ManyToManyField(MineralNutrientsProd, through='PlantMineralNutrientsProd')
    def get_mineral_nutrients_prod(self):
        return ','.join([str(a) for a in self.mineral_nutrients_prod.all()])

    #------------------------behavior---------------------------
    #erosion_control
    erosion_control = models.ManyToManyField(ErosionControl, through='PlantErosionControlByRegion')
    def get_erosion_control(self):
        return ','.join([str(a) for a in self.erosion_control.all()])
    #plants_insect_attractor
    plants_insect_attractor = models.ManyToManyField(Insects, through='PlantInsectAttractorByRegion', related_name='a_plants_insect_attractor_related')
    def get_insect_attractor(self):
        return ','.join([str(a) for a in self.plants_insect_attractor.all()])
    #plants_insect_regulator
    plants_insect_regulator = models.ManyToManyField(Insects, through='PlantInsectRegulatorByRegion')
    def get_insect_regulator(self):
        return ','.join([str(a) for a in self.plants_insect_regulator.all()])
    #plants_animal_regulator
    plants_animal_regulator = models.ManyToManyField(Animals, through='PlantAnimalRegulatorByRegion')
    def get_animal_regulator(self):
        return ','.join([str(a) for a in self.plants_animal_regulator.all()])
    #plants_animal_attractor
    plants_animal_attractor = models.ManyToManyField(Animals, through='PlantAnimalAttractorByRegion', related_name='a_plants_animal_attractor_related')
    def get_animal_attractor(self):
        return ','.join([str(a) for a in self.plants_animal_attractor.all()])

    livestock_bloat = models.ForeignKey(LivestockBloat, blank=True, null=True)
    toxicity = models.ForeignKey('Toxicity', blank=True, null=True)

    #------------------------not in schema----------------------
    toxin_removal = models.ForeignKey('ToxinRemoval', blank=True, null=True)
    lifespan = models.ForeignKey(Lifespan, blank=True, null=True)
    allelopathic = models.ForeignKey(Allelopathic, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'plants'

    def __str__(self):
        if self.common_name:
            return self.common_name
        else:
            return self.genus


class PlantActiveGrowthPeriodByRegion(models.Model):
    plants = models.ForeignKey(Plant, blank=True, null=True)
    active_growth_period = models.ForeignKey(ActiveGrowthPeriod, blank=True, null=True)
    regions = models.ForeignKey('Region', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plants_active_growth_period_by_region'


class PlantAnimalAttractorByRegion(models.Model):
    plants = models.ForeignKey(Plant, blank=True, null=True)
    animals = models.ForeignKey(Animals, blank=True, null=True)
    regions = models.ForeignKey('Region', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plants_animal_attractor_by_region'


class PlantAnimalRegulatorByRegion(models.Model):
    plants = models.ForeignKey(Plant, blank=True, null=True)
    animals = models.ForeignKey(Animals, blank=True, null=True)
    regions = models.ForeignKey('Region', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plants_animal_regulator_by_region'


class PlantBiochemicalMaterialProd(models.Model):
    plants = models.ForeignKey(Plant, blank=True, null=True)
    biochemical_material_prod = models.ForeignKey(BiochemicalMaterialProd, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plants_biochemical_material_prod'


class PlantCanopyDensityByRegion(models.Model):
    plants = models.ForeignKey(Plant, blank=True, null=True)
    regions = models.ForeignKey('Region', blank=True, null=True)
    canopy_density = models.ForeignKey(CanopyDensity, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plants_canopy_density_by_region'
        unique_together = (('plants', 'regions'),)


class PlantCulturalAndAmenityProd(models.Model):
    plants = models.ForeignKey(Plant, blank=True, null=True)
    cultural_and_amenity_prod = models.ForeignKey(CulturalAndAmenityProd, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plants_cultural_and_amenity_prod'


class PlantDurationByRegion(models.Model):
    plants = models.ForeignKey(Plant, blank=True, null=True)
    regions = models.ForeignKey('Region', blank=True, null=True)
    duration = models.ForeignKey(Duration, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plants_duration_by_region'
        unique_together = (('plants', 'regions'),)


class PlantEndemicStatusByRegion(models.Model):
    plants = models.ForeignKey(Plant, blank=True, null=True)
    endemic_status = models.ForeignKey(EndemicStatus, blank=True, null=True)
    regions = models.ForeignKey('Region', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plants_endemic_status_by_region'


class PlantErosionControlByRegion(models.Model):
    plants = models.ForeignKey(Plant, blank=True, null=True)
    regions = models.ForeignKey('Region', blank=True, null=True)
    erosion_control = models.ForeignKey(ErosionControl, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plants_erosion_control_by_region'
        unique_together = (('plants', 'regions'),)


class PlantFertilityNeedsByRegion(models.Model):
    plants = models.ForeignKey(Plant, blank=True, null=True)
    regions = models.ForeignKey('Region', blank=True, null=True)
    fertility_needs = models.ForeignKey(FertilityNeeds, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plants_fertility_needs_by_region'
        unique_together = (('plants', 'regions'),)


class PlantFlowerColor(models.Model):
    plants = models.ForeignKey(Plant, blank=True, null=True)
    flower_color = models.ForeignKey(FlowerColor, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plants_flower_color'


class PlantFoliageColor(models.Model):
    plants = models.ForeignKey(Plant, blank=True, null=True)
    foliage_color = models.ForeignKey(FoliageColor, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plants_foliage_color'


class PlantFoodProd(models.Model):
    plants = models.ForeignKey(Plant, blank=True, null=True)
    food_prod = models.ForeignKey(FoodProd, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plants_food_prod'


class PlantFruitColor(models.Model):
    plants = models.ForeignKey(Plant, blank=True, null=True)
    fruit_color = models.ForeignKey(FruitColor, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plants_fruit_color'


class PlantHarvestPeriodByRegion(models.Model):
    plants = models.ForeignKey(Plant, blank=True, null=True)
    harvest_period = models.ForeignKey(HarvestPeriod, blank=True, null=True)
    regions = models.ForeignKey('Region', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plants_harvest_period_by_region'


class PlantHeightAtMaturityByRegion(models.Model):
    plants = models.ForeignKey(Plant, blank=True, null=True)
    regions = models.ForeignKey('Region', blank=True, null=True)
    height = models.DecimalField(max_digits=8, decimal_places=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plants_height_at_maturity_by_region'
        unique_together = (('plants', 'regions'),)

    # def __str__(self):
    #     return str(self.height)


class PlantInsectAttractorByRegion(models.Model):
    plants = models.ForeignKey(Plant, blank=True, null=True)
    insects = models.ForeignKey(Insects, blank=True, null=True)
    regions = models.ForeignKey('Region', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plants_insect_attractor_by_region'

    # def __str__(self):
    #     return self.insects


class PlantInsectRegulatorByRegion(models.Model):
    plants = models.ForeignKey(Plant, blank=True, null=True)
    insects = models.ForeignKey(Insects, blank=True, null=True)
    regions = models.ForeignKey('Region', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plants_insect_regulator_by_region'


class PlantLayer(models.Model):
    plants = models.ForeignKey(Plant, blank=True, null=True)
    layer = models.ForeignKey(Layer, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plants_layer'

    def __str__(self):
        return str(self.plants)


class PlantLeafRetentionByRegion(models.Model):
    plants = models.ForeignKey(Plant, blank=True, null=True)
    regions = models.ForeignKey('Region', blank=True, null=True)
    leaf_retention = models.ForeignKey(LeafRetention, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plants_leaf_retention_by_region'
        unique_together = (('plants', 'regions'),)


class PlantMedicinalsProd(models.Model):
    plants = models.ForeignKey(Plant, blank=True, null=True)
    medicinals_prod = models.ForeignKey(MedicinalsProd, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plants_medicinals_prod'


class PlantMineralNutrientsProd(models.Model):
    plants = models.ForeignKey(Plant, blank=True, null=True)
    mineral_nutrients_prod = models.ForeignKey(MineralNutrientsProd, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plants_mineral_nutrients_prod'


class PlantRawMaterialsProd(models.Model):
    plants = models.ForeignKey(Plant, blank=True, null=True)
    raw_materials_prod = models.ForeignKey('RawMaterialsProd', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plants_raw_materials_prod'


class PlantShadeTolByRegion(models.Model):
    plants = models.ForeignKey(Plant, blank=True, null=True)
    shade_tol = models.ForeignKey('ShadeTol', blank=True, null=True)
    regions = models.ForeignKey('Region', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plants_shade_tol_by_region'


class PlantSoilDrainageTolByRegion(models.Model):
    plants = models.ForeignKey(Plant, blank=True, null=True)
    soil_drainage_tol = models.ForeignKey('SoilDrainageTol', blank=True, null=True)
    regions = models.ForeignKey('Region', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plants_soil_drainage_tol_by_region'


class PlantSpreadAtMaturityByRegion(models.Model):
    plants = models.ForeignKey(Plant, blank=True, null=True)
    regions = models.ForeignKey('Region', blank=True, null=True)
    spread = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plants_spread_at_maturity_by_region'
        unique_together = (('plants', 'regions'),)

    def __str__(self):
        return str(self.spread)


class PlantSunNeedsByRegion(models.Model):
    plants = models.ForeignKey(Plant, blank=True, null=True)
    regions = models.ForeignKey('Region', blank=True, null=True)
    sun_needs = models.ForeignKey('SunNeeds', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plants_sun_needs_by_region'
        unique_together = (('plants', 'regions'),)


class PlantWaterNeedsByRegion(models.Model):
    plants = models.ForeignKey(Plant, blank=True, null=True)
    regions = models.ForeignKey('Region', blank=True, null=True)
    water_needs = models.ForeignKey('WaterNeeds', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plants_water_needs_by_region'
        unique_together = (('plants', 'regions'),)


class RawMaterialsProd(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'raw_materials_prod'

    def __str__(self):
    	return self.value


class Region(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regions'

    def __str__(self):
    	return self.value


class SaltTol(models.Model):
    value = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salt_tol'

    def __str__(self):
    	return self.value


class ShadeTol(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shade_tol'

    def __str__(self):
    	return self.value


class SoilDrainageTol(models.Model):
    value = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'soil_drainage_tol'

    def __str__(self):
    	return self.value


class SunNeeds(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sun_needs'

    def __str__(self):
    	return self.value


class Toxicity(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'toxicity'

    def __str__(self):
    	return self.value


class ToxinRemoval(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'toxin_removal'

    def __str__(self):
    	return self.value


class Transactions(models.Model):
    timestamp = models.DateTimeField()
    users = models.ForeignKey('Users')
    transaction_type = models.TextField(blank=True, null=True)
    plants_id = models.IntegerField(blank=True, null=True)
    ignore = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'transactions'

    def __str__(self):
    	return str(self.plants_id)


class UrlTags(models.Model):
    value = models.TextField(blank=True, null=True)
    plants = models.ForeignKey('Plant', related_name='Plants_plant_url_tags_related', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'url_tags'
        unique_together = (('value', 'plants'),)

    def __str__(self):
    	return self.value

#---------------should use django user table--------------------
class Users(models.Model):
    username = models.TextField()
    creation_timestamp = models.DateTimeField()
    email = models.TextField()
    enabled = models.BooleanField()
    real_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'users'

    def __str__(self):
    	return self.username


class WaterNeeds(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'water_needs'

    def __str__(self):
    	return self.value


class WindTol(models.Model):
    value = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wind_tol'

    def __str__(self):
    	return self.value
