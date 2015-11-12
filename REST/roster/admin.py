from django.contrib import admin
from .models import Team


# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    fields = ['creation_date', 'name_text']


admin.site.register(Team,TeamAdmin)
