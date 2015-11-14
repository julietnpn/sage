# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0005_auto_20151113_0116'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='duration',
            field=models.ManyToManyField(through='plants.PlantDurationByRegion', to='plants.Duration'),
        ),
        migrations.AddField(
            model_name='plant',
            name='height',
            field=models.ManyToManyField(to='plants.PlantHeightAtMaturityByRegion'),
        ),
        migrations.AddField(
            model_name='plant',
            name='spread',
            field=models.ManyToManyField(to='plants.PlantSpreadAtMaturityByRegion'),
        ),
    ]
