# Generated by Django 2.0.4 on 2018-06-26 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_auto_20180626_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='authuser',
            name='affiliation',
            field=models.CharField(default='NONE', max_length=254),
        ),
        migrations.AddField(
            model_name='authuser',
            name='experience',
            field=models.CharField(default='NONE', max_length=512),
        ),
        migrations.AddField(
            model_name='authuser',
            name='interestes',
            field=models.CharField(default='NONE', max_length=512),
        ),
    ]