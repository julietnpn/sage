# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-08 00:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0008_auto_20160307_1633'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='plantregion',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='plantregion',
            name='plants',
        ),
        migrations.RemoveField(
            model_name='plantregion',
            name='regions',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='regions',
        ),
        migrations.DeleteModel(
            name='PlantRegion',
        ),
    ]