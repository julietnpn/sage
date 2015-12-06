# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0008_auto_20151120_1252'),
    ]

    operations = [
        migrations.CreateModel(
            name='NutrientRquirements',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('value', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'fertility_needs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PlantNutrientRquirementsByRegion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'plants_fertility_needs_by_region',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DegreeOfSerotiny',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('value', models.TextField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'degree_of_serotiny',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Serotiny',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('value', models.TextField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'serotiny',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='plant',
            name='allelochemicals',
            field=models.CharField(null=True, blank=True, max_length=160),
        ),
        migrations.AlterField(
            model_name='plant',
            name='fertility_needs',
            field=models.ManyToManyField(verbose_name='Nutrient Rquirements', to='plants.NutrientRquirements', through='plants.PlantNutrientRquirementsByRegion'),
        ),
        migrations.AddField(
            model_name='plant',
            name='degree_of_serotiny',
            field=models.ForeignKey(null=True, to='plants.DegreeOfSerotiny', blank=True),
        ),
        migrations.AddField(
            model_name='plant',
            name='serotiny',
            field=models.ForeignKey(null=True, to='plants.Serotiny', blank=True),
        ),
    ]
