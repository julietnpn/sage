# Generated by Django 2.0.7 on 2018-10-22 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_authuser_is_data_import'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='is_data_import',
            field=models.BooleanField(default=False),
        ),
    ]
