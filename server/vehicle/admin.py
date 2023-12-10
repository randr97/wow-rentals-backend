from django.contrib import admin

from .models import Booking, OfficeLocation, Vehicle, Invoice

# Register your models here.
admin.site.register(OfficeLocation)
admin.site.register(Booking)
admin.site.register(Vehicle)
admin.site.register(Invoice)
