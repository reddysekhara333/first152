from django.db import models

# Create your models here.
class modelform(models.Model):
    name=models.CharField(max_length=20)
    company=models.CharField(max_length=20)
    salary=models.FloatField()