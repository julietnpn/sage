# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-31 01:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20160731_0115'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='authgroup',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='authgrouppermissions',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='authpermission',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='authuser',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='authusergroups',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='authuseruserpermissions',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='djangoadminlog',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='djangocontenttype',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='djangomigrations',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='djangosession',
            options={'managed': False},
        ),
    ]