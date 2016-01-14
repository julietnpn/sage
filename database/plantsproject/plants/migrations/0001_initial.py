# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('action_type', models.TextField()),
                ('property', models.TextField()),
                ('value', models.TextField(blank=True, null=True)),
                ('citation', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'actions',
            },
        ),
        migrations.CreateModel(
            name='ActiveGrowthPeriod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('value', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'active_growth_period',
            },
        ),
        migrations.CreateModel(
            name='Allelopathic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('value', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'allelopathic',
            },
        ),
        migrations.CreateModel(
            name='Animals',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('value', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'animals',
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(unique=True, max_length=80)),
            ],
            options={
                'managed': True,
                'db_table': 'auth_group',
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(unique=True, max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'managed': True,
                'db_table': 'auth_user',
            },
        ),
        migrations.CreateModel(
            name='BiochemicalMaterialProd',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('value', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'biochemical_material_prod',
            },
        ),
        migrations.CreateModel(
            name='CanopyDensity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('value', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'canopy_density',
            },
        ),
        migrations.CreateModel(
            name='CulturalAndAmenityProd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('value', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'cultural_and_amenity_prod',
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'managed': True,
                'db_table': 'django_admin_log',
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'managed': True,
                'db_table': 'django_content_type',
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'managed': True,
                'db_table': 'django_migrations',
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(primary_key=True, max_length=40, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'managed': True,
                'db_table': 'django_session',
            },
        ),
        migrations.CreateModel(
            name='DroughtTol',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('value', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'drought_tol',
            },
        ),
        migrations.CreateModel(
            name='Duration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('value', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'duration',
            },
        ),
        migrations.CreateModel(
            name='EndemicStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('value', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'endemic_status',
            },
        ),
        migrations.CreateModel(
            name='ErosionControl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('value', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'erosion_control',
            },
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('value', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'family',
            },
        ),
        migrations.CreateModel(
            name='FamilyCommonName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('value', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'family_common_name',
            },
        ),
        migrations.CreateModel(
            name='FertilityNeeds',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('value', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'fertility_needs',
            },
        ),
        migrations.CreateModel(
            name='FireTol',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('value', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'fire_tol',
            },
        ),
        migrations.CreateModel(
            name='FloodTol',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('value', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'flood_tol',
            },
        ),
        migrations.CreateModel(
            name='FlowerColor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('value', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'flower_color',
            },
        ),
        migrations.CreateModel(
            name='FoliageColor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('value', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'foliage_color',
            },
        ),
        migrations.CreateModel(
            name='FoodProd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('value', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'food_prod',
            },
        ),
        migrations.CreateModel(
            name='FruitColor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('value', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'fruit_color',
            },
        ),
        migrations.CreateModel(
            name='HarvestPeriod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('value', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'harvest_period',
            },
        ),
        migrations.CreateModel(
            name='HumidityTol',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('value', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'humidity_tol',
            },
        ),
        migrations.CreateModel(
            name='Insects',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('value', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'insects',
            },
        ),
        migrations.CreateModel(
            name='Layer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('value', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'layer',
            },
        ),
        migrations.CreateModel(
            name='LeafRetention',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('value', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'leaf_retention',
            },
        ),
        migrations.CreateModel(
            name='Lifespan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('value', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'lifespan',
            },
        ),
        migrations.CreateModel(
            name='LivestockBloat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('value', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'livestock_bloat',
            },
        ),
        migrations.CreateModel(
            name='MedicinalsProd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('value', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'medicinals_prod',
            },
        ),
        migrations.CreateModel(
            name='MineralNutrientsProd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('value', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'mineral_nutrients_prod',
            },
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('genus', models.CharField(null=True, blank=True, max_length=160)),
                ('species', models.CharField(null=True, blank=True, max_length=160)),
                ('variety', models.CharField(null=True, blank=True, max_length=160)),
                ('common_name', models.CharField(null=True, blank=True, max_length=160)),
                ('ph_min', models.DecimalField(decimal_places=65535, blank=True, null=True, max_digits=65535, db_column='pH_min')),
                ('ph_max', models.DecimalField(decimal_places=65535, blank=True, null=True, max_digits=65535, db_column='pH_max')),
                ('minimum_temperature_tol', models.IntegerField(blank=True, null=True)),
                ('innoculant', models.CharField(null=True, blank=True, max_length=160)),
                ('allelopathic', models.ForeignKey(blank=True, null=True, to='plants.Allelopathic')),
                ('drought_tol', models.ForeignKey(blank=True, null=True, to='plants.DroughtTol')),
                ('fire_tol', models.ForeignKey(blank=True, null=True, to='plants.FireTol')),
                ('flood_tol', models.ForeignKey(blank=True, null=True, to='plants.FloodTol')),
                ('humidity_tol', models.ForeignKey(blank=True, null=True, to='plants.HumidityTol')),
            ],
            options={
                'managed': True,
                'db_table': 'plants',
            },
        ),
        migrations.CreateModel(
            name='PlantActiveGrowthPeriodByRegion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('active_growth_period', models.ForeignKey(blank=True, null=True, to='plants.ActiveGrowthPeriod')),
                ('plants', models.ForeignKey(blank=True, null=True, to='plants.Plant')),
            ],
            options={
                'managed': True,
                'db_table': 'plants_active_growth_period_by_region',
            },
        ),
        migrations.CreateModel(
            name='PlantAnimalAttractorByRegion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('animals', models.ForeignKey(blank=True, null=True, to='plants.Animals')),
                ('plants', models.ForeignKey(blank=True, null=True, to='plants.Plant')),
            ],
            options={
                'managed': True,
                'db_table': 'plants_animal_attractor_by_region',
            },
        ),
        migrations.CreateModel(
            name='PlantAnimalRegulatorByRegion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('animals', models.ForeignKey(blank=True, null=True, to='plants.Animals')),
                ('plants', models.ForeignKey(blank=True, null=True, to='plants.Plant')),
            ],
            options={
                'managed': True,
                'db_table': 'plants_animal_regulator_by_region',
            },
        ),
        migrations.CreateModel(
            name='PlantBiochemicalMaterialProd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('biochemical_material_prod', models.ForeignKey(blank=True, null=True, to='plants.BiochemicalMaterialProd')),
                ('plants', models.ForeignKey(blank=True, null=True, to='plants.Plant')),
            ],
            options={
                'managed': True,
                'db_table': 'plants_biochemical_material_prod',
            },
        ),
        migrations.CreateModel(
            name='PlantCanopyDensityByRegion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('canopy_density', models.ForeignKey(blank=True, null=True, to='plants.CanopyDensity')),
                ('plants', models.ForeignKey(blank=True, null=True, to='plants.Plant')),
            ],
            options={
                'managed': True,
                'db_table': 'plants_canopy_density_by_region',
            },
        ),
        migrations.CreateModel(
            name='PlantCulturalAndAmenityProd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('cultural_and_amenity_prod', models.ForeignKey(blank=True, null=True, to='plants.CulturalAndAmenityProd')),
                ('plants', models.ForeignKey(blank=True, null=True, to='plants.Plant')),
            ],
            options={
                'managed': True,
                'db_table': 'plants_cultural_and_amenity_prod',
            },
        ),
        migrations.CreateModel(
            name='PlantDurationByRegion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('duration', models.ForeignKey(blank=True, null=True, to='plants.Duration')),
                ('plants', models.ForeignKey(blank=True, null=True, to='plants.Plant')),
            ],
            options={
                'managed': True,
                'db_table': 'plants_duration_by_region',
            },
        ),
        migrations.CreateModel(
            name='PlantEndemicStatusByRegion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('endemic_status', models.ForeignKey(blank=True, null=True, to='plants.EndemicStatus')),
                ('plants', models.ForeignKey(blank=True, null=True, to='plants.Plant')),
            ],
            options={
                'managed': True,
                'db_table': 'plants_endemic_status_by_region',
            },
        ),
        migrations.CreateModel(
            name='PlantErosionControlByRegion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('erosion_control', models.ForeignKey(blank=True, null=True, to='plants.ErosionControl')),
                ('plants', models.ForeignKey(blank=True, null=True, to='plants.Plant')),
            ],
            options={
                'managed': True,
                'db_table': 'plants_erosion_control_by_region',
            },
        ),
        migrations.CreateModel(
            name='PlantFertilityNeedsByRegion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('fertility_needs', models.ForeignKey(blank=True, null=True, to='plants.FertilityNeeds')),
                ('plants', models.ForeignKey(blank=True, null=True, to='plants.Plant')),
            ],
            options={
                'managed': True,
                'db_table': 'plants_fertility_needs_by_region',
            },
        ),
        migrations.CreateModel(
            name='PlantFlowerColor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('flower_color', models.ForeignKey(blank=True, null=True, to='plants.FlowerColor')),
                ('plants', models.ForeignKey(blank=True, null=True, to='plants.Plant')),
            ],
            options={
                'managed': True,
                'db_table': 'plants_flower_color',
            },
        ),
        migrations.CreateModel(
            name='PlantFoliageColor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('foliage_color', models.ForeignKey(blank=True, null=True, to='plants.FoliageColor')),
                ('plants', models.ForeignKey(blank=True, null=True, to='plants.Plant')),
            ],
            options={
                'managed': True,
                'db_table': 'plants_foliage_color',
            },
        ),
        migrations.CreateModel(
            name='PlantFoodProd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('food_prod', models.ForeignKey(blank=True, null=True, to='plants.FoodProd')),
                ('plants', models.ForeignKey(blank=True, null=True, to='plants.Plant')),
            ],
            options={
                'managed': True,
                'db_table': 'plants_food_prod',
            },
        ),
        migrations.CreateModel(
            name='PlantFruitColor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('fruit_color', models.ForeignKey(blank=True, null=True, to='plants.FruitColor')),
                ('plants', models.ForeignKey(blank=True, null=True, to='plants.Plant')),
            ],
            options={
                'managed': True,
                'db_table': 'plants_fruit_color',
            },
        ),
        migrations.CreateModel(
            name='PlantHarvestPeriodByRegion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('harvest_period', models.ForeignKey(blank=True, null=True, to='plants.HarvestPeriod')),
                ('plants', models.ForeignKey(blank=True, null=True, to='plants.Plant')),
            ],
            options={
                'managed': True,
                'db_table': 'plants_harvest_period_by_region',
            },
        ),
        migrations.CreateModel(
            name='PlantHeightAtMaturityByRegion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('height', models.DecimalField(decimal_places=65535, blank=True, null=True, max_digits=65535)),
                ('plants', models.ForeignKey(blank=True, null=True, to='plants.Plant')),
            ],
            options={
                'managed': True,
                'db_table': 'plants_height_at_maturity_by_region',
            },
        ),
        migrations.CreateModel(
            name='PlantInsectAttractorByRegion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('insects', models.ForeignKey(blank=True, null=True, to='plants.Insects')),
                ('plants', models.ForeignKey(blank=True, null=True, to='plants.Plant')),
            ],
            options={
                'managed': True,
                'db_table': 'plants_insect_attractor_by_region',
            },
        ),
        migrations.CreateModel(
            name='PlantInsectRegulatorByRegion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('insects', models.ForeignKey(blank=True, null=True, to='plants.Insects')),
                ('plants', models.ForeignKey(blank=True, null=True, to='plants.Plant')),
            ],
            options={
                'managed': True,
                'db_table': 'plants_insect_regulator_by_region',
            },
        ),
        migrations.CreateModel(
            name='PlantLayer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('layer', models.ForeignKey(blank=True, null=True, to='plants.Layer')),
                ('plants', models.ForeignKey(blank=True, null=True, to='plants.Plant')),
            ],
            options={
                'managed': True,
                'db_table': 'plants_layer',
            },
        ),
        migrations.CreateModel(
            name='PlantLeafRetentionByRegion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('leaf_retention', models.ForeignKey(blank=True, null=True, to='plants.LeafRetention')),
                ('plants', models.ForeignKey(blank=True, null=True, to='plants.Plant')),
            ],
            options={
                'managed': True,
                'db_table': 'plants_leaf_retention_by_region',
            },
        ),
        migrations.CreateModel(
            name='PlantMedicinalsProd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('medicinals_prod', models.ForeignKey(blank=True, null=True, to='plants.MedicinalsProd')),
                ('plants', models.ForeignKey(blank=True, null=True, to='plants.Plant')),
            ],
            options={
                'managed': True,
                'db_table': 'plants_medicinals_prod',
            },
        ),
        migrations.CreateModel(
            name='PlantMineralNutrientsProd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('mineral_nutrients_prod', models.ForeignKey(blank=True, null=True, to='plants.MineralNutrientsProd')),
                ('plants', models.ForeignKey(blank=True, null=True, to='plants.Plant')),
            ],
            options={
                'managed': True,
                'db_table': 'plants_mineral_nutrients_prod',
            },
        ),
        migrations.CreateModel(
            name='PlantRawMaterialsProd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('plants', models.ForeignKey(blank=True, null=True, to='plants.Plant')),
            ],
            options={
                'managed': True,
                'db_table': 'plants_raw_materials_prod',
            },
        ),
        migrations.CreateModel(
            name='PlantShadeTolByRegion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('plants', models.ForeignKey(blank=True, null=True, to='plants.Plant')),
            ],
            options={
                'managed': True,
                'db_table': 'plants_shade_tol_by_region',
            },
        ),
        migrations.CreateModel(
            name='PlantSoilDrainageTolByRegion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('plants', models.ForeignKey(blank=True, null=True, to='plants.Plant')),
            ],
            options={
                'managed': True,
                'db_table': 'plants_soil_drainage_tol_by_region',
            },
        ),
        migrations.CreateModel(
            name='PlantSpreadAtMaturityByRegion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('spread', models.IntegerField(blank=True, null=True)),
                ('plants', models.ForeignKey(blank=True, null=True, to='plants.Plant')),
            ],
            options={
                'managed': True,
                'db_table': 'plants_spread_at_maturity_by_region',
            },
        ),
        migrations.CreateModel(
            name='PlantSunNeedsByRegion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('plants', models.ForeignKey(blank=True, null=True, to='plants.Plant')),
            ],
            options={
                'managed': True,
                'db_table': 'plants_sun_needs_by_region',
            },
        ),
        migrations.CreateModel(
            name='PlantWaterNeedsByRegion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('plants', models.ForeignKey(blank=True, null=True, to='plants.Plant')),
            ],
            options={
                'managed': True,
                'db_table': 'plants_water_needs_by_region',
            },
        ),
        migrations.CreateModel(
            name='RawMaterialsProd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('value', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'raw_materials_prod',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('value', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'regions',
            },
        ),
        migrations.CreateModel(
            name='SaltTol',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('value', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'salt_tol',
            },
        ),
        migrations.CreateModel(
            name='ShadeTol',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('value', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'shade_tol',
            },
        ),
        migrations.CreateModel(
            name='SoilDrainageTol',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('value', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'soil_drainage_tol',
            },
        ),
        migrations.CreateModel(
            name='SunNeeds',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('value', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'sun_needs',
            },
        ),
        migrations.CreateModel(
            name='Toxicity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('value', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'toxicity',
            },
        ),
        migrations.CreateModel(
            name='ToxinRemoval',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('value', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'toxin_removal',
            },
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('timestamp', models.DateTimeField()),
                ('transaction_type', models.TextField(blank=True, null=True)),
                ('plants_id', models.IntegerField(blank=True, null=True)),
                ('ignore', models.BooleanField()),
            ],
            options={
                'managed': True,
                'db_table': 'transactions',
            },
        ),
        migrations.CreateModel(
            name='UrlTags',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('value', models.TextField(blank=True, null=True)),
                ('plants', models.ForeignKey(to='plants.Plant')),
            ],
            options={
                'managed': True,
                'db_table': 'url_tags',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('username', models.TextField()),
                ('creation_timestamp', models.DateTimeField()),
                ('email', models.TextField()),
                ('enabled', models.BooleanField()),
                ('real_name', models.TextField()),
            ],
            options={
                'managed': True,
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='WaterNeeds',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('value', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'water_needs',
            },
        ),
        migrations.CreateModel(
            name='WindTol',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('value', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'wind_tol',
            },
        ),
        migrations.AddField(
            model_name='transactions',
            name='users',
            field=models.ForeignKey(to='plants.Users'),
        ),
        migrations.AddField(
            model_name='plantwaterneedsbyregion',
            name='regions',
            field=models.ForeignKey(blank=True, null=True, to='plants.Region'),
        ),
        migrations.AddField(
            model_name='plantwaterneedsbyregion',
            name='water_needs',
            field=models.ForeignKey(blank=True, null=True, to='plants.WaterNeeds'),
        ),
        migrations.AddField(
            model_name='plantsunneedsbyregion',
            name='regions',
            field=models.ForeignKey(blank=True, null=True, to='plants.Region'),
        ),
        migrations.AddField(
            model_name='plantsunneedsbyregion',
            name='sun_needs',
            field=models.ForeignKey(blank=True, null=True, to='plants.SunNeeds'),
        ),
        migrations.AddField(
            model_name='plantspreadatmaturitybyregion',
            name='regions',
            field=models.ForeignKey(blank=True, null=True, to='plants.Region'),
        ),
        migrations.AddField(
            model_name='plantsoildrainagetolbyregion',
            name='regions',
            field=models.ForeignKey(blank=True, null=True, to='plants.Region'),
        ),
        migrations.AddField(
            model_name='plantsoildrainagetolbyregion',
            name='soil_drainage_tol',
            field=models.ForeignKey(blank=True, null=True, to='plants.SoilDrainageTol'),
        ),
        migrations.AddField(
            model_name='plantshadetolbyregion',
            name='regions',
            field=models.ForeignKey(blank=True, null=True, to='plants.Region'),
        ),
        migrations.AddField(
            model_name='plantshadetolbyregion',
            name='shade_tol',
            field=models.ForeignKey(blank=True, null=True, to='plants.ShadeTol'),
        ),
        migrations.AddField(
            model_name='plantrawmaterialsprod',
            name='raw_materials_prod',
            field=models.ForeignKey(blank=True, null=True, to='plants.RawMaterialsProd'),
        ),
        migrations.AddField(
            model_name='plantleafretentionbyregion',
            name='regions',
            field=models.ForeignKey(blank=True, null=True, to='plants.Region'),
        ),
        migrations.AddField(
            model_name='plantinsectregulatorbyregion',
            name='regions',
            field=models.ForeignKey(blank=True, null=True, to='plants.Region'),
        ),
        migrations.AddField(
            model_name='plantinsectattractorbyregion',
            name='regions',
            field=models.ForeignKey(blank=True, null=True, to='plants.Region'),
        ),
        migrations.AddField(
            model_name='plantheightatmaturitybyregion',
            name='regions',
            field=models.ForeignKey(blank=True, null=True, to='plants.Region'),
        ),
        migrations.AddField(
            model_name='plantharvestperiodbyregion',
            name='regions',
            field=models.ForeignKey(blank=True, null=True, to='plants.Region'),
        ),
        migrations.AddField(
            model_name='plantfertilityneedsbyregion',
            name='regions',
            field=models.ForeignKey(blank=True, null=True, to='plants.Region'),
        ),
        migrations.AddField(
            model_name='planterosioncontrolbyregion',
            name='regions',
            field=models.ForeignKey(blank=True, null=True, to='plants.Region'),
        ),
        migrations.AddField(
            model_name='plantendemicstatusbyregion',
            name='regions',
            field=models.ForeignKey(blank=True, null=True, to='plants.Region'),
        ),
        migrations.AddField(
            model_name='plantdurationbyregion',
            name='regions',
            field=models.ForeignKey(blank=True, null=True, to='plants.Region'),
        ),
        migrations.AddField(
            model_name='plantcanopydensitybyregion',
            name='regions',
            field=models.ForeignKey(blank=True, null=True, to='plants.Region'),
        ),
        migrations.AddField(
            model_name='plantanimalregulatorbyregion',
            name='regions',
            field=models.ForeignKey(blank=True, null=True, to='plants.Region'),
        ),
        migrations.AddField(
            model_name='plantanimalattractorbyregion',
            name='regions',
            field=models.ForeignKey(blank=True, null=True, to='plants.Region'),
        ),
        migrations.AddField(
            model_name='plantactivegrowthperiodbyregion',
            name='regions',
            field=models.ForeignKey(blank=True, null=True, to='plants.Region'),
        ),
        migrations.AddField(
            model_name='plant',
            name='layer',
            field=models.ManyToManyField(to='plants.Layer', through='plants.PlantLayer'),
        ),
        migrations.AddField(
            model_name='plant',
            name='lifespan',
            field=models.ForeignKey(blank=True, null=True, to='plants.Lifespan'),
        ),
        migrations.AddField(
            model_name='plant',
            name='livestock_bloat',
            field=models.ForeignKey(blank=True, null=True, to='plants.LivestockBloat'),
        ),
        migrations.AddField(
            model_name='plant',
            name='salt_tol',
            field=models.ForeignKey(blank=True, null=True, to='plants.SaltTol'),
        ),
        migrations.AddField(
            model_name='plant',
            name='toxicity',
            field=models.ForeignKey(blank=True, null=True, to='plants.Toxicity'),
        ),
        migrations.AddField(
            model_name='plant',
            name='toxin_removal',
            field=models.ForeignKey(blank=True, null=True, to='plants.ToxinRemoval'),
        ),
        migrations.AddField(
            model_name='plant',
            name='wind_tol',
            field=models.ForeignKey(blank=True, null=True, to='plants.WindTol'),
        ),
        migrations.AddField(
            model_name='familycommonname',
            name='plants',
            field=models.ForeignKey(to='plants.Plant'),
        ),
        migrations.AddField(
            model_name='family',
            name='plants',
            field=models.ForeignKey(to='plants.Plant'),
        ),
        migrations.AlterUniqueTogether(
            name='djangocontenttype',
            unique_together=set([('app_label', 'model')]),
        ),
        migrations.AddField(
            model_name='djangoadminlog',
            name='content_type',
            field=models.ForeignKey(blank=True, null=True, to='plants.DjangoContentType'),
        ),
        migrations.AddField(
            model_name='djangoadminlog',
            name='user',
            field=models.ForeignKey(to='plants.AuthUser'),
        ),
        migrations.AddField(
            model_name='actions',
            name='regions',
            field=models.ForeignKey(blank=True, null=True, to='plants.Region'),
        ),
        migrations.AddField(
            model_name='actions',
            name='transactions',
            field=models.ForeignKey(blank=True, null=True, to='plants.Transactions'),
        ),
        migrations.CreateModel(
            name='PlantBehavior',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('plants.plant',),
        ),
        migrations.CreateModel(
            name='PlantCharacteristic',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('plants.plant',),
        ),
        migrations.CreateModel(
            name='PlantID',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('plants.plant',),
        ),
        migrations.CreateModel(
            name='PlantNeed',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('plants.plant',),
        ),
        migrations.CreateModel(
            name='PlantProduct',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('plants.plant',),
        ),
        migrations.CreateModel(
            name='PlantTolerance',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('plants.plant',),
        ),
        migrations.AlterUniqueTogether(
            name='urltags',
            unique_together=set([('value', 'plants')]),
        ),
        migrations.AlterUniqueTogether(
            name='plantwaterneedsbyregion',
            unique_together=set([('plants', 'regions')]),
        ),
        migrations.AlterUniqueTogether(
            name='plantsunneedsbyregion',
            unique_together=set([('plants', 'regions')]),
        ),
        migrations.AlterUniqueTogether(
            name='plantspreadatmaturitybyregion',
            unique_together=set([('plants', 'regions')]),
        ),
        migrations.AlterUniqueTogether(
            name='plantleafretentionbyregion',
            unique_together=set([('plants', 'regions')]),
        ),
        migrations.AlterUniqueTogether(
            name='plantheightatmaturitybyregion',
            unique_together=set([('plants', 'regions')]),
        ),
        migrations.AlterUniqueTogether(
            name='plantfertilityneedsbyregion',
            unique_together=set([('plants', 'regions')]),
        ),
        migrations.AlterUniqueTogether(
            name='planterosioncontrolbyregion',
            unique_together=set([('plants', 'regions')]),
        ),
        migrations.AlterUniqueTogether(
            name='plantdurationbyregion',
            unique_together=set([('plants', 'regions')]),
        ),
        migrations.AlterUniqueTogether(
            name='plantcanopydensitybyregion',
            unique_together=set([('plants', 'regions')]),
        ),
        migrations.AlterUniqueTogether(
            name='familycommonname',
            unique_together=set([('value', 'plants')]),
        ),
        migrations.AlterUniqueTogether(
            name='family',
            unique_together=set([('value', 'plants')]),
        ),
    ]
