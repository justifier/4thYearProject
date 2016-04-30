from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key= True)
    modules = models.CharField(max_length=256)
    type = models.CharField(max_length=64, default='Student')

User.profile = property(lambda u: Profile.objects.get_or_create(user = u)[0])