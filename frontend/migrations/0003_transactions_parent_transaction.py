# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-04-04 19:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_auto_20160801_0250'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='parent_transaction',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]