# Generated by Django 2.0.7 on 2018-10-21 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0012_auto_20180712_1851'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plantscientificname',
            old_name='value',
            new_name='category',
        ),
    ]