from django.db import models
from datetime import datetime


class Company(models.Model):
    CompanyCode=models.IntegerField(primary_key=True)
    CompanyName=models.CharField(max_length=24)
    PresidentEmail= models.CharField(max_length=24)
   