from datetime import datetime

from django.db import models

# Create your models here.
from administer.models import Clusters


class Spark(models.Model):
    ip = models.GenericIPAddressField(protocol='both')
    type = models.SmallIntegerField(default=0)
    status = models.CharField(default="", max_length=20)
    state = models.SmallIntegerField(default=0)
    web_port = models.IntegerField(null=True)
    rpyc_port = models.IntegerField(null=True)
    cluster = models.ForeignKey(Clusters, on_delete=models.CASCADE,default=1)
    updated_at = models.IntegerField(default=0)

class Metrics(models.Model):
    total_cores = models.FloatField(default=0.0)
    cores_used = models.FloatField(default=0.0)
    cores_free = models.FloatField(default=0.0)
    total_memory = models.FloatField(default=0.0)
    memory_used = models.FloatField(default=0.0)
    last_heartbeat = models.CharField(default="", max_length=20)
    node = models.ForeignKey(Spark, on_delete=models.CASCADE,default=1)
    updated_at = models.IntegerField(default=0)
