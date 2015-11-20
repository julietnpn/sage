# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0007_auto_20151113_0219'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'managed': False,
                'db_table': 'auth_group_permissions',
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'managed': False,
                'db_table': 'auth_permission',
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'managed': False,
                'db_table': 'auth_user_groups',
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'managed': False,
                'db_table': 'auth_user_user_permissions',
            },
        ),
        migrations.RemoveField(
            model_name='plant',
            name='family',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='family_common_name',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='urltags',
        ),
        migrations.AlterField(
            model_name='plant',
            name='ph_max',
            field=models.DecimalField(decimal_places=4, validators=[django.core.validators.MaxValueValidator(14, message='pH should be in range 0-14')], null=True, max_digits=6, db_column='pH_max', blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='ph_min',
            field=models.DecimalField(decimal_places=4, validators=[django.core.validators.MaxValueValidator(14, message='pH should be in range 0-14')], null=True, max_digits=6, db_column='pH_min', blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='family',
            unique_together=set([]),
        ),
    ]
