from django.db import models

class Office(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)

class Worker(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    hire_date = models.DateField()
    profession = models.CharField(max_length=100)
    offices = models.ManyToManyField('Office', related_name='workers')
