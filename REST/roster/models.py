from django.db import models

import datetime
from django.utils import timezone
# Create your models here.

class Team(models.Model):
    name_text = models.CharField(max_length=200)
    creation_date = models.DateTimeField('date created')

    def __string__(self):
        return self.name_text

class Employee(models.Model):
    name_text = models.CharField(max_length=200)
    start_date = models.DateTimeField('date hired')
    team = models.ForeignKey(Team)

    def __string__(self):
        return self.name_text
