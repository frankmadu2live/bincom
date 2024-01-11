# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Agentname(models.Model):
    name_id = models.AutoField(primary_key=True)
    firstname = models.TextField()
    lastname = models.TextField()
    email = models.TextField(blank=True, null=True)
    phone = models.TextField()
    pollingunit_uniqueid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'agentname'


class AnnouncedPuResults(models.Model):
    result_id = models.AutoField(primary_key=True, blank=True, null=True)
    polling_unit_uniqueid = models.TextField()
    party_abbreviation = models.CharField()
    party_score = models.IntegerField()
    entered_by_user = models.TextField()
    date_entered = models.DateTimeField()
    user_ip_address = models.TextField()

    class Meta:
        managed = False
        db_table = 'announced_pu_results'


class Lga(models.Model):
    uniqueid = models.AutoField(primary_key=True, blank=True, null=True)
    lga_id = models.IntegerField()
    lga_name = models.CharField()
    state_id = models.IntegerField()
    lga_description = models.TextField(blank=True, null=True)
    entered_by_user = models.CharField()
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField()

    class Meta:
        managed = False
        db_table = 'lga'


class Party(models.Model):
    partyid = models.CharField()
    partyname = models.CharField()

    class Meta:
        managed = False
        db_table = 'party'


class PollingUnit(models.Model):
    uniqueid = models.AutoField(primary_key=True, blank=True, null=True)
    polling_unit_id = models.IntegerField()
    ward_id = models.IntegerField()
    lga_id = models.IntegerField()
    uniquewardid = models.IntegerField(blank=True, null=True)
    polling_unit_number = models.CharField(blank=True, null=True)
    polling_unit_name = models.CharField(blank=True, null=True)
    polling_unit_description = models.TextField(blank=True, null=True)
    lat = models.CharField(blank=True, null=True)
    long = models.CharField(blank=True, null=True)
    entered_by_user = models.CharField(blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    user_ip_address = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'polling_unit'


class States(models.Model):
    state_id = models.AutoField(primary_key=True, blank=True, null=True)
    state_name = models.CharField()

    class Meta:
        managed = False
        db_table = 'states'


class Ward(models.Model):
    uniqueid = models.AutoField(primary_key=True, blank=True, null=True)
    ward_id = models.IntegerField()
    ward_name = models.TextField()
    lga_id = models.IntegerField()
    ward_description = models.TextField(blank=True, null=True)
    entered_by_user = models.TextField()
    date_entered = models.DateTimeField()
    user_ip_address = models.TextField()

    class Meta:
        managed = False
        db_table = 'ward'
