from django.contrib import admin
from .models import Team


# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    fieldsets = [
            (None,  {'fields': ['name_text']}),
            ('Date created', {'fields': ['creation_date']}),
    ]

admin.site.register(Team,TeamAdmin)
