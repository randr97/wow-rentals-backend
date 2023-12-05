from django.contrib import admin

from .models import OfficeLocation, Booking

# Register your models here.
admin.site.register(OfficeLocation)
admin.site.register(Booking)
