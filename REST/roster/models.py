from django.db import models

# Create your models here.
class Employee(models.Model):
    name_text = models.CharField(max_length=200)
    start_date = models.DateTimeField('date hired')

class Team(models.Model):
    name_text = models.CharField(max_length=200)
    teammate = models.ForeignKey(Employee) 
