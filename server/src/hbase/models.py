from datetime import datetime

from django.db import models

# Create your models here.
from administer.models import Clusters


class Hbase(models.Model):
    ip = models.GenericIPAddressField(protocol='both')
    type = models.SmallIntegerField(default=0)
    status = models.CharField(default="", max_length=20)
    state = models.SmallIntegerField(default=0)
    web_port = models.IntegerField(null=True)
    rpyc_port = models.IntegerField(null=True)
    cluster = models.ForeignKey(Clusters, on_delete=models.CASCADE,default=1)
    updated_at = models.IntegerField(default=0)

class Metrics(models.Model):
    online_region = models.FloatField(default=0.0)
    used_heap = models.FloatField(default=0.0)
    max_heap = models.FloatField(default=0.0)
    no_stores = models.FloatField(default=0.0)
    no_store_files = models.FloatField(default=0.0)
    mem_store_size = models.FloatField(default=0.0)
    store_file_size = models.FloatField(default=0.0)
    read_request = models.FloatField(default=0.0)
    write_request = models.FloatField(default=0.0)
    node = models.ForeignKey(Hbase, on_delete=models.CASCADE,default=1)
    updated_at = models.IntegerField(default=0)
