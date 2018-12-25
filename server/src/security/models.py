from django.db import models
from datetime import datetime
# Create your models here.
class Api_key(models.Model):
    key = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.today().replace(microsecond=0))