# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.

# from __future__ import unicode_literals
# from django.core.validators import MaxValueValidator, MinValueValidator
# from django.db.models import Q
# import json
# 
# 
# 
# 
from django.db import models
from login.models import AuthUser
from plants.models import Region



class Actions(models.Model):
    transactions = models.ForeignKey('Transactions', blank=True, null=True)
    action_type = models.TextField()
    regions = models.ForeignKey('plants.Region', blank=True, null=True)
    scientific_names = models.ForeignKey('plants.ScientificName', blank=True, null=True)
    property = models.TextField()
    value = models.TextField(blank=True, null=True)
    citation = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'actions'

    def __str__(self):
        return self.value


class Transactions(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    #timestamp_add = models.DateTimeField(auto_now_add=True)
    users = models.ForeignKey('login.AuthUser', blank=True, null=True)#Users
    transaction_type = models.TextField(blank=True, null=True)
    plants_id = models.IntegerField(blank=True, null=True)
    parent_transaction = models.IntegerField(blank=True, null=True)
    ignore = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'transactions'

    def __str__(self):
        return str(self.plants_id)

