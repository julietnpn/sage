# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-08 01:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0011_auto_20160307_1659'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlantBarrier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barrier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='plants.Barrier')),
                ('plants', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='plants.Plant')),
                ('regions', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='plants.Region')),
            ],
            options={
                'db_table': 'plants_barrier',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PlantRegion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('spread', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('root_depth', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('plants', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='plants.Plant')),
                ('regions', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='plants.Region')),
            ],
            options={
                'db_table': 'plants_region',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='plant',
            name='barrier',
            field=models.ManyToManyField(through='plants.PlantBarrier', to='plants.Barrier'),
        ),
        migrations.AddField(
            model_name='plant',
            name='region',
            field=models.ManyToManyField(through='plants.PlantRegion', to='plants.Region'),
        ),
        migrations.AlterUniqueTogether(
            name='plantregion',
            unique_together=set([('plants', 'regions')]),
        ),
        migrations.AlterUniqueTogether(
            name='plantbarrier',
            unique_together=set([('plants', 'regions')]),
        ),
    ]