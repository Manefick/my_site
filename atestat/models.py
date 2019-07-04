from django.db import models
from students.models import Student

class Atestat(models.Model):
    name_subject = models.CharField(max_length=255, null=False, blank=False)
    mark = models.IntegerField()
    date = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)