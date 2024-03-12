from django.contrib import admin

# Register your models here.
from vehicles.models import vehicles
class VehiclesAdmin(admin.ModelAdmin):
    list_display=('vehicles_name','vehicles_seat','vehicles_door','vehicles_luggage','vehicles_price','vehicles_description','vehicles_image')

admin.site.register(vehicles,VehiclesAdmin)