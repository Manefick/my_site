from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    max_students = models.IntegerField()
