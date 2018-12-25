from django.db import models

# Create your models here.

class User_preferred_configuration(models.Model):
    service_id = models.IntegerField()
    key_name = models.CharField(max_length=200, unique=True)
    value = models.TextField(default="")
    key_type = models.CharField(max_length=100)


    def __str__(self):
        return self.key_name

class Backup_configuration(models.Model):
    service_id = models.IntegerField()
    key_name = models.CharField(max_length=200, unique=True)
    value = models.TextField(default="")
    key_type = models.CharField(max_length=100)


    def __str__(self):
        return self.key_name

class Restart_after_configuration(models.Model):
    service_id = models.CharField(max_length=100)
    status = models.PositiveSmallIntegerField(null=False)

    def __str__(self):
        return self.service_id


class sync_configuration(models.Model):
    sync_by = models.CharField(max_length=100)
    last_sync = models.DateTimeField()

    def __str__(self):
        return self.sync_by

class Default_configuration(models.Model):
    service_id = models.CharField(max_length=50)
    name = models.CharField(max_length=150)
    value = models.CharField(max_length=250,null=True)
    type = models.CharField(max_length=25)

    class Meta:
        unique_together = ('name', 'type',)

    def __str__(self):
        return self.service_id


