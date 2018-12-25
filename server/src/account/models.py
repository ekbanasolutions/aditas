from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=255, unique=True)
    salt = models.CharField(max_length=255)
    hashed_password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

class Role(models.Model):
    name = models.CharField(max_length=255, blank=False)

class Permission(models.Model):
    name = models.CharField(max_length=255, blank=True)
    content_type_id = models.IntegerField()
    code_name = models.CharField(max_length=255, blank=False)

class Role_permission(models.Model):
    role_id = models.IntegerField()
    permission_id = models.IntegerField()

class User_role(models.Model):
    user_id = models.IntegerField()
    role_id = models.IntegerField()



