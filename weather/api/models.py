from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Location(models.Model):
    owner = models.ForeignKey(User, related_name='locations', on_delete=models.CASCADE)
    description = models.CharField(max_length=200)

class Parameter(models.Model):
    name = models.CharField(max_length=20)
    location = models.ForeignKey(Location, related_name='parameters', on_delete=models.CASCADE)
    values = models.JSONField()
