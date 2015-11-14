# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0002_auto_20151112_1256'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actions',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='activegrowthperiod',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='allelopathic',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='animals',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='authgroup',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='authuser',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='biochemicalmaterialprod',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='canopydensity',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='culturalandamenityprod',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='djangoadminlog',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='djangocontenttype',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='djangomigrations',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='djangosession',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='droughttol',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='duration',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='endemicstatus',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='erosioncontrol',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='familycommonname',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='fertilityneeds',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='firetol',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='floodtol',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='flowercolor',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='foliagecolor',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='foodprod',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='fruitcolor',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='harvestperiod',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='humiditytol',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='insects',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='layer',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='leafretention',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='lifespan',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='livestockbloat',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='medicinalsprod',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='mineralnutrientsprod',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='plantactivegrowthperiodbyregion',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='plantanimalattractorbyregion',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='plantanimalregulatorbyregion',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='plantbiochemicalmaterialprod',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='plantcanopydensitybyregion',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='plantculturalandamenityprod',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='plantdurationbyregion',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='plantendemicstatusbyregion',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='planterosioncontrolbyregion',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='plantfertilityneedsbyregion',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='plantflowercolor',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='plantfoliagecolor',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='plantfoodprod',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='plantfruitcolor',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='plantharvestperiodbyregion',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='plantheightatmaturitybyregion',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='plantinsectattractorbyregion',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='plantinsectregulatorbyregion',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='plantlayer',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='plantleafretentionbyregion',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='plantmedicinalsprod',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='plantmineralnutrientsprod',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='plantrawmaterialsprod',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='plantshadetolbyregion',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='plantsoildrainagetolbyregion',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='plantspreadatmaturitybyregion',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='plantsunneedsbyregion',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='plantwaterneedsbyregion',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='rawmaterialsprod',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='salttol',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='shadetol',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='soildrainagetol',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='sunneeds',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='toxicity',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='toxinremoval',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='transactions',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='urltags',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='users',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='waterneeds',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='windtol',
            options={'managed': False},
        ),
        migrations.AddField(
            model_name='plant',
            name='biochemical_material_prod',
            field=models.ManyToManyField(to='plants.BiochemicalMaterialProd', through='plants.PlantBiochemicalMaterialProd'),
        ),
        migrations.AddField(
            model_name='plant',
            name='cultural_and_amenity_prod',
            field=models.ManyToManyField(to='plants.CulturalAndAmenityProd', through='plants.PlantCulturalAndAmenityProd'),
        ),
        migrations.AddField(
            model_name='plant',
            name='food_prod',
            field=models.ManyToManyField(to='plants.FoodProd', through='plants.PlantFoodProd'),
        ),
        migrations.AddField(
            model_name='plant',
            name='medicinals_prod',
            field=models.ManyToManyField(to='plants.MedicinalsProd', through='plants.PlantMedicinalsProd'),
        ),
        migrations.AddField(
            model_name='plant',
            name='mineral_nutrients_prod',
            field=models.ManyToManyField(to='plants.MineralNutrientsProd', through='plants.PlantMineralNutrientsProd'),
        ),
        migrations.AddField(
            model_name='plant',
            name='raw_materials_prod',
            field=models.ManyToManyField(to='plants.RawMaterialsProd', through='plants.PlantRawMaterialsProd'),
        ),
        migrations.AddField(
            model_name='plant',
            name='tags',
            field=models.CharField(blank=True, max_length=160, null=True),
        ),
    ]
