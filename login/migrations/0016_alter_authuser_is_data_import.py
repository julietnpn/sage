# Generated by Django 4.0.4 on 2022-05-17 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0015_alter_authuser_is_data_import'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='is_data_import',
            field=models.BooleanField(blank=True, default=False),
            preserve_default=False,
        ),
    ]
