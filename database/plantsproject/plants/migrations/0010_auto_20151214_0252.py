# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0009_auto_20151206_0156'),
    ]

    operations = [
        migrations.CreateModel(
            name='TheFamily',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('value', models.CharField(null=True, max_length=160, blank=True)),
            ],
            options={
                'managed': True,
                'db_table': 'the_family',
            },
        ),
        migrations.CreateModel(
            name='TheFamilyCommonName',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('value', models.CharField(null=True, max_length=160, blank=True)),
            ],
            options={
                'managed': True,
                'db_table': 'the_family_common_name',
            },
        ),
        migrations.AlterField(
            model_name='familycommonname',
            name='plants',
            field=models.ForeignKey(to='plants.Plant', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='plant',
            name='family',
            field=models.ForeignKey(to='plants.TheFamily', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='plant',
            name='family_common_name',
            field=models.ForeignKey(to='plants.TheFamilyCommonName', null=True, blank=True),
        ),
    ]
