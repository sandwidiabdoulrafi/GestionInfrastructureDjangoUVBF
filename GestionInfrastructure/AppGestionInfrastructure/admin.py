from django.contrib import admin

from AppGestionInfrastructure.models import Administration, Infrastructures, Interventions


@admin.register(Administration,Infrastructures,Interventions)

# Register your models here.
class GenericAdmin (admin.ModelAdmin):
    pass