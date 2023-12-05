from django.contrib import admin

from .models import OfficeLocation, Booking, Vehicle

# Register your models here.
admin.site.register(OfficeLocation)
admin.site.register(Booking)
admin.site.register(Vehicle)
