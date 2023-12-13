from django.contrib import admin

from .models import Booking, Invoice, OfficeLocation, Vehicle


# Register your models here.
@admin.register(OfficeLocation)
class OfficeLocationAdmin(admin.ModelAdmin):
    search_fields = [field.name for field in OfficeLocation._meta.fields]
    list_display = [field.name for field in OfficeLocation._meta.fields]


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    search_fields = [field.name for field in Booking._meta.fields]
    list_display = [field.name for field in Booking._meta.fields]


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    search_fields = [field.name for field in Vehicle._meta.fields]
    list_display = [field.name for field in Vehicle._meta.fields]


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    search_fields = [field.name for field in Invoice._meta.fields]
    list_display = [field.name for field in Invoice._meta.fields]
