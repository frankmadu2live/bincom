from django.db import models

# Create your models here.


class Agentname(models.Model):
    name_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.CharField(max_length=200, default='')
    phone = models.IntegerField(blank=True, null=True)
    pollingunit_uniqueid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agentname'

    def __str__(self):
        return self.firstname


class AnnouncedPuResults(models.Model):
    result_id = models.AutoField(primary_key=True)
    polling_unit_uniqueid = models.CharField(max_length=200)
    party_abbreviation = models.CharField(max_length=200)
    party_score = models.IntegerField(blank=True, null=True)
    entered_by_user = models.TextField(blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    user_ip_address = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'announced_pu_results'

    def __str__(self):
        return self.party_abbreviation


class Lga(models.Model):
    uniqueid = models.AutoField(primary_key=True)
    lga_id = models.IntegerField(blank=True, null=True)
    lga_name = models.CharField(max_length=200)
    state_id = models.IntegerField(blank=True, null=True)
    lga_description = models.TextField(blank=True, null=True)
    entered_by_user = models.CharField(max_length=200)
    date_entered = models.DateTimeField(blank=True, null=True)
    user_ip_address = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'lga'

    def __str__(self):
        return self.lga_name
    
class Party(models.Model):
    partyid = models.CharField(max_length=200)
    partyname = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'party'

    def __str__(self):
        return self.partyname


class PollingUnit(models.Model):
    uniqueid = models.AutoField(primary_key=True)
    polling_unit_id = models.IntegerField(blank=True, null=True)
    ward_id = models.IntegerField(blank=True, null=True)
    lga_id = models.IntegerField(blank=True, null=True)
    uniquewardid = models.IntegerField(blank=True, null=True)
    polling_unit_number = models.CharField(max_length=200, blank=True, null=True)
    polling_unit_name = models.CharField(max_length=200, blank=True, null=True)
    polling_unit_description = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=200, blank=True, null=True)
    long = models.CharField(max_length=200, blank=True, null=True)
    entered_by_user = models.CharField(max_length=200, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    user_ip_address = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'polling_unit'

    def __str__(self):
        return self.polling_unit_name


class States(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'states'

    def __str__(self):
        return self.state_name


class Ward(models.Model):
    uniqueid = models.AutoField(primary_key=True)
    ward_id = models.IntegerField(blank=True, null=True)
    ward_name = models.CharField(max_length=200)
    lga_id = models.IntegerField(blank=True, null=True)
    ward_description = models.TextField(blank=True, null=True)
    entered_by_user = models.CharField(max_length=200)
    date_entered = models.DateTimeField(blank=True, null=True)
    user_ip_address = models.CharField(max_length=200)

    class Meta:
        managed = False 
        db_table = 'ward'

    def __str__(self):
        return self.ward_name