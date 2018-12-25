from datetime import datetime

from django.db import models

# Create your models here.
from administer.models import Clusters


class Elastic_search(models.Model):
    ip = models.GenericIPAddressField(protocol='both')
    type = models.SmallIntegerField(default=0)
    status = models.CharField(default="", max_length=20)
    state = models.SmallIntegerField(default=0)
    web_port = models.IntegerField(null=True)
    rpyc_port = models.IntegerField(null=True)
    cluster = models.ForeignKey(Clusters, on_delete=models.CASCADE,default=1)
    updated_at = models.IntegerField(default=0)


class Metrics(models.Model):
    cpu_percent = models.FloatField(default=0.0)
    total_memory = models.FloatField(default=0.0)
    free_memory = models.FloatField(default=0.0)
    used_memory = models.FloatField(default=0.0)
    swap_total_memory = models.FloatField(default=0.0)
    swap_used_memory = models.FloatField(default=0.0)
    swap_free_memory = models.FloatField(default=0.0)
    node = models.ForeignKey(Elastic_search, on_delete=models.CASCADE,default=1)
    updated_at = models.IntegerField(default=0)
