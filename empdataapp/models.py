from django.db import models


class EmpdataFake(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    salary = models.BigIntegerField()
    email = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    hometown = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    skill = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    percentage = models.BigIntegerField()
