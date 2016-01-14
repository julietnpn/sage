# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='family',
            field=models.ForeignKey(blank=True, to='plants.Family', null=True),
        ),
        migrations.AddField(
            model_name='plant',
            name='flower_color',
            field=models.ManyToManyField(to='plants.FlowerColor', through='plants.PlantFlowerColor'),
        ),
        migrations.AddField(
            model_name='plant',
            name='foliage_color',
            field=models.ManyToManyField(to='plants.FoliageColor', through='plants.PlantFoliageColor'),
        ),
        migrations.AddField(
            model_name='plant',
            name='fruit_color',
            field=models.ManyToManyField(to='plants.FruitColor', through='plants.PlantFruitColor'),
        ),
        migrations.AlterField(
            model_name='allelopathic',
            name='value',
            field=models.CharField(max_length=80, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='animals',
            name='value',
            field=models.CharField(max_length=80, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='family',
            name='plants',
            field=models.ForeignKey(blank=True, related_name='plants_plant_related', null=True, to='plants.Plant'),
        ),
        migrations.AlterField(
            model_name='family',
            name='value',
            field=models.CharField(max_length=160, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='familycommonname',
            name='value',
            field=models.CharField(max_length=160, null=True, blank=True),
        ),
    ]
