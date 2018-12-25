from datetime import datetime

from django.db import models

# Create your models here.
from administer.models import Clusters


class Yarn(models.Model):
    ip = models.GenericIPAddressField(protocol='both')
    type = models.SmallIntegerField(default=0)
    status = models.CharField(default="", max_length=20)
    state = models.SmallIntegerField(default=0)
    web_port = models.IntegerField(null=True)
    rpyc_port = models.IntegerField(null=True)
    cluster = models.ForeignKey(Clusters, on_delete=models.CASCADE,default=1)
    updated_at = models.IntegerField(default=0)


class Metrics(models.Model):
    memory_capacity = models.FloatField(default=0.0)
    memory_used = models.FloatField(default=0.0)
    cpu_capacity = models.FloatField(default=0.0)
    cpu_used = models.FloatField(default=0.0)
    rack = models.CharField(default="", max_length=50)
    last_health_update = models.CharField(default="", max_length=30)
    node = models.ForeignKey(Yarn, on_delete=models.CASCADE, default=1)
    updated_at = models.IntegerField(default=0)
