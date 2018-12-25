from datetime import datetime

from django.db import models

# Create your models here.
from administer.models import Clusters


class Hdfs(models.Model):
    ip = models.GenericIPAddressField(protocol='both')
    type = models.SmallIntegerField(default=0)
    status = models.CharField(default="",max_length=20)
    state = models.SmallIntegerField(default=0)
    web_port = models.IntegerField(null=True)
    rpyc_port = models.IntegerField(null=True)
    safemode = models.SmallIntegerField(default=0,null=True)
    cluster = models.ForeignKey(Clusters, on_delete=models.CASCADE,default=1)
    # updated_at = models.DateTimeField(default=datetime.today().replace(microsecond=0))
    updated_at = models.IntegerField(default=0)

class Metrics(models.Model):
    capacity = models.FloatField(default=0.0)
    non_dfs_used = models.FloatField(default=0.0)
    num_blocks = models.FloatField(default=0.0)
    used_space = models.FloatField(default=0.0)
    decommissioned = models.SmallIntegerField(default=0)
    node = models.ForeignKey(Hdfs, on_delete=models.CASCADE, default=1)
    # updated_at = models.DateTimeField(default=datetime.today().replace(microsecond=0))
    updated_at = models.IntegerField(default=0)

