from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Location(models.Model):
    user = models.ForeignKey(User, related_name='locations', on_delete=models.CASCADE)
    description = models.CharField(max_length=200)