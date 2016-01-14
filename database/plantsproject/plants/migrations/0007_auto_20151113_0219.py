# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0006_auto_20151113_0144'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='active_growth_period',
            field=models.ManyToManyField(to='plants.ActiveGrowthPeriod', through='plants.PlantActiveGrowthPeriodByRegion'),
        ),
        migrations.AddField(
            model_name='plant',
            name='canopy_density',
            field=models.ManyToManyField(to='plants.CanopyDensity', through='plants.PlantCanopyDensityByRegion'),
        ),
        migrations.AddField(
            model_name='plant',
            name='erosion_control',
            field=models.ManyToManyField(to='plants.ErosionControl', through='plants.PlantErosionControlByRegion'),
        ),
        migrations.AddField(
            model_name='plant',
            name='harvest_period',
            field=models.ManyToManyField(to='plants.HarvestPeriod', through='plants.PlantHarvestPeriodByRegion'),
        ),
        migrations.AddField(
            model_name='plant',
            name='leaf_retention',
            field=models.ManyToManyField(to='plants.LeafRetention', through='plants.PlantLeafRetentionByRegion'),
        ),
        migrations.AddField(
            model_name='plant',
            name='plants_animal_attractor',
            field=models.ManyToManyField(to='plants.Animals', through='plants.PlantAnimalAttractorByRegion', related_name='a_plants_animal_attractor_related'),
        ),
        migrations.AddField(
            model_name='plant',
            name='plants_animal_regulator',
            field=models.ManyToManyField(to='plants.Animals', through='plants.PlantAnimalRegulatorByRegion'),
        ),
        migrations.AddField(
            model_name='plant',
            name='plants_insect_attractor',
            field=models.ManyToManyField(to='plants.Insects', through='plants.PlantInsectAttractorByRegion', related_name='a_plants_insect_attractor_related'),
        ),
        migrations.AddField(
            model_name='plant',
            name='plants_insect_regulator',
            field=models.ManyToManyField(to='plants.Insects', through='plants.PlantInsectRegulatorByRegion'),
        ),
    ]
