from django.db import models

# Create your models here.

class Roles(models.Model):
    Id = models.AutoField(primary_key=True)
    rName = models.CharField(max_length=128)
    Power = models.CommaSeparatedIntegerField(max_length=256)

    def __unicode__(self):
        return str(Id)

class Users(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=128)
    uName = models.CharField(max_length=256)
    uPass = models.CharField(max_length=70)
    Role = models.ForeignKey(Roles)
    exPower = models.CommaSeparatedIntegerField(max_length=256)
    Telephone = models.CharField(max_length=16)
    Email = models.CharField(max_length=256)
    Addr = models.CharField(max_length=256)
    Postcode = models.CharField(max_length=8)
    Province = models.CharField(max_length=8)
    Addtime = models.DateField(auto_now_add=True)
    Lastlogon = models.DateTimeField()
    Check = models.BooleanField()

    def __unicode__(self):
        return str(Id)
