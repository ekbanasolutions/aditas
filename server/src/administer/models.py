from django.db import models
from django.forms import ModelForm
from django import forms


# Create your models here.
class Clusters(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Nodes(models.Model):
    ip = models.GenericIPAddressField(protocol='both',unique=True)
    port = models.IntegerField(default=0)
    fqdn = models.CharField(max_length=50)
    hostname = models.CharField(max_length=50)
    name = models.CharField(max_length=50, default='')
    approved = models.SmallIntegerField(default=1)


class Services(models.Model):
    name = models.CharField(max_length=50)


class Service_cluster_reference(models.Model):
    service_id = models.IntegerField()
    cluster_id = models.ForeignKey(Clusters, on_delete=models.CASCADE)


class Service_table_ref(models.Model):
    service_id = models.IntegerField()
    table_name = models.CharField(max_length=50)
    metrics_table = models.CharField(max_length=50)

    class Meta:
        db_table = 'service_table_ref'
