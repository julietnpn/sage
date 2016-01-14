# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0003_auto_20151112_1444'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='familycommonname',
            options={'managed': True},
        ),
        migrations.AddField(
            model_name='plant',
            name='family_common_name',
            field=models.ForeignKey(to='plants.FamilyCommonName', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plant',
            name='fertility_needs',
            field=models.ManyToManyField(to='plants.FertilityNeeds', through='plants.PlantFertilityNeedsByRegion'),
        ),
        migrations.AddField(
            model_name='plant',
            name='shade_tol',
            field=models.ManyToManyField(to='plants.ShadeTol', through='plants.PlantShadeTolByRegion'),
        ),
        migrations.AddField(
            model_name='plant',
            name='soil_drainage_tol',
            field=models.ManyToManyField(to='plants.SoilDrainageTol', through='plants.PlantSoilDrainageTolByRegion'),
        ),
        migrations.AddField(
            model_name='plant',
            name='sun_needs',
            field=models.ManyToManyField(to='plants.SunNeeds', through='plants.PlantSunNeedsByRegion'),
        ),
        migrations.AddField(
            model_name='plant',
            name='water_needs',
            field=models.ManyToManyField(to='plants.WaterNeeds', through='plants.PlantWaterNeedsByRegion'),
        ),
    ]
