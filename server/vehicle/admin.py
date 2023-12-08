from django.contrib import admin

from .models import Booking, OfficeLocation, Vehicle

# Register your models here.
admin.site.register(OfficeLocation)
admin.site.register(Booking)
admin.site.register(Vehicle)
