from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    modules = models.CharField(max_length=256)

User.student = property(lambda u: Student.objects.get_or_create(user = u)[0])