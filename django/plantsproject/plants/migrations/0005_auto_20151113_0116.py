# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0004_auto_20151113_0106'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='endemic_status',
            field=models.ManyToManyField(to='plants.EndemicStatus', through='plants.PlantEndemicStatusByRegion'),
        ),
        migrations.AddField(
            model_name='plant',
            name='urltags',
            field=models.ForeignKey(to='plants.UrlTags', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='familycommonname',
            name='plants',
            field=models.ForeignKey(to='plants.Plant', related_name='plants_plant_family_common_name_related', blank=True, null=True),
        ),
    ]
